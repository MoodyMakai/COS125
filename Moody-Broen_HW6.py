#Makai Moody-Broen, HW6
#help from Troy
teams = []
teamsID = []
list = []
playerID = []
players = []
Hstats = []
TwoStat = []
ThreeStat = []
HRstat = []
ABstat = []
PepToSLG = []
wins = []
losses = []
teamYear = str(input('Proved a year between 1871 and 2020\n'))
def main():
    with open('/Users/makaimoody-broen/Downloads/Teams.csv', 'r') as r:
        data = r.read()
        data = data.split('\n')
        for x in data:
            r = x.strip().split(',')
            if r[0] == teamYear:
                teams.append(r[40])
                teamsID.append(r[2])
    Tselect()
    BIDselect()
    PEOselect()
    slugStat()
    write()

def Tselect():
    j=0
    for x in teams:
        j=j+1            
        print(f'{j}:{x}')
    num = int(input('Select a number:  '))
    global team
    team = teamsID[num-1]
    with open('/Users/makaimoody-broen/Downloads/Teams.csv', 'r') as r:
        data = r.read()
        data = data.split('\n')
        for x in data:
            r = x.strip().split(',')
            try:
                if r[0] == teamYear and r[2] == team:
                    wins.append(r[8])
                    losses.append(r[9])
            except:
                pass

def BIDselect():
    with open('/Users/makaimoody-broen/Downloads/Batting (1).csv','r') as r:
        data = r.read()
        data = data.split('\n')
        for x in data:
            r = x.strip().split(',')
            try:
                if r[1] == teamYear and r[3] == team:
                    playerID.append(r[0])
                    Hstats.append(int(r[8]))
                    TwoStat.append(int(r[9]))
                    ThreeStat.append(int(r[10]))
                    HRstat.append(int(r[11]))
                    ABstat.append(int(r[6]))
            except IndexError:
                pass

def PEOselect():
    with open('/Users/makaimoody-broen/Downloads/People.csv','r') as r:
        data = r.read()
        data = data.split('\n')
        for x in data:
            r = x.strip().split(',')
            for y in playerID:
                if y == r[0]:
                    players.append(r[15])

def slugStat():
    for x in range(len(playerID)):
        if ABstat[x] == 0:
            PepToSLG.append('DIV BY 0 ERR')
        else:
            slg = (Hstats[x]+(TwoStat[x]*2)+(ThreeStat[x]*3)+(HRstat[x]*4))/ABstat[x]
            PepToSLG.append(slg)

def write():
    with open(f'{teamYear}_and_{team}.txt', 'w') as w:
        w.write(f'The {str(wins[0])}-{str(losses[0])} {team} {teamYear} Roster:\n')
        for x in range(len(players)):
            w.write(f'Player: {players[x]}\nSlugging AVG: {PepToSLG[x]:.3}\n')
    print(f'The {team} {teamYear} roster has been written to file: {teamYear}_and_{team}.txt')
        
main()


