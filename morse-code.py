#
#  Morse Code
#  Encoder / Decoder
#  (c) Afaan Bilal
#

from __future__ import print_function

CODE = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    "/": "-..-.",
    "@": ".--.-.",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----",
    " ": "/"
}

def text2morse(text):
    ret = []
    for t in list(text):
        t = t.upper()
        if t in CODE:
            ret.append(CODE[t])
            ret.append(' ')
    return ''.join(ret)

def morse2text(morse):
    ret = []
    for m in morse.split(' '):
        for key, val in CODE.items():
            if val == m:
                ret.append(key)
    return ''.join(ret)
    

print("Morse Code")
print("Encoder / Decoder")
print("https://github.com/AfaanBilal/py-morse-code")
print("Options:")
print("    1 - Encode")
print("    2 - Decode")
choice = input("Enter your choice: ")

if choice == "1":
    print("\nMorse Encoder")
    inp = input("Enter a string: ")
    print("Encoded: " + text2morse(inp))
elif choice == "2":
    print("\nMorse Decoder")
    inp = input("Enter a string: ")
    print("Decoded: " + morse2text(inp))
else:
    print("Invalid choice.")
