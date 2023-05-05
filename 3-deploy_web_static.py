#!/usr/bin/python3
'''
    scripts that fully deploys to a web server.
'''
import os
from datetime import datetime
from fabric.api import local, env, run, put


env.user = "ubuntu"
env.key_filename = "~/.ssh/school"
env.hosts = ['54.157.152.234', '100.25.188.157']


def do_pack():
    '''creates a tar file of the web_static folder'''

    if local("mkdir -p versions/").failed is True:
        return None

    date = datetime.utcnow()
    str_date = date.strftime("%Y%m%d%H%M%S")
    tar_file = "versions/web_static_{}.tgz".format(str_date)

    if local("tar -c -v -z -f {} web_static/".format(tar_file)).failed is True:
        return None
    else:
        return tar_file


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


def deploy():
    """
    fully deploys the archive to the servers.
    pack data into an archive, uploads it to the servers,
    and configure the server to use the uncompressed data.
    """
    archive_path = do_pack()
    if not os.path.exists(archive_path):
        return False
    return do_deploy(archive_path)
