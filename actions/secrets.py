#Define custom actions here.
import actions.common as ac
import template_logic.faust as tl
import requests

def get(params):
    if params['provider'].lower() == 'azure':
        _injectors = ac.get_injectors('azure_keyvault')
        _token_request_data = _injectors['requests']['get_vault_token']
        _token_request = ac.call_rest_endpoint(_token_request_data)
        _access_token = _token_request.json()['access_token']
        _secrets_request_data = _injectors['requests']['get_secrets']
        _secrets_request_data = ac.set_bearer_token(
            _secrets_request_data,
            _access_token
        )
        _secrets_request = ac.call_rest_endpoint(_secrets_request_data)
        return _secrets_request.json()['value']
    
