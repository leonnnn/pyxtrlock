from distutils.core import setup

authors = (
    'Leon Weber <leon@leonweber.de>, '
    'Sebastian Riese <sebastian.riese.mail@web.de>'
)

desc = (
    'The X transparent screen lock rewritten in Python, using XCB and PAM.'
)

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
      version='0.1beta',
      author=authors,
      author_email='leon@leonweber.de',
      requires=['pam'],
      package_dir={'pyxtrlock': 'lib'},
      packages=['pyxtrlock'],
      scripts=['pyxtrlock'],
      license='GPLv3+',
      url='https://zombofant.net/hacking/pyxtrlock',
      description=desc,
      classifiers=classifiers
)
