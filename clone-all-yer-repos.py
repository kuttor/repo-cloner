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

import git
from requests import get
from pprint import pprint
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
        clone_repos(total_repos=repos, account=username)

    except DocoptExit as e:
        print(e.message)


def total_repos(account):
    url = 'https://api.github.com/users/{}'.format(account)
    json = (get(url).json())
    return(json)


def clone_repos(total_repos, account):
    url = 'https://api.github.com/users/{}/repos?'.format(account)
    num = 0
    for repo in url:
        if num <= total_repos:
            num += 1
            print(url + 'page={}per_page=1'.format(num))


if __name__ == '__main__':
    exit(main())
