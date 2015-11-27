#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Bartosz Kruszczynski
# Copyright (c) 2015 Bartosz Kruszczynski
#
# License: MIT
#

"""This module exports the Reek plugin class."""

from SublimeLinter.lint import RubyLinter


class Reek(RubyLinter):
    """Provides an interface to reek."""

    syntax = (
        'better rspec',
        'betterruby',
        'cucumber steps',
        'rspec',
        'ruby experimental',
        'ruby on rails',
        'ruby'
    )
    cmd = 'ruby -S reek'
    regex = r'^.+?\[(?P<line>\d+).*\]:(?P<message>.+)'
    tempfile_suffix = 'rb'
    version_args = '-S reek -v'
    version_re = r'reek\s(?P<version>\d+\.\d+\.\d+)'
    version_requirement = '>= 3.5.0'
    config_file = ('-c', 'config.reek')
