import yaml
import config
import os
import core.session_manager as sm
from core.command_definitions import Definition
from core.action_manager import Engine
from core.error import ErrorHandler

class CParser:
    verb_list = [
        'get',
        'set',
        'put',
        'del',
        'do',
        'let',
        'create',
        'init',
        'test'
    ]
    command = None
    error_struct = {
        'status' : 0,
        'message' : 'Command {} not found.',
        'data' : None
    }
    def __init__(self):
        pass

    def parse_command(self, session, command):
        self.command = command
        tokens = self._get_tokens(command, ' ')

        #Try to retrieve command from definitions.
        _get_definition = self._get_definition_by_name(tokens)
        if _get_definition['status'] == 1:
            _definition = _get_definition['data'][0]
        else:
            return _get_definition
        if (_definition['name'] == 'Projects' or
            session.get_last_project() != ''):
            #Extract actual parameters from command
            _actual_params = self._get_parameters(tokens)
            _verb = self._get_verb(tokens)["data"]
            _detected_mode = list(filter(lambda x:_verb in x, _definition['modes']))

            #Ensure definition, verb, detected mode are not None.
            if None not in (_definition, _verb, _detected_mode):
                #Get defined parameters.
                _defined_params = self._get_defined_parameters(
                    _detected_mode, _verb
                )
                return self._call_action_engine(
                session,
                 _detected_mode, 
                 _verb,
                 _defined_params, 
                 _actual_params
                )
        else:
            _error_handler = ErrorHandler()
            return _error_handler.raise_project_missing_error('')

            
    def _call_action_engine(self, 
        session,
        detected_mode, 
        verb, 
        defined_params, 
        actual_params):
        #Check if actual parameters passed
        if  self._parameters_match(defined_params, actual_params):
            #If parameters match, invoke list of actions.
            #Use action engine to invoke parameters.
            _actions = detected_mode[0][verb]['actions']
            return self._call_actions(_actions, session, actual_params)
        else:
            return {
                    'status' : 0,
                    'message' : 'Parameters mismatch error.',
                    'data' : actual_params
            }
        
    def _call_actions(self, actions, session, actual_params=None):
        _action_engine = Engine(session)
        return _action_engine.init_actions(
            actions, 
            actual_params
        )

    def _get_parameters(self, tokens):
        _parameters = filter(lambda x:x.startswith('--'), tokens)
        _params = list(_parameters)
        _param_keys = list(map(lambda x: x.split('=')[0].replace('--',''), _params))
        _param_values = list(map(lambda x: x.split('=')[1], _params))
        return {_param_keys[i]: _param_values[i] for i in range(len(_params))}

    def _get_defined_parameters(self, detected_mode, actual_verb):
        '''Get parameters defined in the definitions.
        Use the mode detected in the definition
        with the actual verb (in the command).
        '''
        if 'params' in detected_mode[0][actual_verb]:
            _defined_params = detected_mode[0][actual_verb]['params']
        else :
            _defined_params = None
        return _defined_params



    def _get_verb(self, tokens):
        potential_verb = tokens[0]
        if potential_verb in self.verb_list:
            return {
                "status" : 1,
                "message" : "Verb found.",
                "data" : potential_verb
            }
        else:
            return {
                "status" : 0,
                "message" : "Verb/ action not found.",
                "data" : None
            }

    def _extract_resource(self, tokens):
        '''Get resource type/name from the command.'''
        return tokens[1]

    def _get_tokens(self, command, separator=' '):
        return command.split(separator)

    def _get_definition_by_name(self, tokens):
        '''Check if identified resource in resource definitions.'''
        _resource_definitions = Definition().resources
        if len(tokens) > 0:
            try:
                _potential_resource = self._extract_resource(tokens)
            except Exception as e:
                _error_handler = ErrorHandler()
                return _error_handler.raise_command_error(
                    '_'.join(tokens)
                )
        else:
            return self._check_command_found(
                _potential_resource,
                _filtered_resource
            )
        _filtered_resource = Definition().filter_resource_definition(_potential_resource)
        if len(_filtered_resource)>0:
            return {
                'status' : 1,
                'message' : 'Command found.',
                'data' : _filtered_resource
            }
        else:
            _error_handler = ErrorHandler()
            return _error_handler.raise_command_error(
                ' '.join(tokens)
            )
        

    def _check_command_found(self,_potential_resource, _filtered_resource):
        if _potential_resource is not None:
            _filtered_resource = Definition(
            ).filter_resource_definition(_potential_resource)
            if len(_filtered_resource)>0:
                return {
                    'status' : 1,
                    'message' : 'Command found.',
                    'data' : _filtered_resource
                }
            else:
                _error_handler = ErrorHandler()
                return _error_handler.raise_command_error(
                    _potential_resource
                )



    def _parameters_match(self, defined_params, actual_params):
        _check_actual_params_passed = bool(actual_params)
        #If no parameters are defined in definitions.
        _none_match_check = defined_params is None
        #If parameters are defined in definitions.
        _match_check = defined_params is not None and _check_actual_params_passed

        if _none_match_check:
            return True

        if _match_check:
            _required_params = list(filter(lambda x: x['isRequired'],defined_params))
            _required_params = list(map(lambda item: item['name'], _required_params))
            _actual_params_sorted = list(actual_params.keys())
            _required_params.sort()
            _actual_params_sorted.sort()
            if len(_required_params) > 0:
                return all(item in _actual_params_sorted for item in _required_params)
            else:
                return True
        else:
            return True