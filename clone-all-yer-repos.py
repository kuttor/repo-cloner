#!/usr/bin/usr python
"""
clone-all-yer-repos - Clones all repos by username

Usage:
  clone-all-yer-repos -u <username>
  clone-all-yer-repos [ -h | --help | --version ]

Options:
  --version               Show version.
  -h --help               Show this screen.
  -u --username USERNAME  Specify github username to create
"""

from urllib2 import urlopen
from docopt import DocoptExit, docopt

# about
__author__ = "Andrew Kuttor "
__maintainer__ = "Andrew Kuttor"
__email__ = "akuttor@gmail.com"
__version__ = "1.0.0"


def main():
    try:
        args = docopt(__doc__, version='Clone All Yer Repos - v1.0')
        get_total_pages(**args)
    except DocoptExit as e:
        print e.message

# get total repos and divivde by 100
# use urllib2 to snag attribute - "public_repos": X
def get_total_pages(user):
    url = urlopen('https://api.github.com/users/{0}').format(user)
    print url.read()

if __name__ == "__main__":
    exit(main())
