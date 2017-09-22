import re
import os
import time
import xml.etree.ElementTree as ET
import csv
import numpy as np

def getTrack(game_id, quater, time_1, time_2):
    root = '/Users/hayk/Desktop/NBA_hack2017/Basketball Data-selected/'
    track_root = root + 'tracking_data/trackdata/'

    def _get_game_track():
        tree = ET.parse('{}NBA_LG_FINAL_SEQUENCE_OPTICAL${}_{}.XML'.format(track_root, game_id, quater))
        ball_re = re.compile('-1\,-1\,(\-?\d*\.*\d*)\,(\-?\d*\.*\d*)\,(\-?\d*\.*\d*)')
        crd_re = re.compile('\d+\,\d{3,}\,(\-?\d*\.*\d*)\,(\-?\d*\.*\d*)\,0')
        team_re = re.compile('\\;(\d+)')
        player_re = re.compile('\\,(\d{3,})\\,')
        root = tree.getroot()
        for neighbor in root.iter('moment'):
            game_clock = neighbor.get('game-clock')
            shot_clock = neighbor.get('shot-clock')
            g_time = neighbor.get('time')
            game_event_id = neighbor.get('game-event-id')

            data = neighbor.get('locations')

            teams = team_re.findall(data)
            players = player_re.findall(data)
            ball = ball_re.findall(data)
            if ball != []:
                ball = ball[0]
                ball = map(float, ball)
            coords = crd_re.findall(data)
            coords = np.reshape(coords, (len(players), 2))
            coords = [map(float, coord) for coord in coords]
            yield float(game_clock), float(shot_clock), int(g_time), game_event_id, zip(teams, players, coords), ball
    data = {'game-clock': [],
            'shot-clock': [],
            'time': [],
            'game-event-id': [],
            'ball': [],
            'players': []
            }
    for game_clock, shot_clock, g_time, game_event_id, crds_raw, ball in _get_game_track():
        if game_clock < time_1 and game_clock > time_2:
            data['game-clock'].append(game_clock)
            data['shot-clock'].append(shot_clock)
            data['time'].append(g_time)
            data['game-event-id'].append(game_event_id)
            data['ball'].append(ball)
            data['players'].append(crds_raw)
    return data

def getStatisticsPlayer(season, game_id, person_id, fname, parameters):
    rootdir = '/Users/hayk/Desktop/NBA_hack2017/Basketball Data-selected/NBAPlayerTrackingData_2014-17/'
    fname = "{}{}_{}.txt".format(rootdir, season, fname)

    with open(fname, 'rb') as csvfile:
        csvfile = csv.reader(csvfile, delimiter='\t')
        first = True
        for row in csvfile:
            if first:
                person_ind = row.index('PERSON_ID')
                game_ind = row.index('GAME_ID')
                param_ind = [row.index(param) for param in parameters]
                first = False
            else:
                if row[person_ind] == person_id and row[game_ind] == game_id:
                    return [row[ind] for ind in param_ind]

def getStatisticsTeam(season, game_id, team_id, fname, parameters):
    rootdir = '/Users/hayk/Desktop/NBA_hack2017/Basketball Data-selected/NBAPlayerTrackingData_2014-17/'
    fname = "{}{}_{}.txt".format(rootdir, season, fname)

    with open(fname, 'rb') as csvfile:
        csvfile = csv.reader(csvfile, delimiter='\t')
        first = True
        found = False
        team_data = np.zeros(len(parameters))
        for row in csvfile:
            if first:
                team_ind = row.index('TEAM_ID')
                game_ind = row.index('GAME_ID')
                param_ind = [row.index(param) for param in parameters]
                first = False
            else:
                if row[team_ind] == team_id and row[game_ind] == game_id:
                    team_data += np.array([float(row[ind]) for ind in param_ind])
                    found = True
                if found and row[game_ind] != game_id:
                    return team_data
        return team_data
