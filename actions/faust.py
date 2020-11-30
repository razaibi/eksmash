#Define custom actions here.
import actions.common as ac
import template_logic.faust as tl
import os

def init(params):
    _injectors = ac.get_injectors('faust')
    _rendered_template = ac.read_template(
        'faust',
        'app',
        _injectors
    )
    ac.write_to_file('{}.py'.format(_injectors['app_name']),_rendered_template)
    print('Review app named {} in the output folder.'.format(
        _injectors['app_name']
    ))

def test(params):
    _injectors = ac.get_injectors('faust_message')
    _raw_template = ac.read_template_raw('faust','send_message')
    
    for item in _injectors['messages']:
        item.__setitem__('app_name', _injectors['app_name']) 
        _rendered_command = ac.render_template(_raw_template, item)
        ac.append_to_file('{}.sh'.format(
            _injectors['app_name']),
            _rendered_command + '\n'
        )
    ac.own_script(_injectors['app_name'])
    ac.switch_dir(os.path.join(os.getcwd(),'output'))
    ac.invoke_script(
        os.path.join(os.getcwd(),_injectors['app_name'])
    )