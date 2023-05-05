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
    str_date = date.strftime("%Y%m%d%H%M%S")
    tar_file = "versions/web_static_{}.tgz".format(str_date)

    if local("tar -c -v -z -f {} web_static/".format(tar_file)).failed is True:
        return None
    else:
        return tar_file
