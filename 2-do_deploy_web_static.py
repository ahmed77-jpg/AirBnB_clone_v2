#!/usr/bin/python3
"""
Write a Fabric script that generates a .tgz archive from the contents
"""
from fabric.operations import local, run, put
from datetime import datetime
import os
from fabric.api import *
import re


def do_pack():
    """
    function creates a .tgz
    """
    local("mkdir -p versions")
    rtat = local("tar -cvzf versions/web_static_{}.tgz web_static"
                 .format(datetime.strftime(datetime.now(), "%Y%m%d%H%M%S")),
                 capture=True)
    if rtat.failed:
        return None
    return rtat

def do_deploy(archive_path):
    """ Script that does a lot of magic =) like penn and teller """
    if (archive_path is False or archive_path is None):
        return False
    try:
        # this will be the web_static_NUMBERSSSS.tgz
        last = archive_path.split("/")[-1]
        # and this will be the stuff without the dot extension
        foldName = "/data/web_static/releases/" + last.split(".")[0]
        # overwrites pre-existing remote files without request confirmation
        put(archive_path, "/tmp/")
        # make the directory on the server
        run("sudo mkdir -p {}".format(foldName))
        # unzips the archive to the folder on the webserver
        run("sudo tar -xzf /tmp/{} -C {}".format(last, foldName))
        # deletes archive from web server
        run("sudo rm /tmp/{}".format(last))
        # moves the archive out of web static to be removed
        run("sudo mv {}/web_static/* {}/".format(foldName, foldName))
        # removes the archive
        run("sudo rm -rf {}/web_static".format(foldName))
        # deletes the symbolic link to the web server
        run("sudo rm -rf /data/web_static/current")
        # create a new sym link that links to new version of code
        run("sudo ln -s {} /data/web_static/current".format(foldName))
    except:
        return False
    return True
