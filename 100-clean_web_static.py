#!/usr/bin/python3
""" Fabric script to clean outdated archive files
"""
from fabric.api import lcd, local, settings, env
from os import remove, listdir

env.shell = "/bin/bash -l -c"


def do_clean(number=0):
    """ Function to remove outdate tgz files
    """
    print(number)
    with lcd('versions'):
        with settings(warn_only=True):
            shell = '/usr/bin/bash'
            curr_files = []

            # check for the current file
            if number == '1' or number == '0':
                curr_files.append(local('ls -1t | head -n 1', capture=True))

            # check for two most current files
            if number == '2':
                curr_files.append(local('ls -1t | head -n 1', capture=True))
                curr_files.append(local('ls -1t | tail -n +2 | head -n 1',
                                  capture=True))

            # remove files one by one
            all_files = listdir('versions/')
            for f in all_files:
                if f not in curr_files:
                    remove(f"versions/{f}")
