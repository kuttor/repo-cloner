#!/usr/bin/usr python
"""
clone-all-yer-repos - Clones all public github repos in an account

Usage:
  clone-all-yer-repos <username>
  clone-all-yer-repos [ -h | --help ]
  clone-all-yer-repos [ -v | --version ]

Options:
  -v --version            Show version
  -h --help               Show this screen
"""

from requests import get
from pprint import pprint
from docopt import DocoptExit, docopt


# about
__author__ = "Andrew Kuttor "
__maintainer__ = "Andrew Kuttor"
__email__ = "akuttor@gmail.com"
__version__ = "1.0.0"


def main():
    try:
        args = docopt(__doc__, version='Clone All Yer Repos - v1.0')
        print(args)
        url_to_json(args['<username>'])
    except DocoptExit as e:
        print(e.message)


def url_to_json(user):
    url = 'https://api.github.com/users/{0}'.format(user)
    pprint(get(url).json()) # test output
    return(get(url).json())


# get total repos and divivde by 100
# use requests to snag attribute - "public_repos": X
def get_total_number_pages_of_url():
    return "place holder"


if __name__ == "__main__":
    exit(main())
