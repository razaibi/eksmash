#Define custom actions here.
import actions.common as ac
from core.session_manager import Session
import os

class Executor:
    '''Class to manage actions for Projects.'''
    def __init__(self, params):
        self.params = params

    def set(self, params):
        _project_name = self.params['name']
        _session = Session()
        _session.set_last_project(_project_name)
        self.initialize_project(_project_name)
        print('Active project set to {}.'.format(_project_name))

    def get(self, params):
        _session = Session()
        _project_name = _session.get_last_project()
        print('Active Project : {}'.format(_project_name))

    def initialize_project(self, project_name):
        ac.create_folder('actions', project_name)
        ac.create_folder('injectors', project_name)
        ac.create_folder('output', project_name)
        ac.create_folder('templates', project_name)
        print('Project Initialized.')

