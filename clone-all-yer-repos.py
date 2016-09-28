#!/usr/bin/env python
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

import os
from requests import get
from docopt import DocoptExit, docopt


# about
__author__ = 'Andrew Kuttor'
__maintainer__ = 'Andrew Kuttor'
__email__ = 'akuttor@gmail.com'
__version__ = '1.0.0'


def main():
    try:
        args = docopt(__doc__, version='Clone All Yer Repos - v1.0')
        username = args['<username>']
        repos = total_repos(account=username)
        clone_repos(total=repos, account=username)
    except DocoptExit as e:
        print(e.message)


# returns total repos as int
def total_repos(account):
    url = 'https://api.github.com/users/{}'.format(account)
    json = (get(url).json())
    return(json['public_repos'])


def clone_repos(total, account):
    num = 0
    url = '''https://api.github.com/users/{0}/repos?\
    'page={1}per_page=1'''.format(account, num)
    json = (get(url).json())

    print("\nTotal Git repos to be cloned: {}".format(total)) + "\n"

    while num < total:
        print("Cloning: {}".format(json[num]['name']))
        os.system("git clone {}".format(json[num]['git_url']))
        num += 1


if __name__ == '__main__':
    exit(main())
