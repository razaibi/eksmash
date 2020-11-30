import os
import actions.common as ac
import config
from actions import secrets

def test(params):
    _injectors = ac.get_injectors('iotclient')
    _raw_base_template = ac.read_template_raw('iot', 'iotclient')
    _iot_hub_connection = secrets.get({
        'provider' : params['provider']
    })
    # Generate code for IoT Client.
    _rendered_template = ac.render_template(_raw_base_template, 
        {
            'messages' : _injectors['messages'],
            'configs' : {
                'iot_hub_connection' : _iot_hub_connection
            }
        }
    )
    # Write Template to file 
    _app_name =  '{}.py'.format(params['app'])
    ac.write_to_file(
        _app_name,
        _rendered_template
    )
    # Execute project.
    os.system('python3 {}'.format(os.path.join(
        'output',
        _app_name)
    ))