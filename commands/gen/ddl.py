import click
import os
import CONFIGS
import shutil
import core.gen

_gen_logic = core.gen.ddl

@click.command("ddl")
@click.argument('action', default='create')
@click.option('--file', '-f', default="ddl.yml")
def create_ddl(action, file):
    """
        Description:

        Create scripts for database definition.
    """
    _gen_logic.create_ddl(action, file)




    

    
