"""
A pygmentize lexer to highlight pip package names
when piped through less.
"""

from setuptools import setup

entry_points = """
[pygments.lexers]
piplexer = piplexer.piplex:PipLexer
"""

setup(
    name='piplexer',
    version='0.1',
    description="A lexer for pip",
    author="b b",
    packages=['piplexer'],
    entry_points=entry_points
)
