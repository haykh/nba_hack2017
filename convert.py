import numpy as np

import csv

def team2teamID(team):
    rootdir = '/Users/hayk/Desktop/NBA_hack2017/Basketball Data-selected/'
    fname = rootdir + 'Team_Map.csv'

    with open(fname, 'rb') as csvfile:
        csvfile = csv.reader(csvfile, delimiter=',')
        first = True
        for row in csvfile:
            if first:
                first = False
                continue
            else:
                if row[-1] == team:
                    return row[1]
def team2VUteamID(team):
    rootdir = '/Users/hayk/Desktop/NBA_hack2017/Basketball Data-selected/'
    fname = rootdir + 'Team_Map.csv'

    with open(fname, 'rb') as csvfile:
        csvfile = csv.reader(csvfile, delimiter=',')
        first = True
        for row in csvfile:
            if first:
                first = False
                continue
            else:
                if row[-1] == team:
                    return row[0]

def teamID2team(team_id):
    rootdir = '/Users/hayk/Desktop/NBA_hack2017/Basketball Data-selected/'
    fname = rootdir + 'Team_Map.csv'

    with open(fname, 'rb') as csvfile:
        csvfile = csv.reader(csvfile, delimiter=',')
        first = True
        for row in csvfile:
            if first:
                first = False
                continue
            else:
                if row[1] == team_id:
                    return row[-1]
def VUteamID2team(vu_team_id):
    rootdir = '/Users/hayk/Desktop/NBA_hack2017/Basketball Data-selected/'
    fname = rootdir + 'Team_Map.csv'

    with open(fname, 'rb') as csvfile:
        csvfile = csv.reader(csvfile, delimiter=',')
        first = True
        for row in csvfile:
            if first:
                first = False
                continue
            else:
                if row[0] == vu_team_id:
                    return row[-1]

def teamsPlayed(player_id):
    root = '/Users/hayk/Desktop/NBA_hack2017/Basketball Data-selected/'
    pbox = 'Player_Boxscores.csv'

    fname = root + pbox
    teams_played = []
    with open(fname, 'rb') as csvfile:
        csvfile = csv.reader(csvfile, delimiter=',')
        first = True
        for row in csvfile:
            if first:
                person_ind = row.index('Person_id')
                team_ind = row.index('Team_id')
                first = False
                continue
            else:
                if row[person_ind] == player_id:
                    if not row[team_ind] in teams_played:
                        teams_played.append(row[team_ind])
    return teams_played

def findAllPlayerID(season):
    root = '/Users/hayk/Desktop/NBA_hack2017/Basketball Data-selected/'
    pbox = 'Player_Boxscores.csv'

    fname = root + pbox
    players = []
    with open(fname, 'rb') as csvfile:
        csvfile = csv.reader(csvfile, delimiter=',')
        first = True
        for row in csvfile:
            if first:
                person_ind = row.index('Person_id')
                season_ind = row.index('Season')
                season_type_ind = row.index('Season_Type')
                first = False
                continue
            else:
                if row[season_ind] == season:
                    if row[season_type_ind] == 'Regular':
                        if not row[person_ind] in players:
                            players.append(row[person_ind])
    return players
