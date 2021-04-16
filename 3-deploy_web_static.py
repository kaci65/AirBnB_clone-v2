#!/usr/bin/python3
"""
Fabric script (based on the file 2-do_deploy_web_static.py) that creates
and distributes an archive to web servers, using the function deploy
"""
from datetime import datetime
from fabric.api import *
from os import path
env.hosts = ['35.231.35.245', '34.74.188.166']


def do_pack():
    """compress files"""
    time = datetime.now()
    timeDate = time.strftime("%Y%m%d%H%M%S")
    try:
        local("mkdir -p versions")
        local("tar -czvf versions/web_static_{}.tgz web_static/"
              .format(timeDate))
        return("versions/web_static_{}.tgz".format(timeDate))
    except:
        return None


def do_deploy(archive_path):
    """distributes an archive to your web servers"""
    if exists(archive_path) is False:
        return False

    filename = archive_path.split("/")[-1]
    file_aux = filename.split(".")[0]
    filepath = "/data/web_static/releases/"
    try:
        put(archive_path, "/tmp/")
        run("mkdir -p {}{}/".format(filepath, file_aux))
        run("tar -xzf /tmp/{} -C {}{}/".format(filename, filepath, file_aux))
        run("rm /tmp/{}".format(filename))
        run("mv {0}{1}/web_static/* {0}{1}/".format(filepath, file_aux))
        run("rm -rf {}{}/web_static".format(filepath, file_aux))
        run("rm -rf /data/web_static/current")
        run("ln -s {}{}/ /data/web_static/current".format(filepath, file_aux))
        return True
    except:
        return False


def deploy():
    """creates and distributes an archive to web servers"""
    archive_path = do_pack()
    if archive_path is None:
        return False
