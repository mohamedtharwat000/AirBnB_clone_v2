#!/usr/bin/python3

from fabric.api import run, put, env
from os import path


env.hosts = ["100.26.53.140", "100.26.244.194"]


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

        run(f'mv {release_folder}/web_static/* {release_folder}')
        run(f'rm -r {release_folder}/web_static/')
        run('rm -rf /data/web_static/current')

        run(f'ln -s {release_folder} /data/web_static/current')

        return True

    except Exception as e:
        return False
