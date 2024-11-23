#TODO use the class to create a dictionary and create a uniform display template.
import colorama
from colorama import Fore, Back, Style, init
colorama.init(autoreset=True)
from munch import Munch
n = 'null' #if i forgot to remove this, it is a global value to put in functions before I am ready to code them to avoid bugs.

class SCP:
    def __init__(self, DocLog=None):
        if DocLog is None:
            DocLog = {'one':'why'}
        self.DocLog = DocLog

    def add_item(self, key, value):
        self.DocLog[key] = value

    def get_item(self, key):
        return self.DocLog.get(key)

    def print_dict(self):
        print(self.DocLog)























#use .get method to avoid errors
#use .update
#use .keys to display entries
    #use for key in *dictionary* to print each key on new line
    #use for key, value in *dictionary*.items to print each key and value on paired up lines
#use .items to return keys and their values   