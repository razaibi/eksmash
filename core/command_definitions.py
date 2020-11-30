import yaml
import config
import os

class Definition:
    
    def __init__(self):
        self.resources = None

    def _get_definition(self, definition_name):
        #TODO: TBD
        _definitions = None
        with open(os.path.join(config.DEFINITIONS_FOLDER,config.DEFINITIONS_DEVOPS)) as f:
            _definitions = yaml.load(f, Loader=yaml.FullLoader)
        print(_definitions)

    def _get_definitions(self):
        _definitions = None
        with open(os.path.join(config.DEFINITIONS_FOLDER,config.DEFINITIONS_DEVOPS)) as f:
            _definitions = yaml.load(f, Loader=yaml.FullLoader)

    def get_all_definitions(self):
        '''Get all resource definitions from all definitions world.'''
        _definitions_files = os.listdir(config.DEFINITIONS_FOLDER)
        _resources = []
        for file_item in _definitions_files:
            with open(os.path.join(config.DEFINITIONS_FOLDER,file_item)) as opened_file:
                _current_resources = yaml.load(opened_file, Loader=yaml.FullLoader)['resources']
                _resources += _current_resources
        return _resources

    def filter_resource_definition(self, name):
        return list(filter(lambda elem: elem['identifier'] == name, self.get_all_definitions()))