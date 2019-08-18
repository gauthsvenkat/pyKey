import sys

if sys.platform == 'linux':
    from pyKey.linux import pressKey, releaseKey, press, showKeys, sendSequence
elif sys.platform == 'win32':
    from pyKey.windows import pressKey, releaseKey, press, showKeys, sendSequence

