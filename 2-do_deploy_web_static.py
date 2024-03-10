#!/usr/bin/python3
""" Fabric script to distribute an archive to a web server """
import os
from fabric.api import env, put, run

env.hosts = ["100.26.225.15", "54.237.106.87"]


def do_deploy(archive_path):
    """ Distributes an archive to a web server.

    Args:
        archive_path (str): The path of the archive to distribute.

    Returns:
        If the file doesn't exist at archive_path or an error occurs - False.
        Otherwise - True.
    """
    if not os.path.isfile(archive_path):
        return False

    file = os.path.basename(archive_path)
    file_no_ext = os.path.splitext(file)[0]

    put(archive_path, "/tmp/")
    run("mkdir -p /data/web_static/releases/{}/".format(file_no_ext))
    run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/"
        .format(file, file_no_ext))
    run("rm /tmp/{}".format(file))
    run("mv -f /data/web_static/releases/{}/web_static/* "
        "/data/web_static/releases/{}/"
        .format(file_no_ext, file_no_ext))
    run("rm -rf /data/web_static/releases/{}/web_static".format(file_no_ext))
    run("rm -rf /data/web_static/current")
    run("ln -s /data/web_static/releases/{}/ /data/web_static/current"
        .format(file_no_ext))
    return True


if __name__ == "__main__":
    pass
