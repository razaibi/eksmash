import actions.common
from core.session_manager import Session
from core.error import ErrorHandler

class Engine:
    def __init__(self, session):
        self._session=session

    def init_actions(self, actions, params):
        try:
            self._enumerate_actions(actions, params)
            return {
                    'status' : 1,
                    'message' : 'Action invoked.',
                    'data' : 'Invoke'
            }
        except Exception as e:
            _error_handler = ErrorHandler()
            return _error_handler.raise_action_error(
                actions[0]['library']
            )
        

    def _enumerate_actions(self, actions, params):
        for action in actions:
            self._process_action(action, params)

    def _process_action(self, action, params):
        #params['session']=self._session.state
        _method = action['method']
        _library = action['library']
        exec('import actions.{}'.format(_library))
        exec('executor=actions.{}.Executor({})'.format(
            _library,
            params
        ))
        eval('executor.{}()'.format(
            _method
        ))
        