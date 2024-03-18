#!/usr/bin/python3
"""Fabric script to deploy archive to my webservers"""
from datetime import datetime
from fabric.api import *
import os

env.hosts = ["ubuntu@54.175.1.126", "ubuntu@3.83.253.4"]
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

def do_deploy(archive_path):
    """Distribute archive to web servers and deploy"""
    if not os.path.exists(archive_path):
        print("Error: Archive {} does not exist".format(archive_path))
        return False
    try:
        put(archive_path, '/tmp/')
        archive_name = os.path.basename(archive_path)
        release_folder = '/data/web_static/releases/' + os.path.splitext(archive_name)[0]
        run('sudo mkdir -p {}'.format(release_folder))
        run('sudo chmod 755 {}'.format(release_folder))
        run('tar -xzf /tmp/{} -C {}'.format(archive_name, release_folder))
        run('rm /tmp/{}'.format(archive_name))
        run('rm -rf /data/web_static/current')
        run('sudo ln -s {} /data/web_static/current'.format(release_folder))
        print("New version deployed!")
        return True
    except Exception as e:
        print("{} Error during deployment!".format(e))
if __name__ == "__main__":
    archive_path = do_pack()
    do_deploy(archive_path)
    if archive_path:
        do_deploy(archive_path)
    else:
        print("Archive creation failed. Deployment aborted!")
