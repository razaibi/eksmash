#Define custom actions here.
import actions.common as ac
import template_logic.faust as tl
from core.session_manager import Session

def set(params):
    _project_name = params['name']
    _session = Session()
    _session.set_last_project(_project_name)
    print('Active project set to {}.'.format(_project_name))

def get(params):
    _session = Session()
    _project_name = _session.get_last_project()
    print('Active Project : {}'.format(_project_name))