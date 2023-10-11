#!/usr/bin/python3
"""Script that generates a .tgz archive from the contents of the web_static."""

from fabric.api import local, env, put, run
from datetime import datetime
import os.path as path

env.hosts = ["100.26.212.225", "100.26.233.38"]


def do_pack():
    """ Compress before sending """

    try:
        local("mkdir -p versions")

        now = datetime.now()
        time = now.strftime("%Y%m%d%H%M%S")

        archive_name = f"web_static_{time}.tgz"
        local(f"tar -cvzf versions/{archive_name} web_static")

        return (f"versions/{archive_name}")

    except Exception as error:
        return None


def do_deploy(archive_path):
    """Distributes an archive to your web servers."""

    if not path.exists(archive_path):
        return False

    try:
        file = archive_path.split("/")[-1]
        filename = file.split(".")[0]
        releases_path = f"/data/web_static/releases/{filename}/"

        put(archive_path, "/tmp/")

        run(f"mkdir -p {releases_path}")
        run(f"tar -xzf /tmp/{file} -C {releases_path}")

        run(f"rm /tmp/{file}")

        run(f"mv {releases_path}web_static/* {releases_path}")
        run(f"rm -rf {releases_path}/web_static")

        run("rm -rf /data/web_static/current")
        run(f"ln -s {releases_path} /data/web_static/current")

        return True

    except Exception as error:
        return False


def deploy():
    """makes the whole deploy at once"""

    path = do_pack()
    if not path:
        return False

    return do_deploy(path)
