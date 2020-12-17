from enum import Enum
from operator import itemgetter
from functools import partial

class Workflow:
    '''Setup workflow.'''
    def __init__(self, name):
        self.workflow_name = name
        self.workflow_tasks = []

    def add_task(self, name, func, *args):
        new_task = Task(name, func, args)
        self.workflow_tasks.append(new_task)

    def execute(self):
        for item in self.workflow_tasks:
            item.task_function(*item.task_function_args)

class Task:
    '''Class to manage Tasks.
    '''
    is_scheduled = False
    priority = 0
    schedule_times = []
    actual_start_time = None
    actual_end_time = None
    task_function = None
    task_function_args = None
    exectuion_style = 'sync'

    def __init__(self, name, func, args):
        self.task_name = name
        self.state = TaskState(0)
        self.task_function = func
        self.task_function_args = args

class TaskState(Enum):
    stopped_error = -1
    not_started = 0
    running = 1
    completed = 2