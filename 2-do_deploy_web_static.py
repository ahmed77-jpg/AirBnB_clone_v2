#!/usr/bin/python3
"""
Write a Fabric script that generates a .tgz archive from the contents
"""
from fabric.operations import local, run, put
from datetime import datetime as d
from fabric.api import *

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
    """Function to distribute an archive to a server"""
    destination = "/tmp/" + archive_path.split("/")[-1]
    result = put(archive_path, "/tmp/")
    if result.failed:
        return False
    filename = archive_path.split("/")[-1]
    f = filename.split(".")[0]
    directory = "/data/web_static/releases/" + f
    run_res = run("mkdir -p \"%s\"" % directory)
    if run_res.failed:
        return False
    run_res = run("tar -xzf %s -C %s" % (destination, directory))
    if run_res.failed:
        return False
    run_res = run("rm %s" % destination)
    if run_res:
        return False
    web = directory + "/web_static/*"
    run_res = run("mv %s %s" % (web, directory))
    if run_res.failed:
        return False
    web = web[0:-2]
    run_res = run("rm -rf %s" % web)
    if run_res.failed:
        return False
    run_res = run("rm -rf /data/web_static/current")
    if run_res.failed:
        return False
    run_res = run("ln -s %s /data/web_static/current" % directory)
    if run_res.failed:
        return False
    return True
