import json
import player

#Store player records in <player id> : Player() pairs.
tracked_players = {}

def load_records(bot, filename):
    """Loads player records from player_records.json
    into tracked_players.

    keyword arguments:
    bot -- Bot object
    """
    global tracked_players
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
            for id in data:
                tracked_players[id] = player.Player()
                user = await bot.get_user_info(id)
                tracked_players[id].id = id
                tracked_players[id].name = user.name
                tracked_players[id].discriminator = user.discriminator
                tracked_players[id].score = data[id]["score"]
                tracked_players[id].wins = data[id]["wins"]
    #Need to make this more detailed/informative
    except:
        print('Error loading player records.')
        exit()

def update_records(filename):
    """Updates player_records.json from tracked_players
    dictionary

    keyword arguments:
    bot -- Bot object
    """
    global tracked_players
    data = {}
    with open(filename,'w') as f:
        for player in tracked_players:
            data[player] = (
                {"score": tracked_players[player].score,
                "wins": tracked_players[player].wins}
            )
        json.dump(data,f)

class Game(object):
    pass