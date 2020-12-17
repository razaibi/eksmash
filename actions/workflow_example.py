#Define custom actions here.
import actions.common as ac
from core.workflow_manager import Workflow
import template_logic.fastapi as tl
import config
import os

class Executor:
    '''Class to manage actions for Sample Workflow.'''
    def __init__(self, params):
        self.workflow = Workflow('wf_fastapi')
        self.params = params
        self.project = ac.session.get_last_project()
        self.api_injectors = ac.get_injectors('fastapi_api')
        self.db_injectors = ac.get_injectors('fastapi_db')
        self.api_injectors['project_name'] = self.project
        self.db_injectors['project_name'] = self.project
            
    def initiate(self):
        self.workflow.add_task(
            'Some Action One',
            self.do_action_one
        )

        self.workflow.add_task(
            'Some Action Two',
            self.do_action_one
        )
        self.workflow.execute()

    def do_action_one(self):
        print('Did action one.')

    def do_action_two(self):
        print('Did action two.')

