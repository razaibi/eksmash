import click

from commands.project import manager as project_manager
from commands.gen import webapi as webapi
from commands.gen import ddl as ddl

@click.group()
def cli():
    """
    Initiate the eksm@$h ecosystem with the "eks" command. 

    The general syntax is :

    eks <RESOURCE NAME> <ACTION> <OPTIONS>
    """
    pass 

cli.add_command(webapi.dropdb)
cli.add_command(webapi.initx)
cli.add_command(ddl.create_ddl)
cli.add_command(project_manager.create_project)
