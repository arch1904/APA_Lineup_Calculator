import itertools
from pprint import pprint

team = ["Archit", "Allan", "Jack", "Kyra", "Brooke", "Parth", "Neil", "Risalat"]
nine_ball_SL = {"Archit" : 4, "Allan" : 7, "Jack" : 4, "Kyra"  : 1, "Brooke"  : 3 , "Parth" : 2, "Neil" : 4, "Risalat" : 5}
eight_ball_SL = {"Archit" : 5, "Allan" : 6, "Jack" : 4, "Kyra"  : 3, "Brooke"  : 3 , "Parth" : 6, "Neil" : 5, "Risalat" : 6}
MAX_SL_SUM = 23
MAX_LINEUP = 5

def generate_team_combos(team, x_ball_SL):
    possible_lineups = []
    for comb in itertools.combinations(team, MAX_LINEUP):
        possible_lineups.append(comb)
    sl_restricted_lineups = []
    for lineup in possible_lineups:
        sum = 0
        for player in lineup:
            sum += x_ball_SL[player]
        if sum <= MAX_SL_SUM:
            sl_restricted_lineups.append(lineup)

    return sl_restricted_lineups

pprint(generate_team_combos(team, nine_ball_SL))