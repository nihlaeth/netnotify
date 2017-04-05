# netnotify

A simple python daemon for receiving desktop notifications over the network using dbus


## Author

Written by nihlaeth (info@nihlaeth.nl)

The issi plugin is based on the irssi-libnotify plugin: https://code.google.com/p/irssi-libnotify/

## Installation

Requirements:
* dbus-python

For irssi notifications:
* perl
* irssi
* HTML::Entities (perl module)

```
$ pip install .
# if you want to install the server:
$ pip install ".[server]"
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
$ netnotify --generate-config > ~/.config/netnotify/client.cfg
$ vim ~/.config/netnotify/client.cfg
$ netnotify --title Title --message "Body of the notification \nEasy, right?"
```

## Irssi
Put the netnotify.py script somwhere in your path (I suggest  /usr/bin/) and make sure the right ip/hostname
is in it. Now put the netnotify.pl script in the .irssi/scripts dir inside your home directory. From irssi run:;

	/script load netnotify

To load the script automatically, copy it to the .irssi/scripts/autorun/ directory, or even better, place a 
symlink.

Be aware that the notifications are sent in plain text at this time. That means that if you send the notifications
over the net, your highlights and private messages can be spied upon, and anyone can spam your screen with notifications.

## To Do
* assign urgency to notifications
* use ssh
* allow client to set application name and icon
