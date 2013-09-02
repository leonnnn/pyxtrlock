from distutils.core import setup
from distutils.command.install import install

import os
import stat
import subprocess

class my_install(install):
    def run(self):
        stat_make_lock = os.stat("make_default_lock.py")
        try:
            stat_lock = os.stat("lock.pickle")
        except OSError:
            stat_lock = None
        if stat_lock is None \
                or stat_lock[stat.ST_MTIME] < stat_make_lock[stat.ST_MTIME]:
            subprocess.call(["python3", "./make_default_lock.py"])
        super().run()

authors = (
    'Leon Weber <leon@leonweber.de>, '
    'Sebastian Riese <s.riese@zombofant.net>'
)

desc = (
    'The X transparent screen lock rewritten in Python, using XCB and PAM.'
)

long_desc = """
pyxtrlock -- The leightweight screen locker rewritten in Python
---------------------------------------------------------------

pyxtrlock is a very limited transparent X screen locker inspired by Ian
Jackson’s great xtrlock program. pyxtrlock uses modern libraries, most
importantly the obsolete direct passwd/shadow authentication has been replaced
by today’s PAM authentication mechanism, hence it also works on Fedora. Also,
it’s mostly written using XCB instead of Xlib.

"""


classifiers = [
    'Development Status :: 3',
    'Environment :: X11 Applications',
    'Intended Audience :: End Users/Desktop',
    'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
    'Operating System :: POSIX :: Linux',
    'Programming Language :: Python :: 3',
    'Topic :: Desktop Environment :: Screen Savers'
]

setup(name='pyxtrlock',
      version='0.1',
      author=authors,
      author_email='leon@leonweber.de',
      requires=['simplepam'],
      package_dir={'pyxtrlock': 'lib'},
      data_files=[('share/pyxtrlock/', ['lock.pickle'])],
      packages=['pyxtrlock'],
      scripts=['pyxtrlock'],
      cmdclass={'install': my_install},
      license='GPLv3+',
      url='https://zombofant.net/hacking/pyxtrlock',
      description=desc,
      long_description=long_desc,
      classifiers=classifiers
)
