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

Description
-----------
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

Installation and Usage
----------------------
Install [python3-simplepam](https://github.com/leonnnn/python3-simplepam) for
dependencies:

    $ git clone git://github.com/leonnnn/python3-simplepam.git
    $ cd python3-simplepam
    $ sudo python3 setup.py install

Install [pyxdg](http://freedesktop.org/Software/pyxdg) for
dependencies:

    $ git clone git://anongit.freedesktop.org/xdg/pyxdg
    $ cd pyxdg
    $ sudo python3 setup.py install

Clone and install pyxtrlock:

    $ git clone git://github.com/leonnnn/pyxtrlock.git
    $ cd pyxtrlock
    $ sudo python3 setup.py install

Once this is done, you should be able to simply lock your display by running

    $ pyxtrlock

If you would like to automatically lock your screen after some idle time,
we recommend the ``xautolock`` tool. Just add something like

    xautolock -locker pyxtrlock -time 5

to your X autostart file to lock the screen with ``pyxtrlock`` after 5
minutes idle time. ``xautolock`` has many other useful features, see
its documentation. Most distributions provide an ``xautolock`` package
with a man page. An alternative to ``xautolock`` is the use of
[autolockd](https://github.com/zombofant/autolockd) which also
monitors for lid close and suspend events.

Staying up-to-date
------------------
As pyxtrlock is a security tool, it is important to stay up-to-date with
security updates. We take security seriously and try to handle any
vulnerabilities quickly. However, our efforts are useless if the users
aren’t notified that updates are available, so if you use pyxtrlock, we
urge you to subscribe to
[the pyxtrlock mailing list](http://lists.zombofant.net/mailman/listinfo/pyxtrlock).
This list is likely very low traffic and will ensure you get
notifications of security updates in time.

We also appreciate any feedback you have regarding pyxtrlock on this
mailing list.

Bugs & Limitations
------------------
Additional input devices other than the keyboard and mouse are not disabled.

Although this is not a bug, please note that pyxtrlock does not
prevent a user from switching to a virtual terminal, so be advised to
always log out from your terminals.

The lenght of the password is limited to 100 KiB to prevent memory
exhaustion attacks. This limit can only be adapted in the source code.

Please report any new bugs you may find to our
[Github issue tracker](https://github.com/leonnnn/pyxtrlock/issues).

Configuration
-------------
The padlock icon can be changed. It is stored as a
[pickle](http://docs.python.org/3/library/pickle.html) of a
dictionary, and the ``tools`` directory contains a tool for generating
cursors from image files.

The default cursor file is placed at
``PREFIX/share/pyxtrlock/lock.pickle`` while the cursor file at
``~/.config/pyxtrlock/lock.pickle`` takes precedence if present.

*PLEASE NOTE:* The ``pickle`` file format is not designed to be
resistant against maliciously crafted files. Therfore do not open
``pickle`` files from untrusted sources as they may compromise your
system. The default padlock file is created on install (by
``make_default_lock.py``).

Requirements
------------
* [python3-simplepam](https://github.com/leonnnn/python3-simplepam)
* [pyxdg](http://freedesktop.org/Software/pyxdg)
* Python ≥ 3.0
* libxcb
* libxcb-image
* libX11 ≥ 1.4, or libX11 ≥ 1.2 compiled with XCB backend

These requirements are met at least on
* Debian wheezy and sid, and probably on Debian squeeze (untested; please report your experience)
* Ubuntu ≥ 11.10, and probably 10.04 (untested; please report your experience)
* Fedora ≥ 16

Authors
-------
* Leon Weber <leon@leonweber.de>
* Sebastian Riese <s.riese@zombofant.net>

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
