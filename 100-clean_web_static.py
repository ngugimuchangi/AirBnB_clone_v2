#!/usr/bin/python3
""" Fabric script to clean outdated archive files
"""
from fabric.api import cd, lcd, local, run, env, with_settings

env.hosts = ["44.200.168.223", "18.204.14.103"]


@with_settings(warn_only=True)
def do_clean(number=0):
    """Function to remove outdate tgz files"""
    number = int(number)

    with lcd('versions'):
        # check for number of files
        num_files = int(local('ls -1 | wc -l', capture=True))

        # check if number is greater than files in directory
        if number >= num_files:
            return

        # delete files
        if number == 1 or number == 0:
            limit = num_files - 1
        local("{}{}{}".format("for((i=0; i < ", limit,
              "; i++)); do rm -rf -v $(ls -r1t | head -n 1); done"),
              shell='/bin/bash')

    with cd('/data/web_static/releases'):
        num_files = int(run('ls -1 | wc -l'))

        # check if number is greater than files in directory
        if number >= num_files:
            return

        # delete files
        if number == 1 or number == 0:
            limit = num_files - 1
        run("{}{}{}".format("for((i=0; i < ", limit,
            "; i++)); do rm -rf -v $(ls -r1t | head -n 1); done"))
