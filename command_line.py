from pprint import pprint
import sys

from api_requests import ClubAPI, GameAPI, PlayerAPI

action = sys.argv[1]
flag = sys.argv[2]

if action == 'clubs':
    pprint(ClubAPI().get_club_by_name(flag))

if action == 'players':
    pprint(PlayerAPI().get_players(flag))

if action == 'games':
    pprint(GameAPI().get_games())