#!/usr/bin/python3
"""doc"""
from datetime import datetime
from fabric.api import run, put, env, local
from os import path


env.hosts = ["100.26.53.140", "100.26.244.194"]
env.user = 'ubuntu'
env.key_filename = ['~/.ssh/school']

def do_deploy(archive_path):
    """ Deploy archive to the web server """

    if not path.exists(archive_path):
        return False

    try:
        put(archive_path, '/tmp/')

        archive_filename = archive_path.split('/')[-1]
        release_folder = f'/data/web_static/releases/{archive_filename.split(".")[0]}'

        run(f'mkdir -p {release_folder}')
        run(f'tar -xzf /tmp/{archive_filename} -C {release_folder}')

        run(f'rm /tmp/{archive_filename}')

        run(f'mv -f {release_folder}/web_static/* {release_folder}')
        run(f'rm -rf {release_folder}/web_static/')
        run('rm -rf /data/web_static/current')

        run(f'ln -s {release_folder} /data/web_static/current')

        return True

    except Exception as e:
        return False


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


def deploy():
    """makes the whole deploy at once"""

    path = do_pack()
    if not path:
        return False

    return do_deploy(path)
