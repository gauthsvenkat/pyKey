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


def pressKey(key=None):

    assert key is not None, "No keys are given (key=None). Please check your code"
    assert key in key_dict, "The key({}) you're trying to press does not exists! Please check for any spelling errors.".format(key)

    #import pdb; pdb.set_trace()

    extra = ctypes.c_ulong(0)
    ii_ = Input_I()

    if key in ['INS', 'HOME', 'PGUP', 'PGDN', 'END', 'DEL', 'UP', 'DOWN', 'LEFT', 'RIGHT']:
        ii_.ki = KeyBdInput( 0, key_dict[key], 0x0008 | 0x0001, 0, ctypes.pointer(extra) )
    else: ii_.ki = KeyBdInput( 0, key_dict[key], 0x0008, 0, ctypes.pointer(extra) )

    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

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

def press(key, sec=0):

    if key.isalpha() and key.islower():
        key = key.upper()

    shift_flag = None

    if key in '!@#$%^&*()_+}{~|:"<>?':
        pressKey('LSHIFT')
        shift_flag = True

    pressKey(key)
    time.sleep(sec)
    releaseKey(key)

    if shift_flag:
        releaseKey('LSHIFT')

def sendSequence(seq=None):

    if isinstance(seq, str):
         for c in seq:
            press(c)

    if isinstance(seq, list):
        for key in seq:
            press(key)

    if isinstance(seq, dict):
        for key, sec in seq.items():
            press(key, sec)








