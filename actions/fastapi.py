#Define custom actions here.
import actions.common as ac
import template_logic.fastapi as tl
import config
import os

class Executor:
    '''Class to manage actions for Fast API.'''
    def __init__(self, params):
        self.params = params
        self.project = ac.session.get_last_project()
        self.api_injectors = ac.get_injectors('fastapi_api')
        self.db_injectors = ac.get_injectors('fastapi_db')
        self.api_injectors['project_name'] = self.project
        self.db_injectors['project_name'] = self.project
            
    def initiate(self):
        ac.create_directory(self.project)
        self.generate_main()
        self.generate_api()
        self.generate_dtos()
        self.generate_db()
        self.generate_models()
        self.generate_db_manager()

    def generate_main(self):
        _rendered_template = ac.read_template(
            'fastapi',
            'main',
            self.api_injectors
        )
        ac.write_to_file(
            os.path.join(self.project, 'main.py'),
            _rendered_template
        )

    def generate_api(self):
        _folder_path = os.path.join(self.project,'api')
        ac.create_directory(_folder_path)
        _injector = {}
        for item in self.api_injectors['classes']:
            _injector['item'] = item
            _injector['project_name'] = self.project
            _rendered_template = ac.read_template(
                'fastapi',
                'api',
                _injector
            )
            ac.write_to_file(
                os.path.join(
                    self.project,
                    'api', 
                    item['name'].lower() + 's.py'
                ),
                _rendered_template
            )

    def generate_dtos(self):
        _injector = {}
        for item in self.api_injectors['classes']:
            _injector['item'] = item
            _injector['project_name'] = self.project
            _rendered_template = ac.read_template(
                'fastapi',
                'dto',
                _injector
            )
            ac.write_to_file(
                os.path.join(
                    self.project,
                    'dto',
                    '{}.py'.format(item['name'])
                ),
                _rendered_template
            )

    def generate_db(self):
        self.db_injectors['db_connection'] = \
        "{}.api.app_config.POSTGRES_CONNECTION".format(
            self.project
        )
        _rendered_template = ac.read_template(
            'fastapi',
            'db',
            self.db_injectors
        )
        ac.write_to_file(
            os.path.join(self.project, 'api', 'db.py'),
            _rendered_template
        )
        ac.write_to_file(
            os.path.join(self.project, 'api', 'app_config.py'),
            'POSTGRES_CONNECTION="{}"'.format(
                config.POSTGRES_CONNECTION
            )
        )

    def generate_models(self):
        self.db_injectors['db_connection'] = \
        "{}.api.app_config.POSTGRES_CONNECTION".format(self.project)
        _rendered_template = ac.read_template(
            'fastapi',
            'db',
            self.db_injectors
        )
        # TODO: Make config imported from one file
        # TODO: Ensure metadata is shared with the main.py file
        for table in self.db_injectors['tables']:
            ac.write_to_file(
                os.path.join(self.project, 'api', '{}.py'.format(table['name'])),
                _rendered_template
            )
            ac.write_to_file(
                os.path.join(self.project, 'api', 'app_config.py'),
                'POSTGRES_CONNECTION="{}"'.format(
                    config.POSTGRES_CONNECTION
                )
            )

    def generate_db_manager(self):
        _rendered_template = ac.read_template(
            'fastapi',
            'db_manager',
            self.api_injectors
        )
        ac.write_to_file(
            os.path.join(self.project, 'api', 'db_manager.py'),
            _rendered_template
        )
