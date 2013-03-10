pyxtrlock
=========

``pyxtrlock`` is a rewrite of Ian Jackson's great ``xtrlock`` program using
modern libraries, most importantly the obsolete direct passwd/shadow
authentication has been replaced by today's
[PAM](http://en.wikipedia.org/wiki/Pluggabe_authentication_module) authentication
mechanism, hence it also works on Fedora. Also, it's mostly written using
[XCB](http://xcb.freedesktop.org/) instead of Xlib, although some Xlib/XCB
interaction is still necessary. As soon as XCB can provide the required
services of Xlib, the remaining code will be ported to XCB.

Since pyxtrlock uses PAM authentication, it can be run as the normal user and
doesn't need special privileges.

Usage
-----
pyxtrlock, like its predecessor, is a very minimal X display lock program. While
pyxtrlock is running, it doesn't obscure the screen, only the mouse and keyboard
are grabbed and the mouse cursor becomes a padlock. Output displayed by X
programs, and windows put up by new X clients, continue to be visible, and any
new output is displayed normally.

In good Unix tradition, pyxtrlock provides no visual feedback during password
entry. You simply type your password at it, followed by Enter or Newline.
Pressing Backspace or Delete erases one character of a password partially typed;
pressing Escape or Clear clears anything that has been entered.

Like xtrlock, pyxtrlock will ignore further keystrokes until a timeout has
expired after too many attempts have been made in too short time.

Installation
------------
pyxtrlock requires [python3-pam](https://github.com/leonnnn/python3-pam). Make
sure to install this package before installing pyxtrlock.

After that, [download pyxtrlock from github](https://github.com/leonnnn/pyxtrlock),
and run ``python3 setup.py install`` as root. Once this is done, you should be
able to simply lock your display by running

    $ pyxtrlock

To enable autolocking after a specified amount of idle time you can
use the ``xautolock`` tool. Just add something like

    xautolock -locker pyxtrlock -time 5

to your X autostart file, to lock the screen with ``pyxtrlock`` after
5 minutes idle time. ``xautolock`` has many other useful features, see
its documentation. There does not seem to be a official ``xautolock``
homepage that we can link for documentation, but most distris provide
a ``xautolock`` package with a man page.

Bugs
----
Additional input devices other than the keyboard and mouse are not disabled.

Please report any new bugs you may find to our [Github issue tracker](https://github.com/leonnnn/pyxtrlock/issues).

Requirements
------------
* [python3-pam](https://github.com/leonnnn/python3-pam)
* Python ≥ 3.0
* libxcb
* libX11 ≥ 1.4, or libX11 ≥ 1.2 compiled with XCB backend

These requirements are met on
* Debian wheezy and sid, and probably on Debian squeeze (untested; please report your experience)
* Ubuntu ≥ 11.10, and probably 10.04 (untested; please report your experience)
* Fedora ≥ 17, probably 16

Authors
-------
* Leon Weber <leon@leonweber.de>
* Sebastian Riese <sebastian.riese.mail@web.de>

pyxtrlock has been inspired by
[Ian Jacksons](http://www.chiark.greenend.org.uk/~ijackson/)'s brilliant
``xtrlock`` program and uses many ideas and techniques from the xtrlock
source code. Also, the lock icon has been copied from xtrlock.

License
-------
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
