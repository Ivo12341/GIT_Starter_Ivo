morseCode = {
    "a" :".-" ,
    "b" :"-..." ,
    "c" : "-.-.",
    "d" :"-.." ,
    "e" :"." ,
    "f" : "..-.",
    "g" :"--." ,
    "h" : "....",
    "i" :".." ,
    "j" : ".---",
    "k" : "-.-",
    "l" :".-.." ,
    "m" :"--" ,
    "n" :"-." ,
    "o" :"---" ,
    "p" :".--." ,
    "q" :"--.-" ,
    "r" : ".-.",
    "s" : "...",
    "t" : "-",
    "u":"..-" ,
    "v" : "...-",
    "w" : ".--" ,
    "x" :"-..-" ,
    "y" : "-.--",
    "z" :"--.."  
}
text = str(input("Geben sie einen Stz ein: "))
for i in text:
    if i in morseCode.keys():
        print(morseCode.get(i), end="")
    else:
        print(" ")