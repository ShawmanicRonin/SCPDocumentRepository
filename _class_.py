#TODO use the class to create a dictionary and create a uniform display template.
import colorama
from colorama import Fore, Back, Style, init
colorama.init(autoreset=True)
from docs import *
from skeleton import SearchBot
from munch import Munch
n = 'null' #if i forgot to remove this, it is a global value to put in functions before I am ready to code them to avoid bugs.

# class SCP:
#     DocLog = {'001':['Keter', 'Doc']}

#     # Number = DocLog.get[key]
#     # ObjectClass = DocLog.get[value]

#     @classmethod
#     def GetDocDeets(cls, Number, ObjectClass, Doc):
#         n

#     # def __init__(self, Number, ObjectClass, Doc):
#     #     self.Number = Number
#     #     self.ObjectClass = ObjectClass
#     #     self.Doc = Doc
    
#     def __repr__(self):
#         return "SCP:('{}\n'Object Class:'{}\n'Special Containment Procedures:'{}'".format(self.Number, self.ObjectClass, self.Doc)

#     def DocInstanceCreator(self):
#         n

#     def DisplayDoc(self):
#         return f''
    

class SCP:
    DocLog = {'001':[3, one],'002':[2, two]}
    
    def DocLayout(self, Number, DocNum):
        self.Number = SCP.DocLog.keys
        self.DocNum = SearchBot()
        Header = f'SCP:{self.Number}\n'
        if 1 in SCP.DocLog.items():
            ObjectClass = 'Safe'
        elif 2 in SCP.DocLog.items():
            ObjectClass = 'Euclid'
        elif 3 in SCP.DocLog.items():
            ObjectClass = 'Keter'
        else:
            ObjectClass = 'Not Recorded'
        
        Classification = f'Object Class:{ObjectClass}'

        if DocNum in SCP.DocLog.items:
            return f'\n\n{Style.BRIGHT}{Header}{Style.RESET_ALL}{'Object Class:'}{Classification}{Back.WHITE + Fore.BLACK}{SCP.DocLog.get(SearchBot, 'That entry is not in the archive yet.')}'
        
























#use .get method to avoid errors
#use .update
#use .keys to display entries
    #use for key in *dictionary* to print each key on new line
    #use for key, value in *dictionary*.items to print each key and value on paired up lines
#use .items to return keys and their values   