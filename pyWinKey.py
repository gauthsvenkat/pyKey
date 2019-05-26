import ctypes
import time
from key_dict import key_dict


SendInput = ctypes.windll.user32.SendInput

# C struct redefinitions 
PUL = ctypes.POINTER(ctypes.c_ulong)
class KeyBdInput(ctypes.Structure):
    _fields_ = [("wVk", ctypes.c_ushort),
                ("wScan", ctypes.c_ushort),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class HardwareInput(ctypes.Structure):
    _fields_ = [("uMsg", ctypes.c_ulong),
                ("wParamL", ctypes.c_short),
                ("wParamH", ctypes.c_ushort)]

class MouseInput(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time",ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class Input_I(ctypes.Union):
    _fields_ = [("ki", KeyBdInput),
                 ("mi", MouseInput),
                 ("hi", HardwareInput)]

class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("ii", Input_I)]


#Presses a key and holds it until explicitely called the releaseKey function.
def pressKey(key=None):

    assert key is not None, "No keys are given (key=None). Please check your code"
    assert key in key_dict, "The key({}) you're trying to press does not exists! Please check for any spelling errors.".format(key)

    extra = ctypes.c_ulong(0)
    ii_ = Input_I()

    #These keys use the extendedkey prefix 0xE0, directly simulating the actual key rather than the redundant ones in numpad
    if key in ['INS', 'HOME', 'PGUP', 'PGDN', 'END', 'DEL', 'UP', 'DOWN', 'LEFT', 'RIGHT']:
        ii_.ki = KeyBdInput( 0, key_dict[key], 0x0008 | 0x0001, 0, ctypes.pointer(extra) )
    #Else normal use
    else: ii_.ki = KeyBdInput( 0, key_dict[key], 0x0008, 0, ctypes.pointer(extra) )

    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

#Releases a key that was pressed by pressKey function. Doesn't really matter if you're just simulating typing
#text. But it's generally smart to explicitely call releaseKey, particularly if you're trying to simulate
#pressing keys like shift, ctrl, etc.
def releaseKey(key=None):

    assert key is not None, "No keys are given (key=None). Please check your code"
    assert key in key_dict, "The key({}) you're trying to release does not exists! Please check for any spelling errors.".format(key)

    extra = ctypes.c_ulong(0)
    ii_ = Input_I()

    if key in ['INS', 'HOME', 'PGUP', 'PGDN', 'END', 'DEL', 'UP', 'DOWN', 'LEFT', 'RIGHT']:
        ii_.ki = KeyBdInput( 0, key_dict[key], 0x0008 | 0x0002 | 0x0001, 0, ctypes.pointer(extra) )
    else: ii_.ki = KeyBdInput( 0, key_dict[key], 0x0008 | 0x0002, 0, ctypes.pointer(extra) )

    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

#Presses a key and releases it. If sec argument is given, this function will press and hold a key for that many
#seconds.
def press(key, sec=0):

    assert key is not None, "No keys are given (key=None). Please check your code"
    assert sec >= 0, "Seconds cannot be negative"

    shift_flag = None #to check if shift is toggled

    if key in '!@#$%^&*()_+}{~|:"<>?ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        pressKey('LSHIFT')
        shift_flag = True

    pressKey(key.upper())
    time.sleep(sec) #if sec is not 0, hold key for sec seconds
    releaseKey(key.upper())

    if shift_flag: #release shift if shift is toggled
        releaseKey('LSHIFT')

#Send a sequence of key presses. If sequence is a string, it'll be simulated. If sequence is a list of keys, it'll
#be simulated. If sequence is a dict, it will be interpreted as a key value pair, whose key is the key that is 
#going to be pressed and the value as how long to hold the key for (in seconds).
def sendSequence(seq=None):

    #if sequence is a string
    if isinstance(seq, str):
         for c in seq:
            press(c)

    #if sequence is a list
    if isinstance(seq, list):
        for key in seq:
            press(key)

    #if sequence is a dict
    if isinstance(seq, dict):
        for key, sec in seq.items():
            press(key, sec)

#Show the list of available keys and their scancodes.
def showKeys():
    print("These are the available keys and their corresponding hexcode\n\n")
    print('{:20}'.format('Key'), "HEXCODE")
    for key, hexcode in key_dict.items():
        print('{:20}'.format(key), hex(hexcode))







