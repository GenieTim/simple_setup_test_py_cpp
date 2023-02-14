#!/usr/bin/env python
# cli.py
import click
import numpy as np

from simple_setup_test_py_cpp import UniverseSequence


@click.command()
@click.argument('files', nargs=-1, type=click.Path(exists=True))
def cli(files):
    """
    Basic CLI application listing all passed files

    Arguments:
      - files: list of files to read
    """
    click.echo("Processing {} files".format(len(files)))
    for filePath in files:
        click.echo("\nAnalysing File " + filePath)
    click.echo("Arbitrary units used. E.g.: Length: u")


if __name__ == "__main__":
    cli()
