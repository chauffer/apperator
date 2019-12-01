import click
import yaml
import subprocess

from .classes import Apperator, YamlInput, f_to_manifests

@click.group()
def cli():
    pass

@cli.command()
@click.option('-f', default='-', help='apperator manifest')
def build(f):
    print(f_to_manifests(f).decode())


@cli.command()
@click.option('-f', default='-', help='apperator manifest')
def apply(f):
    print(subprocess.check_output(
        ['kubectl', 'apply', '-f', '-'],
        input=f_to_manifests(f),
    ).decode('utf-8'))


@cli.command()
@click.option('-f', default='-', help='apperator manifest')
def delete(f):
    print(subprocess.check_output(
        ['kubectl', 'delete', '-f', '-'],
        input=f_to_manifests(f),
    ).decode('utf-8'))

@click.group()
def cli():
    pass

cli.add_command(build)
cli.add_command(apply)
cli.add_command(delete)
