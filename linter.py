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
import re


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
    cmd = 'reek'
    regex = r'^.+?\[(?P<line>\d+).*\]:(?P<message>.+) \[.*\]'
    tempfile_suffix = 'rb'
    version_re = r'reek\s(?P<version>\d+\.\d+\.\d+)'
    version_requirement = '>= 3.5.0'
    config_file = ('-c', 'config.reek')

    def split_match(self, match):
        """Extract named capture groups from the regex and return them as a tuple."""

        match, line, col, error, warning, message, _ = super().split_match(match)
        near = self.search_token(message)

        return match, line, col, error, warning, message, near

    def search_token(self, message):
        """Search text token to be highlighted."""

        # First search for variable name enclosed in single quotes
        m = re.search("'.*'", message)

        # If there's no variable name search for nil-check message
        if m is None:
            m = re.search('nil(?=-check)', message)

        # If there's no nil-check search for method name that comes after a `#`
        if m is None:
            m = re.search('(?<=#)\S+', message)

        return m.group(0) if m else None
