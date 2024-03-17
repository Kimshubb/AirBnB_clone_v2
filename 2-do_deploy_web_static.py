#!/usr/bin/python 3
"""Fabric script to deploy archive to my webservers"""
from datetime import datetime
from fabric.api import *
import os

env.hosts = ["ubuntu@54.175.1.126", "ubuntu@3.83.253.4"]

def do_deploy(archive_path):
    if not os.path.exists(archive_path):
        print("Error: Archive {} does not exist".format(archive_path))
        return False
    try:
        put(archive_path, '/tmp/')
        archive_name = os.path.basename(archive_path)

