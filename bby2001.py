import os
import yaml
import gzip
from pathlib import Path

class AlphaNum:
    CA = " "
    CB = "!"
    CC = "\\"
    CD = "#"
    CE = "$"
    CF = "%"
    CG = "&"
    CH = "'"
    CI = "("
    CJ = ")"
    CK = "*"
    CL = "+"
    CM = ","
    CN = "-"
    CO = "."
    CP = "/"
    DA = 0
    DB = 1
    DC = 2
    DD = 3
    DE = 4
    DF = 5
    DG = 6
    DH = 7
    DI = 8
    DJ = 9
    DK = " ="
    DL = ";"
    DM = "<"
    DN = "="
    DO = ">"
    DP = "?"
    EA = "@"
    EB = "A"
    EC = "B"
    ED = "C"
    EE = "D"
    EF = "E"
    EG = "F"
    EH = "G"
    EI = "H"
    EJ = "I"
    EK = "J"
    EL = "K"
    EM = "L"
    EN = "M"
    EO = "N"
    EP = "O"
    FA = "P"
    FB = "Q"
    FC = "R"
    FD = "S"
    FE = "T"
    FF = "U"
    FG = "V"
    FH = "W"
    FI = "X"
    FJ = "Y"
    FK = "Z"
    FL = "["
    FM = \
    FN = "]"
    FO = "^"
    FP = "_"
    GA = "~"

class StatRatings:
    AA = 0
    AB = 1
    AC = 2
    AD = 3
    AE = 4
    AF = 5
    AG = 6
    AH = 7
    AI = 8
    AJ = 9
    AK = 10
    AL = 11
    AM = 12
    AN = 13
    AO = 14
    AP = 15
    BA = 16
    BB = 17
    BC = 18
    BD = 19
    BE = 20
    BF = 21
    BG = 22
    BH = 23
    BI = 24
    BJ = 25
    BK = 26
    BL = 27
    BM = 28
    BN = 29
    BO = 30
    BP = 31
    CA = 32
    CB = 33
    CC = 34
    CD = 35
    CE = 36
    CF = 37
    CG = 38
    CH = 39
    CI = 40
    CJ = 41
    CK = 42
    CL = 43
    CM = 44
    CN = 45
    CO = 46
    CP = 47
    DA = 48
    DB = 49
    DC = 50
    DD = 51
    DE = 52
    DF = 53
    DG = 54
    DH = 55
    DI = 56
    DJ = 57
    DK = 58
    DL = 59
    DM = 60
    DN = 61
    DO = 62
    DP = 63
    EA = 64
    EB = 65
    EC = 66
    ED = 67
    EE = 68
    EF = 69
    EG = 70
    EH = 71
    EI = 72
    EJ = 73
    EK = 74
    EL = 75
    EM = 76
    EN = 77
    EO = 78
    EP = 79
    FA = 80
    FB = 81
    FC = 82
    FD = 83
    FE = 84
    FF = 85
    FG = 86
    FH = 87
    FI = 88
    FJ = 89
    FK = 90
    FL = 91
    FM = 92
    FN = 93
    FO = 94
    FP = 95
    GA = 96
    GB = 97
    GC = 98
    GD = 99
    GE = 100
    GF = 101
    GG = 102
    GH = 103
    GI = 104
    GJ = 105
    GK = 106
    GL = 107
    GM = 108
    GN = 109
    GO = 110
    GP = 111
    HA = 112
    HB = 113
    HC = 114
    HD = 115
    HE = 116
    HF = 117
    HG = 118
    HH = 119
    HI = 120
    HJ = 121
    HK = 122
    HL = 123
    HM = 124
    HN = 125
    HO = 126
    HP = 127
    IA = 128
    IB = 129
    IC = 130
    ID = 131
    IE = 132
    IF = 133
    IG = 134
    IH = 135
    II = 136
    IJ = 137
    IK = 138
    IL = 139
    IM = 140
    IN = 141
    IO = 142
    IP = 143
    JA = 144
    JB = 145
    JC = 146
    JD = 147
    JE = 148
    JF = 149
    JG = 150
    JH = 151
    JI = 152
    JJ = 153
    JK = 154
    JL = 155
    JM = 156
    JN = 157
    JO = 158
    JP = 159

class StatCategories:
    #DONOTCHANGE
    P1 = str
    #STAMINA
    P2 = str
    #THROW RELIABILITY
    P3 = str
    #REACTION
    P4 = str
    #SPEED
    P5 = str
    #THROWPOWER
    P6 = str
    #THROWACCURACY
    P7 = str
    #BATTINGPOWER
    P8 = str
    #BATTINGCONTACT
    P9 = str
    #BALLTRACKING
    P10 = str
    #UNKNOWN
    P11 = str
    #Appearance
    P12 = str
    #UNKNOWN
    P13 = str
    #BATS/THROWS
    P14 = str
    #FASTBALL
    P15 = str
    #SLOWBALL
    P16 = str
    #LEFTHOOK
    P17 = str
    #RIGHTHOOK
    P18 = str
    #SCREWBALL
    P19 = str
    #ZIGZAG
    P20 = str
    #BIGFREEZE
    P21 = str
    #FIREBALL
    P22 = str
    #SPITBALL
    P23 = str
    #CRAZYBALL
    P24 = str
    #SLOMO
    P25 = str
    #ELEVATOR
    P26 = str
    #BATTINGSTANCE
    P27 = str
    #HEIGHT
    #NOTE: THIS BASICALLY TELLS THE GAME HOW TALL THE STRIKEZONE SHOULD BE AND HOW HIGH THE CAN REACH WITH THEIR GLOVE
    P28 = str
    #GENDER
    P29 = str
    #BIRTHDAYMONTH
    P30 = str
    #BIRTHDAYDAY
    P31 = str
    #BLOCK FOR UNKNOWN
    P32 = str
    P33 = str
    P34 = str
    P35 = str
    P36 = str
    #NICKNAME
    P37 = str

def Import():
    dictionary = {}

    for line in uncompress:
        decode = line.decode()
        if decode[0] == "[":
            key = decode[1:-2]
            dictionary[key] = {}
        else:
            lk = list(dictionary)[-1]
            kv = decode.split("=")
            if len(kv) < 2:
                kv.append("")
            dictionary[lk][kv[0]] = kv[1].strip()

    return dictionary

def Rename(dictionary, name):
    print("hello")

def GetName(dictionary):
    ogname = dictionary['custom']['names0']
    translated = ""
    for i in range(0, len(ogname), 2):
        chunk = ogname[i:i+2]
        if chunk != 'AA':
            char = getattr(AlphaNum(), ogname[i:i+2])
            translated = translated + char

    print(translated)

def MaxStats(dictionary, name):
    print("hello")

uncompress = gzip.open("bby2001.c01", mode="rb").readlines()

dictionary = Import()

Rename(dictionary, "hello")
