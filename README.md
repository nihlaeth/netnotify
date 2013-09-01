netnotify
=========

A simply python daemon for receiving desktop notifications from the network using libnotify


Author
==========

Written by nihlaeth (info@nihlaeth.nl)

Installation
==========

Requirements:
* libnotify
* a notification daemon like dunst
* python
* notify-python / python-notify / pynotify
* gnu-screen
* telnet (optional)

The notification daemon has to be started inside a screen:
    $ screen -S netnotify
    $ notify-daemon.py

To detach, press Ctrl+a+d

To send a notification from the system the daemon is running on (localhost), simply run:
    $ notify-send.py "Title:Body of the notification \nEasy, right?"

To send notifications from remote hosts, edit the ip address inside the notify-send.py script to
that of the host on which the daemon is running.

You can also use the notify.sh script, though at this time it doesn't take command line arguments yet.
You can edit the script to send different messages.

To Do
==========
* have the notify.sh script read command line input
* assign urgency to notifications
* write an irssi plugin to work with the netnotify daemon


Troubleshooting
==========
If no notifications are popping up and you're not getting errors, something may be wrong with your
notification daemon. Test it by executing:
    $ notify-send Test "This is a test"

If you can send notifications from localhost but not from remote hosts, it's probably a firewall issue.
Check the local machine's firewall, it should allow tcp traffic on port 5757. Also check if your router
or modem allows traffic on port 5757. If you're sending notifications from outside your LAN port 5757 
has to be forwarded.

Not being able to send notifications from localhost CAN also be a firewall issue, though that's usually
a sign of an overzealous system administrator.
