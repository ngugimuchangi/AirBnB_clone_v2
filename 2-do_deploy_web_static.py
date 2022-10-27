#!/urs/bin/python3
"""Deployment module using fabric
"""
from fabric.api import cd, env, run, put
from os import path

env.hosts = ["44.200.168.223", "18.204.14.103"]


def do_deploy(archive_path):
    """ Function to distribute archive files to webservers
    """
    # essential file names
    file_name = archive_path.split('/')[-1]
    extract = file_name.split('.')[0]
    destination = '/data/web_static/releases/'
    link = "/data/web_static/current"

    # check if archive file exists
    if not path.isfile(archive_path):
        return False

    # transfer file to remote
    if put(archive_path, "/tmp/").failed:
        return False

    # change directory and extract file
    with cd(destination):
        if run(f'tar -xcvf /tmp/{file_name}').failed:
            return False

    # rm  archive file
    if run(f'rm -rf /tmp/{file_name}').failed:
        return False

    # create new symbolic link
    if run(f'ln -sfn {destination}{extract} {link}').failed:
        return False

    return True
