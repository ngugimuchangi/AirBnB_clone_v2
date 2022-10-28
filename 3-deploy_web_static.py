#!/usr/bin/python3
""" Full deployment module
"""
from fabric.api import task


def deploy():
    """ Function to pack and deploy
    """
    # import required functions
    do_pack = __import__('1-pack_web_static').do_pack
    do_depoly = __import__('2-do_deploy_web_static').do_deploy

    tar = do_pack()
    if tar is None:
        return False
    status = do_deploy(tar)
    return status
