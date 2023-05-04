#!/usr/bin/python3
'''
contains a function to create tape archive (tar)
'''
from datetime import datetime
import fabric.api as fapi


def do_pack():
    '''creates a tar file of the web_static folder'''

    if fapi.local("mkdir -p versions/").failed is True:
        return None

    date = datetime.utcnow()
    tar_file = "versions/web_static_{}{}{}{}{}.tgz".format(
            date.year, date.month, date.day,
            date.hour, date.minute, date.second
            )

    if fapi.local(f"tar -c -v -f {tar_file} web_static/").failed is True:
        return None
    else:
        return tar_file
