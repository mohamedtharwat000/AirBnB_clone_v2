#!/usr/bin/python3
""" doc """
from fabric.api import local
from datetime import datetime


def do_pack():
    """ Compress before sending """

    try:
        local("mkdir -p versions")

        now = datetime.now()
        time = now.strftime("%Y%m%d%H%M%S")

        archive_name = f"web_static_{time}.tgz"
        local(f"tar -cvzf versions/{archive_name} web_static")

        return (f"versions/{archive_name}")

    except Exception as e:
        return None
