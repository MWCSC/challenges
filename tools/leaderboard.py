# Script to generate main leaderboar

from os import listdir # import os
from os.path import isfile, join # import other stuff needed

# create arrays to hold the names of the successful people
advanced_names = []
intermediate_names = []

def formatFile(strings, team): # function creates a string to be written to file
    final = [] # final list, each item in list is a line in file

    final.append(f'# {team} Leaderboard\n') # add the boilerplate
    final.append('|Name|Score|\n')
    final.append('|----|-----|\n')

    for string in strings: # loop through all the strings being sent into the function, Ex: 'slate:6'
        name = string.split(':')[0]
        score = string.split(':')[1].rstrip()
        final.append(f'|{name}|{score}|\n') # add the name and score to the md table

    return final # return the final array

def getScore(string): # get score from the string, Ex: 'slate:6' would return 6
    return string.split(':')[1].strip('\n')

def calculateScore(team): # do all the calculating stuff
    with open(f'../{team}-leaderboard.md', 'r') as main: # read the stuff, i dont know why this is here, maybe we can remove it?
        main_lines = main.readlines()

    new_names = [] # add unique names to this array
    new_lines = [] # add unformated string to this array, Ex: 'slate:6'

    if team == 'advanced': # assign the team array based on the incoming parameter
        team_names = advanced_names
    elif team == 'intermediate':
        team_names = intermediate_names

    for name in team_names: # get the score based on the number of times a persons name appears in their team's array
        score = team_names.count(name)

        if name not in new_names: # if the name is unique, add it to the array and append it to the unformatted strings array
            new_names.append(name)
            new_lines.append(f"{name}:{score}\n")


    with open(f'../{team}-leaderboard.md', 'w') as new: # open the leaderboard file for that specific team
        sorted_scores = sorted(new_lines, key=getScore, reverse=True) # sort the scores based on the string, Ex: 'slate:6' would come before 'slatedev:3'
        final_file = formatFile(sorted_scores, team.title()) # use formatFile function to get the final file
        new.write(''.join(final_file)) # write the file
        new.close() # close file to avoid random errors



advanced_days_path = '../advanced/days/' # assign the paths to the teams days
intermediate_days_path = '../intermediate/days/'

for folder in listdir(advanced_days_path): # go thru each day
    for file in listdir(advanced_days_path + folder): # get each file from within the day
        if file == 'leaderboard.txt': # get the leaderboard file
            with open(advanced_days_path + folder +"/"+ file,'r') as leaderboard:# open the file and read each line
                lines = leaderboard.readlines()
                for line in lines:
                    if '✅' in line: # see who was successful
                        name = line.split(' ') # get the name of the succesful person
                        advanced_names.append(name[0]) # append their name to their teams array

            calculateScore('advanced') # once done the above, calculate the score
        else:
            continue

# do the same thing as above, but for intermediates

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
