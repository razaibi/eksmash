class ErrorHandler():
    """Error handler across the application.
    """

    error_struct = {
        'status' : 0,
        'message' : None,
        'data' : None
    }

    def __init__(self):
        pass

    def raise_parsing_error(self):
        pass

    def raise_malformed_command_error(self, message, status=0, data=None):
        self.error_struct['status'] = status
        self.error_struct['message'] = 'Command {} malformed.'.format(
            message
        )
        self.error_struct['data'] = data
        return self.error_struct

    def raise_command_error(self, message, status=0, data=None):
        self.error_struct['status'] = status
        self.error_struct['message'] = 'Command "{}" not found.'.format(
            message
        )
        self.error_struct['data'] = data
        return self.error_struct

    def raise_project_missing_error(self, message, status=0, data=None):
        self.error_struct['status'] = status
        self.error_struct['message'] = 'Project has not been set.{}'.format(
            message
        )
        self.error_struct['data'] = data
        return self.error_struct

    def raise_definition_error(self):
        pass

    def raise_config_error(self):
        pass

    def raise_injector_error(self):
        pass

    def raise_action_error(self, message, status=0, data=None):
        self.error_struct['status'] = status
        self.error_struct['message'] = 'Check actions for "{}".'.format(
            message
        )
        self.error_struct['data'] = data
        return self.error_struct

    def raise_template_error(self):
        pass

    def raise_template_logic_error(self):
        pass

    def raise_session_error(self):
        pass
