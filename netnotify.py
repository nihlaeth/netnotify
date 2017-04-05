import logging
import socket
import sys
import daemonocle
import notify2
from user_config import Config, Section, StringOption, IntegerOption

class ServerConfig(Config):

    """netnotify server configuration."""

    application = "netnotify"
    author = "nihlaeth"

    class ServerSection(Section):
        listen = StringOption(doc='IP to listen on', default='0.0.0.0')
        port = IntegerOption(doc='port to listen on', default=5757)
        pid_file = StringOption(
            doc='path to PID file', default='/tmp/netnotify.pid')

    server = ServerSection()

    class LogSection(Section):
        log_file = StringOption(
            doc='file to write logs to', default='/var/log/netnotify.log')
        verbosity = StringOption(
            doc='one of critical, error, warning, info, debug or notset',
            default='warning')

    logging = LogSection()

def notification_daemon():
    config = ServerConfig(file_name="server", cli=False)
    logging.basicConfig(
        filename=config.logging.log_file,
        level=getattr(logging, config.logging.verbosity.upper()),
        format='%(asctime)s [%(levelname)s] %(message)s',
        )
    logging.info("server starting")
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error, msg:
        logging.critical("Failed to create socket: {}".format(msg))
        sys.exit()
    logging.debug("Created socket")
    port = 5757
    server_socket.bind((config.server.listen, config.server.port))
    logging.debug("Now listening on port".format(config.server.port))

    server_socket.listen(10)
    notify2.init("Python notification Daemon")
    while True:
        client, address = server_socket.accept()
        data = client.recv(4096)
        logging.info("Got connection from {}: {}".format(address, data))
        datalist = data.split(":", 1)
        title = datalist[0]
        try:
            body = datalist[1]
        except IndexError:
            print "No notification body received, using title"
            body = title
        notification = notify2.Notification(title, body)
        notification.show()
        client.close()

def usage():
    print("netnotify daemon")
    print("Daemon actions: {}".format(daemonocle.Daemon.list_actions()))
    print("Generate configuration file: --generate-config")

def daemon_controller():
    if len(sys.argv) < 2:
        usage()
    elif sys.argv[1] in daemonocle.Daemon.list_actions():
        config = ServerConfig(file_name="server", cli=False)
        daemon = daemonocle.Daemon(
            detach=False,
            worker=notification_daemon,
            pidfile=config.server.pid_file)
        daemon.do_action(sys.argv[1])
    elif sys.argv[1] == "--generate-config":
        config = ServerConfig(file_name="server")
    else:
        usage()

def send():
    message = sys.argv[1]
    notification_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    notification_socket.connect(("127.0.0.1", 5757)) #seshata
    notification_socket.send(message)
    notification_socket.close()
