import actions.common as ac
import os

def generate_base_models(entities):
    #Read raw templates.
    _raw_base_template = ac.read_template_raw('sqlalchemy', 'model')
    _raw_db_connector_template = ac.read_template_raw('sqlalchemy', 'model_connector')
    _rendered_template = None
    _rendered_db_connector_template = None
    #Read rendered templates.
    for item in entities:
        _rendered_template = ac.render_template(_raw_base_template, {'entity_item' : item })
        ac.write_to_file(
            os.path.join('','{}_model.py'.format(item['name'])),
            _rendered_template
        )
    _rendered_db_connector_template = ac.render_template(_raw_db_connector_template, {})
    ac.write_to_file(
            os.path.join('','connection.py'),
            _rendered_db_connector_template
        )
