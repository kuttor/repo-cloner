#!/usr/bin/env python

"""
repo-cloner - Clones all public github repos in an account

Usage:
  repo-cloner <username>
  repo-cloner [ -h | --help ]
  repo-cloner [ -v | --version ]

Options:
  -v --version            Show version
  -h --help               Show this screen
"""

import os
from requests import get
from docopt import DocoptExit, docopt

__author__ = 'Andrew Kuttor'
__maintainer__ = 'Andrew Kuttor'
__email__ = 'andrew.kuttor@gmail.com'
__version__ = '1.2.1'


# -----------------------------------------------------------------------------
# Main
# -----------------------------------------------------------------------------

def main():
    '''performs execution and logic for the arg parser'''
    try:
        args = docopt(__doc__, version='Clone All Yer Repos - v1.0')
        username = args['<username>']
        repos = total_repos(account=username)
        clone_repos(total=repos, account=username)
    except DocoptExit as e:
        print(e.message)


def total_repos(account):
    '''stores and returns total repos'''
    url = 'https://api.github.com/users/{}'.format(account)
    json = (get(url).json())
    return(json['public_repos'])


def clone_repos(total, account):
    '''concatonates url and the destination dir-path'''
    num = 0
    url = '''https://api.github.com/users/{0}/repos?\
    'page={1}per_page=1'''.format(account, num)
    json = (get(url).json())

    print("\nTotal Git repos to be cloned: {}".format(total)) + "\n"

    while num < total:
        address = json[num]['git_url']

        print("Cloning: {}".format(json[num]['name']))
        os.system("git clone {} {}/{}\
                  ".format(address, account, json[num]['name']))
        num += 1


if __name__ == '__main__':
    exit(main())
