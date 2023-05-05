#!/usr/bin/python3
"""
deploy an archive file to a web server.
"""
import os
from fabric.api import put
from fabric.api import env
from fabric.api import run


env.hosts = ['54.157.152.234', '100.25.188.157']


def do_deploy(archive_path):
    """
    uploads the archive path to a web
    server.
    """
    if os.path.exists(archive_path) is False:
        return False
    file = archive_path.split('/')[-1]
    name = file.split('.')[0]
    directory = "/data/web_static/releases/{}".format(name)

    try:
        put(archive_path, "/tmp/")
        run("mkdir -p {}".format(directory))
        run("tar -xzf /tmp/{} -C {}/".format(file, directory))
        run("rm /tmp/{}".format(file))
        run("mv {}/web_static/* {}/".format(directory, directory))
        run("rm -rf {}/web_static".format(directory))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(directory))
        return True
    except ValueError:
        return False
