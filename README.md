# netnotify

A simple python daemon for receiving desktop notifications from the network using libnotify


## Author

Written by nihlaeth (info@nihlaeth.nl)

The issi plugin is based on the irssi-libnotify plugin: https://code.google.com/p/irssi-libnotify/

## Installation

Requirements:
* libnotify

For irssi notifications:
* perl
* irssi
* HTML::Entities (perl module)

```
$ pip install .
```

## Usage
The notification daemon has to be configured:
```
$ netnotifyd --generate-config > ~/.config/netnotify/server.cfg
$ vim ~/.config/netnotify/server.cfg
$ netnotifyd start
```


To send a notification:
```
$ netnotify "Title:Body of the notification \nEasy, right?"
```

You can also use the notify.sh script, though at this time it doesn't take command line arguments yet.
You can edit the script to send different messages.

## Irssi
Put the netnotify.py script somwhere in your path (I suggest  /usr/bin/) and make sure the right ip/hostname
is in it. Now put the netnotify.pl script in the .irssi/scripts dir inside your home directory. From irssi run:;

	/script load netnotify

To load the script automatically, copy it to the .irssi/scripts/autorun/ directory, or even better, place a 
symlink.

Be aware that the notifications are sent in plain text at this time. That means that if you send the notifications
over the net, your highlights and private messages can be spied upon regardless of you using ssl.

## To Do
* assign urgency to notifications
* use ssh
