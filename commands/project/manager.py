import click
import os
import CONFIGS
import shutil

@click.command("project")
@click.argument('action', default='create')
@click.argument('name')
def create_project(action, name):
    """
        Description:

        Manage projects with this command.
        
        Creating a new project: \n
        eks project new <name> \n
        eks project create <name> \n



        Delete a project: \n
        eks project del <name> \n
        eks project rm <name> \n
        eks project remove <name> \n
    """
    action_swticher = {
        "create" : create_new_project,
        "new" : create_new_project,
        "del" : delete_project,
        "remove" : delete_project,
        "rm" : delete_project,
    }
    action_swticher[action](name)
    

def create_new_project(project_name):
    project_path = os.path.join(
        CONFIGS.OUTPUT_FOLDER,
        'projects',
        project_name
    )
    artifacts_path = os.path.join(project_path, 'artifacts')
    configs_path = os.path.join(project_path, 'configs')
    logs_path = os.path.join(project_path, 'logs')
    if not os.path.exists(project_path):
        os.makedirs(project_path)
        os.makedirs(artifacts_path)
        os.makedirs(logs_path)
        

def delete_project(project_name):
    project_path = os.path.join(
        CONFIGS.OUTPUT_FOLDER,
        'projects',
        project_name
    )
    if os.path.exists(project_path):
        shutil.rmtree(project_path)
        print("Project {} deleted.".format(project_name))
    else:
        print("Project {} does not exist.".format(project_name))
    
