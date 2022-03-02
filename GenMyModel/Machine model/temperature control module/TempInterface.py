from Machine model.Communication Management.serialHandler import serialHandler

class TempInterface(serialHandler):
    def __init__(self):
        self.temp_id = Device IDs.default id
        self.extensionBoard = None
        
    # Start of user code -> properties/constructors for TempInterface class

    # End of user code
    def start_heating(self):
        # Start of user code protected zone for start_heating function body
        raise NotImplementedError
        # End of user code	
    def stop_heating(self):
        # Start of user code protected zone for stop_heating function body
        raise NotImplementedError
        # End of user code	
    def set_temp(self):
        # Start of user code protected zone for set_temp function body
        raise NotImplementedError
        # End of user code	
    def get_temp(self):
        # Start of user code protected zone for get_temp function body
        raise NotImplementedError
        # End of user code	
    # Start of user code -> methods for TempInterface class

    # End of user code

