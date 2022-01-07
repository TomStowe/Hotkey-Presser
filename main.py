import argparse
from pynput.keyboard import Key, Controller

# The dictionary of the keys to convert
keyConversions = {
    "win": Key.cmd,
    "cmd": Key.cmd,
    "shift": Key.shift,
    "ctrl": Key.ctrl,
    "alt": Key.alt,
    "caps": Key.caps_lock,
    "delete": Key.delete,
    "up": Key.up,
    "down": Key.down,
    "left": Key.left,
    "right": Key.right,
    "insert": Key.insert,
    "home": Key.home,
    "end": Key.end,
    "pageup": Key.page_up,
    "pagedown": Key.page_down,
    "enter": Key.enter,
    "esc": Key.esc,
    "f1": Key.f1,
    "f2": Key.f2,
    "f3": Key.f3,
    "f4": Key.f4,
    "f5": Key.f5,
    "f6": Key.f6,
    "f7": Key.f7,
    "f8": Key.f8,
    "f9": Key.f9,
    "f10": Key.f10,
    "f11": Key.f11,
    "f12": Key.f12,
    "f13": Key.f13,
    "f14": Key.f14,
    "f15": Key.f15,
    "f16": Key.f16,
    "f17": Key.f17,
    "f18": Key.f18,
    "f19": Key.f19,
    "f20": Key.f20,
}

# Setup the arguments
parser = argparse.ArgumentParser(description="Press the keys for a hotkey")
parser.add_argument("keycombo", type=str, help="The hotkey to use, where each key is separated by a + sign.\nAll letters and numbers are available to use in addition to the following keys: \"" + ', '.join(keyConversions.keys()) + "\"")
args = parser.parse_args()

# Setup the controller
keyboard = Controller()

"""
    Convert a string to a key value
    val: The string value to convert
    returns: The key version of the string
"""
def stringToKey(val: str):
    if (val in keyConversions):
        return keyConversions[val]
    return val

# Press the keys for the shortcut
for key in args.keycombo.split("+"):
    keyboard.press(stringToKey(key))
    
# Release the keys for the shortcut
for key in args.keycombo.split("+"):
    keyboard.release(stringToKey(key))