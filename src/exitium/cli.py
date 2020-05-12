# -*- coding: utf-8 -*-

"""Console script for exitium."""
import sys

import click

from . import __version__


@click.command()
@click.version_option(version=__version__)
def main() -> None:
    """The hypermodern Python project."""
    click.echo("Hello, world!")


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
