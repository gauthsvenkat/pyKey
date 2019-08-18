import subprocess
import time
from pyWinKey.key_dict import linux_dict as key_dict

#Presses a key and holds it until explicitly called the releaseKey function.
def pressKey(key=None):
    assert key is not None, "No keys are given (key=None). Please check your code"
    assert key in key_dict, "The key({}) you're trying to press does not exist! Please check for any spelling errors.".format(key)
    
    subprocess.call(['xdotool', 'keydown', key_dict[key]])

#Releases a key that was pressed using pressKey. NEVER FORGET TO USE THIS AFTER USING pressKey()
def releaseKey(key=None):
    assert key is not None, "No keys are given (key=None). Please check your code"
    assert key in key_dict, "The key({}) you're trying to press does not exist! Please check for any spelling errors.".format(key)
    
    subprocess.call(['xdotool', 'keyup', key_dict[key]])

#Presses a key and releases it. If sec argument is given, this function will press and hold a key for that many seconds.
def press(key=None, sec=0):
    assert key is not None, "No keys are given (key=None). Please check your code"
    assert key in key_dict, "The key({}) you're trying to press does not exist! Please check for any spelling errors.".format(key)
    assert sec >= 0, 'Seconds cannot be negative' 

    if sec == 0:
        subprocess.call(['xdotool', 'key', key_dict[key]])
    else:
        subprocess.call(['xdotool', 'keydown', key_dict[key]])
        time.sleep(sec)
        subprocess.call(['xdotool', 'keyup', key_dict[key]])

'''Send a sequence of key presses. If sequence is a string, it'll be simulated. If sequence is a list of keys, it'll be simulated. If sequence is a dict, it will be interpreted as a key value pair, whose key is the key that is going to be pressed and the value as how long to hold the key for (in seconds).'''
def sendSequence(seq=None):
    assert seq is not None, "No sequence is given (seq=None). Please check your code"

    if isinstance(seq, str):
        subprocess.call(['xdotool', 'type', "{}".format(seq)])

    elif isinstance(seq, list):
        for key in seq:
            press(key)

    elif isinstance(seq, dict):
        for key, sec in seq.items():
            press(key, sec)

#Show the list of available keys and their scancodes.
def showKeys():
    print('These are the available keys and their corresponding xdotool names')
    print('{:20}'.format('Key'), 'Xdotool Name')
    print('')
    for key, name in key_dict.items():
        print('{:20}'.format(key), name)
