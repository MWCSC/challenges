# Script to generate main leaderboard

from os import listdir
from os.path import isfile, join

advanced_names = []
intermediate_names = []

def formatFile(strings, team):
    final = []

    final.append(f'# {team} Leaderboard\n')
    final.append('|Name|Score|\n')
    final.append('|----|-----|\n')

    for string in strings:
        name = string.split(':')[0]
        score = string.split(':')[1].rstrip()
        final.append(f'|{name}|{score}|\n')

    return final

def getScore(string):
    return string.split(':')[1].strip('\n')

def calculateScore(team):
    with open(f'../{team}-leaderboard.md', 'r') as main:
        main_lines = main.readlines()

    new_names = []
    new_lines = []

    if team == 'advanced':
        team_names = advanced_names
    elif team == 'intermediate':
        team_names = intermediate_names

    for name in team_names:
        score = team_names.count(name)

        if name not in new_names:
            new_names.append(name)
            new_lines.append(f"{name}:{score}\n")


    with open(f'../{team}-leaderboard.md', 'w') as new:
        sorted_scores = sorted(new_lines, key=getScore, reverse=True)
        final_file = formatFile(sorted_scores, team.title())
        new.write(''.join(final_file))
        new.close()



advanced_days_path = '../advanced/days/'
intermediate_days_path = '../intermediate/days/'

for folder in listdir(advanced_days_path):
    for file in listdir(advanced_days_path + folder):
        if file == 'leaderboard.txt':
            with open(advanced_days_path + folder +"/"+ file,'r') as leaderboard:
                lines = leaderboard.readlines()
                for line in lines:
                    if '✅' in line:
                        name = line.split(' ')
                        advanced_names.append(name[0])

            calculateScore('advanced')
        else:
            continue

for folder in listdir(intermediate_days_path):
    for file in listdir(intermediate_days_path + folder):
        if file == 'leaderboard.txt':
            with open(intermediate_days_path + folder +"/"+ file, 'r') as leaderboard:
                lines = leaderboard.readlines()
                for line in lines:
                    if '✅' in line:
                        name = line.split(' ')
                        intermediate_names.append(name[0])

            calculateScore('intermediate')
        else:
            continue
