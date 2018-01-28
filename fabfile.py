#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (C) 2016, cloudez Adm. Sis. SA. <hello@cloudez.io>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# On Debian systems, you can find the full text of the license in
# /usr/share/common-licenses/GPL-2

import time

from fabric.api import env, local, puts


#
# available environments
#
def production():
    env.user = 'pythonbrasil'
    env.deploy_path = '/srv/2017.pythonbrasil.org.br/www'
    env.current_path = '/srv/2017.pythonbrasil.org.br/www/current'
    env.releases_path = '/srv/2017.pythonbrasil.org.br/www/releases'
    env.releases_limit = 3
    env.git_origin = 'https://github.com/pythonbrasil/pythonbrasil13-site.git'
    env.git_branch = 'master'
#
# end available environments
#


#
# available commands
#
def deploy():
    start = time.time()

    setup()
    checkout()
    releases()
    symlink()
    cleanup()

    final = time.time()
    puts('execution finished in %.2fs' % (final - start))


def rollback():
    start = time.time()

    setup()
    releases()
    rollback_code()

    final = time.time()
    puts('execution finished in %.2fs' % (final - start))
#
# end available commands
#


#
# internal commands
#
def setup():
    local('mkdir -p {}'.format(env.deploy_path))
    local('mkdir -p {}/releases'.format(env.deploy_path))


def checkout():
    env.current_release = '{0}/{1:.0f}'.format(env.releases_path, time.time())
    local('cd {0}; git clone -q -b {1} -o deploy --depth 1 {2} {3}'.format(
        env.releases_path, env.git_branch, env.git_origin,
        env.current_release))


def releases():
    env.releases = sorted(
        local('ls -x {}'.format(env.releases_path), capture=True).split())


def symlink():
    local('ln -nfs {0} {1}'.format(env.current_release, env.current_path))


def cleanup():
    if len(env.releases) > env.releases_limit:
        directories = env.releases
        directories.reverse()
        del directories[:env.releases_limit]
        env.directories = ' '.join(['{0}/{1}'.format(
            env.releases_path, release) for release in directories])
        local('rm -rf {}'.format(env.directories))


def rollback_code():
    if len(env.releases) > 1:
        env.current_release = env.releases[-1]
        env.previous_revision = env.releases[-2]
        env.current_release = '{0}/{1}'.format(
            env.releases_path, env.current_revision)
        env.previous_release = '{0}/{1}'.format(
            env.releases_path, env.previous_revision)
        command = 'rm {0}; ln -s {1} {0} && rm -rf {2}'
        local(command.format(
            env.current_path, env.previous_release, env.current_release))
#
# end internal commands
#
