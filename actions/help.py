#Define custom actions here.
from colorama import Fore, Back, Style
import actions.common as ac
import template_logic.faust as tl
from core.command_definitions import Definition

def get_help(params=None):
    _definition = Definition()
    _command_list = _definition.get_all_definitions()
    for item in _command_list:
        for mode in item['modes']:
            _verb = list(mode.keys())[0]
            print('')
            print(Fore.YELLOW + '{} {}'.format(
                _verb,
                item['identifier']
            ))
            
            _detected_mode = mode[_verb]
            if 'params' in _detected_mode:
                for param in mode[_verb]['params']:
                    print(Fore.CYAN + '\t--{:<10} [{}] {}'.format(
                        param['name'],
                        param['type'],
                        param['desc']
                        )
                    )
            else:
                print(Fore.CYAN + '\t--{:<10}'.format('No parameters'))
            print('')

    