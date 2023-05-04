#!/usr/bin/python3
'''contains a function to create tape archive (tar).
'''

from datetime import datetime
from fabric.api import local


def do_pack():
    '''creates a tar file of the web_static folder'''

    if local("mkdir -p versions/").failed is True:
        return None

    date = datetime.utcnow()
    tar_file = "versions/web_static_{}{}{}{}{}{}.tgz".format(
            date.year, date.month,
            date.day, date.hour,
            date.minute, date.second)

    if local("tar -c -v -f {} web_static/".format(tar_file)).failed is True:
        return None
    else:
        return tar_file
