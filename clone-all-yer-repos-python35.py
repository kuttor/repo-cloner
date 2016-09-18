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
        total_repos = github_to_json(account=args['<username>'])['public_repos']
        clone_repos(total_repos=total_repos, account=args['<username>'])

    except DocoptExit as e:
        print(e.message)


def github_to_json(account):
    url = 'https://api.github.com/users/{}/repos'.format(account)
    json = (get(url).json())
    return(json)


def clone_repos(total_repos, account):
    url = 'https://api.github.com/users/{}/repos?'.format(account)
    num = 0
    for num in url:
        if num <= total_repos:
            url = url + 'page={}per_page=1'.format(num)
            print(url['0']['git_url'])


def total_repos(total_repos):
    return 'place holder'


if __name__ == '__main__':
    exit(main())
