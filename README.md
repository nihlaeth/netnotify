netnotify
=========

A simply python daemon for receiving desktop notifications from the network using libnotify


Author
==========

Written by nihlaeth (info@nihlaeth.nl)

The issi plugin is based on the irssi-libnotify plugin: https://code.google.com/p/irssi-libnotify/

Installation
==========

Requirements:
* libnotify
* a notification daemon like dunst
* python
* notify-python / python-notify / pynotify
* gnu-screen
* telnet (optional)

For irssi notifications:
* perl
* irssi
* HTML::Entities (perl module)

The notification daemon has to be started inside a screen:

	$ screen -S netnotify
	$ notify-daemon.py

To detach, press Ctrl+a+d

To send a notification from the system the daemon is running on (localhost), simply run:

	$ netnotify.py "Title:Body of the notification \nEasy, right?"

To send notifications from remote hosts, edit the ip address inside the notify-send.py script to
that of the host on which the daemon is running.

You can also use the notify.sh script, though at this time it doesn't take command line arguments yet.
You can edit the script to send different messages.

Irssi
=========
Put the netnotify.py script somwhere in your path (I suggest  /usr/bin/) and make sure the right ip/hostname
is in it. Now put the netnotify.pl script in the .irssi/scripts dir inside your home directory. From irssi run:;

	/script load netnotify

To load the script automatically, copy it to the .irssi/scripts/autorun/ directory, or even better, place a 
symlink.

Be aware that the notifications are sent in plain text at this time. That means that if you send the notifications
over the net, your highlights and private messages can be spied upon regardless of you using ssl.

To Do
==========
* have the notify.sh script read command line input
* assign urgency to notifications
* encrypt the notifications (they are sent plain text at the moment)


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
