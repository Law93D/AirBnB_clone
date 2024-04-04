#!/usr/bin/python3
"""Fabric script that deletes out-of-date archives"""

from fabric.api import env, local, run
from os.path import exists, isfile
env.hosts = ['34.227.93.156', '3.85.136.88']


def do_clean(number=0):
    """Deletes out-of-date archives"""
    number = int(number)
    if number < 1:
        number = 1
    number += 1
    local("ls -1t versions | tail -n +{} | xargs -I {{}} rm versions/{{}}"
          .format(number))
    run("ls -1t /data/web_static/releases | tail -n +{} | xargs -I {{}} rm -rf /data/web_static/releases/{{}}"
        .format(number))
