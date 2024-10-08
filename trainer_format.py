import re

class Team:
    pokemon = str
    nature  = str
    ability = str
    item    = str
    moves   = [str]
    mega    = bool

    def __init__(self, pokemon, nature, ability, item, moves, mega):
        self.pokemon = pokemon
        self.nature  = nature
        self.ability = ability
        self.item    = item
        self.moves   = moves
        self.mega    = mega

class Battle:
    names    = [str]
    optional = bool
    gauntlet = bool
    double   = bool
    teams    = [Team]

    def New(self, name, optional, gauntlet, double, team):
        self.names    = name
        self.optional = optional
        self.gauntlet = gauntlet
        self.double   = double
        self.teams    = team


class Battles:
    info = {}

    def Add(self, location, battle):
        if location not in self.info:
            self.info[location] = [battle]
        else:
            self.info[location].append(battle)

def find_nth(haystack: str, needle: str, n: int) -> int:
    start = haystack.find(needle)
    while start >= 0 and n > 1:
        start = haystack.find(needle, start+len(needle))
        n -= 1
    return start

def CheckTrainer(line):
    try:
        line.index("Lv.")
        yield True
    except ValueError:
        yield False

    try:
        line.index("*")
        yield True
    except ValueError:
        yield False

    try:
        line.index("Double")
        yield True
    except ValueError:
        yield False

def GetLevel(line):
    return line.split(" ")[1]

def GetItem(line):
    m = re.search('@[A-Za-z]+ ?[A-Za-z]+', line)

    if m is None:
        return ""
    else:
        return line.group(0)

def GetPoke(line):
    return line.split(" ")[0]

def GetMoves(line):
    try:
        line.index(",")
    except ValueError:
        return "Default"

    try:
        col = line.index(":") + 2
    except ValueError:
        col = 0

    if col == 0:
        col = find_nth(line, " ", 2) + 1

    e = find_nth(line, "[", 1) - 1
    moves = (line[col:e]).split(",")

    print(moves)

    return [""]

def GetAbility(line):
    return ""

def GetNature(line):
    return ""

def CheckMega(line):
    return True

def CheckB2B(line):
    return True

file    = open("trainer.txt", "r" )
battles = Battles();
trainer = None
loction = ''
flag    = False
b2b     = False
double  = False
team    = []

for line in file.readlines():
    # Check Route and if its in the dictionary
    ## Lazy way is have a bool flag, turn on starting ---, turn off hitting it again ---

    if line.strip():
        if line[0] == "-":
            flag = True if flag == False else False

        if flag == True:
            if line not in battles.info:
                battles.info[line] = []
                curkey = line

        if flag == False:
            chk = CheckTrainer(line)

            if next(chk) == True:
                if trainer is not None:
                    print(line)


                trainer = line
                b2b     = next(chk)
                double  = next(chk)
            else:
                poke    = GetPoke(line)
                lvl     = GetLevel(line)
                item    = GetItem(line)
                moves   = GetMoves(line)
                ability = GetAbility(line)
                nature  = GetNature(line)
                mega    = CheckMega(line)

                team.append(Team(poke, nature, ability, item, moves, mega))

file.close()
