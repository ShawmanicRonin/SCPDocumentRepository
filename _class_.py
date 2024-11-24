#TODO use the class to create a dictionary and create a uniform display template.
import colorama
from colorama import Fore, Back, Style, init
colorama.init(autoreset=True)
from munch import Munch
n = 'null' #if i forgot to remove this, it is a global value to put in functions before I am ready to code them to avoid bugs.

class SCP:
    DocLog = {'001':['Keter', 'Doc']}

    # Number = DocLog.get[key]
    # ObjectClass = DocLog.get[value]

    @classmethod
    def GetDocDeets(cls, Number, ObjectClass, Doc):
        n

    # def __init__(self, Number, ObjectClass, Doc):
    #     self.Number = Number
    #     self.ObjectClass = ObjectClass
    #     self.Doc = Doc
    
    def __repr__(self):
        return "SCP:('{}\n'Object Class:'{}\n'Special Containment Procedures:'{}'".format(self.Number, self.ObjectClass, self.Doc)

    def DocInstanceCreator(self):
        n

    def DisplayDoc(self):
        return f''
























#use .get method to avoid errors
#use .update
#use .keys to display entries
    #use for key in *dictionary* to print each key on new line
    #use for key, value in *dictionary*.items to print each key and value on paired up lines
#use .items to return keys and their values   