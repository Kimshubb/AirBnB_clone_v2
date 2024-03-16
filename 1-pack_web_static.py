#!/usr/bin/python3
from fabric.api import local
from datetime import datetime

def do_pack():
    """Generate a tgz archive from web static folder contentds"""
    try:
        local("mkdir -p versions")
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        archive_name = "web_static.tgz{}".format(timestamp)
        local("tar -cvzf versions/{} web_static".format(archive_name))
        return "versions/{}".format(archive_name)
    except Exception as e:
        print("Error:", e)
        return None
if __name__ == "__main__":
    do_pack()
