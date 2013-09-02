make_lock.py
============

PLEASE NOTE: make_lock.py requires python2 as the PIL is not packaged
for python3 on most distris.

Therefore another tool – repickle.py – must be used to postprocess the
generated files.

usage: make_lock.py [-h] [--x-hit X_HIT] [--y-hit Y_HIT] [--fg-color FG_COLOR]
                    [--bg-color BG_COLOR] [--output OUTPUT] [--debug]
                    bg_bitmap [fg_bitmap]

positional arguments:
  bg_bitmap             The single image or the 1-bit mask
  fg_bitmap             If given, the 1-bit foreground pixels

optional arguments:
  -h, --help            show this help message and exit
  --x-hit X_HIT, -x X_HIT
                        x-coordinate of the cursor hotspot
  --y-hit Y_HIT, -y Y_HIT
                        x-coordinate of the cursor hotspot
  --fg-color FG_COLOR, -f FG_COLOR
                        The foreground colour (necessary only if the
                        colourscannot be guessed from the image file).
                        Accepted formats:colour name, rgb(255, 50, 0),
                        rgb(1.0, 0.2, 0.0), #ff7700, #f70
  --bg-color BG_COLOR, -b BG_COLOR
                        The background colour.
  --output OUTPUT, -o OUTPUT
                        The output file, by default stdout
  --debug               Check for consistency and printthe bitmaps to the
                        stdout


This tools allows you to easily make cursor files for pyxtrlock from
various image file types (basically: anything with 1-3 discrete colors,
various forms of transparency, that can be opened by python imaging).

The recommended file type is PNG.

There are several modes of operation which are guessed from the
supplied file:

*a singe colour image with 2 colours and transparency is compiled to
 the appropriate cursor (transparency may either be an alpha threshold
 or single colour transparency)
*a single image with 1 colour will have its border stroked the colours
 should be given on the commandline
*two (one bit!) bitmaps may be given, on is the mask and the other the
 foreground of the cursor. The colours should be given on the commandline.
*colours may be given on the commandline or the default colours black
 and white apply, colours given on the commandline override colours from
 the file, but note that the assignment will be random in that case

Additionally the cursor hotspot can be given otherwhise it is the
center of the image (this is more or less irrelevant, as the all
cursor events are blocked by pyxtrlock).

Typical usage
-------------

To create a cursor from a PNG with two colors (foreground and
background) and transparenct pixels and then install it for your user
do the following:

    $ ./make_lock.py lock.png -o lock.pickle
    $ ./repickle lock.pickle
    $ mkdir ~/.config/pyxtrlock/
    $ cp lock.pickle ~/.config/pyxtrlock

Requirements
------------
*Python 2.7
*python-imaging (PIL)

Authors
-------
Sebastian Riese <s.riese@sotecware.net>

Liense
------

Copyright 2013 Sebastian Riese

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
