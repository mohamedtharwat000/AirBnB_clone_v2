#!/usr/bin/python3
""" doc """
import os
from fabric.api import *

env.hosts = ["100.26.53.140", "100.26.244.194"]


def do_clean(number):
    """ delete unused archives """

    number = int(number)

    if number < 1:
        number = 1

    with lcd('versions'):
        archives = sorted(local('ls -t *.tgz', capture=True).split('\n'))
        archives = archives[:number]

    for arc in archives:
        local(f'rm -rf versions/{arc}')

    with cd('/data/web_static/releases'):
        archives = run("ls -tr").split()
        archives = [a for a in archives if 'web_static_' in a]
        archives = archives[:number]

        for arc in archives:
            run(f'rm -rf ./{arc}')
