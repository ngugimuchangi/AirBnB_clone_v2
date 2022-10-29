#!/usr/bin/python3
# Fabfile script for generating compressed tar file

from datetime import datetime
from fabric.api import local, lcd, settings


def do_pack():
    '''creates compressed archive file of web_static folder
        Args: none
        Return: name of tgz file created
    '''
    file_name = f"web_static_{datetime.now().strftime('%Y%m%d%H%M%S')}.tgz"

    with settings(warn_only=True):
        if local('test -d versions').failed:
            local('mkdir versions')

    with lcd('versions'):
        execute = local(f'tar -zcvf {file_name} ../web_static')

    if execute.succeeded:
        return f"versions/{file_name}"
