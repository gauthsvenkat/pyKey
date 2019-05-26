# pyWinKey
A python wrapper for SendInput function to synthesize keystrokes. (Please visit:- https://docs.microsoft.com/en-us/windows/desktop/api/winuser/nf-winuser-sendinput)

This library specifically uses the keyboard scan codes to simulate keystrokes (as opposed to other python keyboard simulator libraries, which use virtual keyboard codes). The advantage is that this package will work with sending keystrokes to video games (which won't normally work with virtual keyboard codes).

## Requirements
This package was created and tested on python 3.6 on windows 10. Should work for similar configurations. 

## Installation

Note:- This package is specifically for windows and does NOT work with linux

```
pip install pyWinKey
```

## Usage

```
from pyWinKey import pressKey, releaseKey, press, sendSequence, showKeys
```

There are two important functions you need to know about; pressKey() and releaseKey().

pressKey() will press a key and holds it until explicitly called the releaseKey function.
releaseKey() will release a key that was pressed by pressKey function.

Note:- It doesn't really matter calling releaseKey if you're just simulating typing text. But it's good practice to explicitly call releaseKey, particularly if you're trying to simulate pressing keys like shift, ctrl, etc, or in games.

There are 3 other functions, explained below:

### press(key=None, sec=0)
(Have a look at the available keys by calling showKeys())
key: A string, denoting which key to be pressed. (If it's a superscript character like !, @ press() will automatically hold and release SHIFT key for you)
sec: Int, time in seconds to hold the key

### sendSequence(seq=None)

Will simulate pressing a sequence of keys.
seq: str or list or dict type.

if seq is a string, each character in the string will be pressed one by one
if seq is a list, each item in the list will be pressed one by one
if seq is a dict, it is assumed that the key, value pairs are the key that is to be pressed and the time to hold the key for (in seconds) respectively. 

### showKeys()

Will display the available keys and their corresponding scan codes.


## Credits

The motivation for this project comes from sentdex's python plays gta series in youtube. Several people have come together as a community to make this work. I just put together everything in a nice package.

## License 
MIT License

Copyright (c) [year] [fullname]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

