#!/usr/bin/python3
"""
Write a Fabric script that generates a .tgz archive from the contents
"""
from fabric.operations import local
from datetime import datetime


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
    if not os.path.exists(archive_path) and not os.path.isfile(archive_path):
        return False
    put(archive_path, '/tmp/')
    m = archive_path.replace('.tgz', '')
    m = m.replace('versions/', '')
    run('mkdir -p /data/web_static/releases/{}/'.format(m))
    run('tar -xzf /tmp/{}.tgz -C /data/web_static/releases/{}/'
        .format(m, m))
    run('rm /tmp/{}.tgz'.format(m))
    run('mv /data/web_static/releases/{}/web_static/* '.format(m) +
        '/data/web_static/releases/{}/'.format(m))
    run('rm -rf /data/web_static/releases/{}/web_static'.format(m))
    run('rm -rf /data/web_static/current')
    run('ln -s /data/web_static/releases/{}/ /data/web_static/current'
        .format(m))
    print('New version successfuly deployed')
    return True
