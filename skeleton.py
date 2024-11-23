import sys
import random
import string
from colorama import Fore, Back, Style #I ran a pip install command to run this code. This link will hopefully give you the same google A.I. results I had... 
#https://www.google.com/search?q=how+to+print+different+color+text+to+terminal+python&rlz=1C1RXQR_enUS927US927&oq=how+to+print+different+color+text+to+term&gs_lcrp=EgZjaHJvbWUqBwgBECEYoAEyBggAEEUYOTIHCAEQIRigATIHCAIQIRigATIHCAMQIRigATIHCAQQIRiPAtIBCTE1ODk4ajBqN6gCALACAA&sourceid=chrome&ie=UTF-8
from _class_ import SCP
from _class_ import n #importing temp value

redacted_10 = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(10))
redacted_25 = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(25))
redacted_5 = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(5))
redacted_2 = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(2))

ChoiceSeparator = '-'* 5
def Menu():
    print(f'what would you like to do?\n\n',
          'Search the archive', ChoiceSeparator, '1\n',
          'Retrieve a random entry', ChoiceSeparator, '2\n',
          'Append the archive', ChoiceSeparator, '3\n',
          'Exit the archive', ChoiceSeparator, '4\n\n\n\n\n',
          'Reminder: Unauthorized accsess of the SCP archive is punishable by a maximum sentence of',
          {redacted_5},'years of service as D-class personell.\n',
          'Sentence length varries by sensitivity of compromised material.\n',
          'Maximum sentencing length can exceed preception of',{redacted_25},'years.')
    menu_choice = int(input('>'))
    if menu_choice == 1:
        n
    elif menu_choice == 2:
        n
    elif menu_choice == 3:
        n
    elif menu_choice == 4:
        exit()

def exit():
    sys.exit('https://www.youtube.com/watch?v=dQw4w9WgXcQ')

 #TODO create a function that takes string input to search for a key name and intigers to search by key number.
def search():
    print(f'')
    search_input = input('> ')

#TODO create a function that returns a random archinve entry.
def _random():
    n

#TODO create a function that allows the user to edit the dictionary contents
def append():
    n


Menu()