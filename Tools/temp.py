#stats handler
def user_stats(user: str) -> None:
    with open('/home/studente418/VSCodeProjects/Tools/Wordle/wordle_stats.txt', 'r') as f:
        lines=f.readlines()
    profile_name, games_won, games_lost, winrate, current_streak, max_streak, won_last_game=lines[0][9:-1], int(lines[1][11:-1]), int(lines[2][12:-1]), int(lines[3][9:-2]), int(lines[4][20:-1]), int(lines[5][16:-1]), int(lines[6])
    print(profile_name, games_won, games_lost, winrate, current_streak, max_streak, won_last_game)
    with open('/home/studente418/VSCodeProjects/Tools/Wordle/wordle_stats.txt', 'w') as f:
        f.seek(0)
        pass
def print_user_stats(user: str) -> None:
    with open('/home/studente418/VSCodeProjects/Tools/Wordle/wordle_stats.txt', 'r') as f:
        pass

user_stats('a')



# Profile: Gabriel
# Games won: 0
# Games lost: 0
# Winrate: 0%
# Current win streak: 0
# Max win streak: 0
# False