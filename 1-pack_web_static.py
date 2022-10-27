#!/usr/bin/pyton3
""" Fabfile module for webstatic
"""
from fabric.api import local, lcd
from datetime import datetime


def do_pack():
    """ Creates compressed archive file
        of web_static folder
    """
    local('mkdir versions')  # create directory

    # essential variables
    date = datetime.now()
    year = date.year
    month = date.month
    day = date.day
    hour = date.hour
    minute = date.minute
    second = date.second
    file = f"web_static{year}{month}{day}{hour}{minute}{second}"

    # create compressed tar file in the versions directory
    with lcd('versions'):
        local(f'tar -zcf {file}.tzg ../web_static')
