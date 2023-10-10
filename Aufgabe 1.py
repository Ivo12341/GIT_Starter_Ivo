def caesarVerschlüsseln(wort):
    for i in range(len( wort)):
        ordwort = ord(wort[i])
        ordPlus = ordwort + 5
        print(chr(ordPlus))


def caesarEntschlüsseln(wort):
    for i in range(len( wort)):
        ordWortneu = ord(wort[i])
        ordWortneu = ordWortneu - 5
        print(chr(ordWortneu))


def spartaVerschlüsseln(satz):
    satzList = []
    for i in satz:
        satzList.append(i)
    posi = 0
    z1 = 0
    z2 = 1
    for c in range(len(satz)):
        satzList[posi] = satz[z1]
        z1 += 1
        posi += 4
        if posi >= len(satzList):
            posi = z2
            z2 += 1
    print(satzList)


def spartaEntschlüsseln(satz):
    satzList = []
    for i in satz:
        satzList.append(i)
    posi = 0
    z1 = 0
    z2 = 1
    for c in range(len(satz)):
        satzList[z1] = satz[posi]
        z1 += 1
        posi += 4
        if posi >= len(satzList):
            posi = z2
            z2 += 1
    print(satzList)


def spartaXVerschlüsseln(satz ,anzahlSparta):
    satzList = []
    for i in satz:
        satzList.append(i)
    posi = 0
    z1 = 0
    z2 = 1
    for c in range(len(satz)):
        satzList[posi] = satz[z1]
        z1 += 1
        posi += anzahlSparta
        if posi >= len(satzList):
            posi = z2
            z2 += 1
    print(satzList)

def spartaXEntschlüsseln(satz ,anzahlSparta):
    satzList = []
    for i in satz:
        satzList.append(i)
    posi = 0
    z1 = 0
    z2 = 1
    for c in range(len(satz)):
        satzList[z1] = satz[posi]
        z1 += 1
        posi += anzahlSparta
        if posi >= len(satzList):
            posi = z2
            z2 += 1
    print(satzList)
spartaVerschlüsseln("Hallo das wird verschlüsselt")
spartaEntschlüsseln("Ha lasvül eslwrsoise rclddht")
spartaXVerschlüsseln("Hallo ihr seid alle Clowns", 8)
spartaXEntschlüsseln("Hore lCwa  iaelnlisdl oslh", 8)