#!/usr/bin/python3
import os
from fabric.api import local
from datetime import datetime


def do_pack():
    """Generate a tgz archive from web static folder contentds"""
    try:
        local("mkdir -p versions")
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        archive = "versions/web_static_{}.tgz".format(timestamp)
        print("Packing web static to {}".format(archive))
        local("tar -cvzf {} web_static".format(archive))
        size = os.stat(archive).st_size
        print("Web static packed:{} -> {}Bytes".format(archive, size))
        return "versions/{}".format(archive)
    except Exception as e:
        print("Error:", e)
        return None
if __name__ == "__main__":
    do_pack()
