# -*- coding: utf-8 -*-
"""
    pip less lexer
    ~~~~~~~~~~~

    Pygments lexer for less piped pip output.

    :license: GNU I guess
"""

from pygments.lexer import RegexLexer, bygroups
from pygments.token import *


class PipLexer(RegexLexer):
    name = 'Pip'
    aliases = ['pip']
    filenames = ['*.piplex']

    tokens = {
        'root': [
            (r'(^[^\s][^.]*?)([\s-]{2})', bygroups(Generic.Strong, Text)),
            (r'.*?\n', Text)
        ]
    }
