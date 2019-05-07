#!/usr/bin/env python


import click

import prefect

from .auth import auth as _auth
from .describe import describe as _describe
from .execute import execute as _execute
from .get import get as _get
from .run import run as _run


@click.group()
def cli():
    """
    The Prefect CLI for creating, managing, and inspecting your flows.

    \b
    Query Commands:
        get         List high-level object information
        describe    Retrieve detailed object descriptions
        summarize   Aggregate query information

    \b
    Execution Commands:
        execute     Execute a flow's environment
        run         Run a flow

    \b
    Setup Commands:
        auth        Handle Prefect Cloud authorization

    \b
    Miscellaneous Commands:
        version     Get your current Prefect version
        config      Output your Prefect config
    """
    pass


cli.add_command(_auth)
cli.add_command(_describe)
cli.add_command(_execute)
cli.add_command(_get)
cli.add_command(_run)


# Miscellaneous Commands


@cli.command(hidden=True)
def version():
    """
    Get your current Prefect version
    """
    click.echo(prefect.__version__)


@cli.command(hidden=True)
def config():
    """
    Output your Prefect config
    """
    click.echo(prefect.config.to_dict())
