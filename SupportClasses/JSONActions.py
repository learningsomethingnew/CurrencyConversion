####################################################################
# JSON Library to handle interactions with file type
####################################################################
from json import *

class JSONActions():

    def __init__(self):
        pass

#returns a dictionary of json input
    def get_json_response(self, a_json_input):
        return load(a_json_input)