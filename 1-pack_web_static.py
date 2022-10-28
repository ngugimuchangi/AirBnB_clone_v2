#!/usr/bin/python3
""" Fabfile module for webstatic
"""
from datetime import datetime
from fabric.api import local, lcd, settings, task


@task
def do_pack():
    """ Creates compressed archive file of web_static folder
    """

    # essential variables for file name
    file_name = f"web_static_{datetime.now().strftime('%Y%m%d%H%M%S')}"

    # create directory if it doesn't exist
    with settings(warn_only=True):
        if local('test -d versions').failed:
            local('mkdir versions')

    # create compressed tar file in the versions directory
    with lcd('versions'):
        execute = local(f'tar -zcvf {file_name}.tgz ../web_static')

    # check cmd success and return path
    if execute.succeeded:
        return f"versions/{file_name}"
