import configparser
import os

class Manager:
    def __init__(self):
        self.state = None
        self.project = self.get_last_project()

    def set_state(self, state):
        self.state = state

    def set_project(self, project):
        self.project = project

    def set_last_project(self, project_name):
        _config = configparser.ConfigParser()
        _config_file = os.path.join('logs', 'session_details.conf')
        _config.read(_config_file)
        _config['session-log']['last_project'] = project_name
        with open(_config_file, 'w') as configfile:
            _config.write(configfile)

    def get_last_project(self):
        _config = configparser.ConfigParser()
        _config.readfp((open(
            os.path.join('logs', 'session_details.conf')
        )))
        _last_project = _config.get('session-log', 'last_project')
        return _last_project

    def has_project(self):
        if self.project == None:
            return False
        else:
            return True