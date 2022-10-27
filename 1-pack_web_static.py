#!/usr/bin/python3
""" Fabfile module for webstatic
"""
from datetime import datetime
from fabric.api import local, lcd
from os import path


def do_pack():
    """ Creates compressed archive file
        of web_static folder
    """

    # essential variables for file name
    date = datetime.now()
    year = date.year
    month = date.month
    day = date.day
    hour = date.hour
    minute = date.minute
    second = date.second
    file_name = f"web_static{year}{month}{day}{hour}{minute}{second}"

    # create directory if it doesn't exist
    if not path.exists('versions'):
        local('mkdir versions')

    # create compressed tar file in the versions directory
    with lcd('versions'):
        execute = local(f'tar -zcvf {file_name}.tzg ../web_static')

    # check cmd success and return path
    if execute.succeeded:
        return f"versions/{file_name}"
