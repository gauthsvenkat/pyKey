# pyKey

![](pykey_demo.gif)

A python wrapper for SendInput function (on windows) and xdotool (on linux) to synthesize keystrokes. (Please visit:- https://docs.microsoft.com/en-us/windows/desktop/api/winuser/nf-winuser-sendinput)

This library makes use of SendInput function (on windows) and xdotool (on linux) to simulate keystrokes (as opposed to other python keyboard simulator libraries, which use virtual keyboard codes). The advantage is that this package will work with sending keystrokes to video games (which won't normally work with virtual keyboard codes).

## Requirements
This package was created and tested on python 3.6 on windows 10 and python 3.7 on arch linux and fedora 30. Should work for similar configurations. 

## Installation

Note:- While this package works on both linux and windows, there are some differences in how it actually runs. Most of the common keys will work without a hitch on both windows and linux. Also, note that some may or may not be available depending on the platform. Please refer to showKeys() on the usage section. 

### On Windows

```
pip3 install pyKey
```
### On linux based OSes

This project requires the xdotool to be installed. You can usually install it using your package manager.

For example:
On fedora/openSUSE
```
sudo dnf install xdotool
```
On ubuntu/debian
```
sudo apt install xdotool
```
On Arch
```
sudo pacman -S xdotool
```
Once you have xdotool installed you can run 
```
pip3 install pyKey
```
## Usage

```
from pyKey import pressKey, releaseKey, press, sendSequence, showKeys
```

There are two important functions you need to know about; pressKey() and releaseKey().

pressKey() will press a key and holds it until explicitly called the releaseKey function.
releaseKey() will release a key that was pressed by pressKey function.

Note:- DO NOT forget to call releaseKey() if you have called pressKey already. Not doing do will result in some unforeseen behaviour.

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

Will display the available keys and their corresponding scan codes (on windows) or xdotool name (on linux).


## Credits

The motivation for this project comes from sentdex's python plays gta series in youtube. Several people have already come up with the code as a community to make this work. I just put together everything in a nice package.

## License 
MIT License

Copyright (c) [2019] [Gautham Venkataraman]

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

