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
        # check for the current file
        if number == 1 or number == 0:
            file_1 = local('ls -1t | head -n 1', capture=True)

            # rm !(file_name) shorter method but doesn't work
            # when bash reads cmds from string as fabric uses it
            local("{}{}{}{}".format("for f in $(ls); do ",
                  "if [ $f != ", file_1, " ]; then rm -v $f; fi done"))

        # check for two most current files
        if number == 2:
            file_1 = local('ls -1t | head -n 1', capture=True)
            file_2 = local('ls -1t | tail -n +2 | head -n 1',
                           capture=True)
            run("{}{}{}{}{}{}".format("for f in $(ls -1t); do ",
                "if [ $f != ", file_1, " ] && [ $f != ", file_2,
                                      " ]; then rm -vrf $f; fi done"))

    with cd('/data/web_static/releases'):
        if number == 1 or number == 0:
            file_1 = run('ls -1t | head -n 1')

            run("{}{}{}{}".format("for f in $(ls); do ",
                "if [ $f != ", file_1, " ]; then rm -rf -v $f; fi done"))

        if number == 2:
            file_1 = run('ls -1t | head -n 1')
            file_2 = run('ls -1t | tail -n +2 | head -n 1')
            run("{}{}{}{}{}{}".format("for f in $(ls -1t); do ",
                "if [ $f != ", file_1, " ] && [ $f != ", file_2,
                                      " ]; then rm -rf -v $f; fi done"))
