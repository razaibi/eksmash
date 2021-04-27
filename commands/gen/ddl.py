import click
import os
import CONFIGS
import shutil
import core

@click.command("ddl")
@click.argument('action', default='create')
@click.option('--file', '-f', default="ddl.yml")
def create_ddl(action, file):
    """
        Description:

        Create scripts for database definition.
        
        Creating a new data definition script: \n
    """
    action_swticher = {
        "create" : create_new_database,
        "new" : create_new_database
    }
    action_swticher[action](file)
    

def create_new_database(file_name):
    project_path = os.path.join(
        CONFIGS.INPUT_FOLDER,
        file_name
    )
    print(core.common.read_yaml(project_path))


def parse_databases(ddl_content):
    for database in ddl_content['databases']:
        parse_tables(database)


def parse_tables(database):
    for table in database['tables']:
        pass


def generate_table_ddl(table):
    for column in table['columns']:
        pass




    

    
