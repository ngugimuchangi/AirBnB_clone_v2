#!/urs/bin/python3
""" Deployment module using fabric
"""
from fabric.api import cd, env, run, put
from os import path

env.hosts = ["44.200.168.223", "18.204.14.103"]
env.user = 'user'


def do_deploy(archive_path):
    """ Function to distribute archive files to webservers
    """

    file_name = archive_path.split('/')[-1]
    extract = file_name.split('.')[0]
    destination = '/data/web_static/releases/'
    link = "/data/web_static/current"

    if not path.isfile(archive_path):
        return False

    if put(archive_path, "/tmp/").failed:
        return False

    with cd(destination):
        if run(f'tar -xcvf /tmp/{file_name}').failed:
            return False

    if run(f'rm -rf /tmp/{file_name}').failed:
        return False

    if run(f'ln -sf {destination}{extract} {link}').failed:
        return False

    return True
