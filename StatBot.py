
import Api_Functions as api
import tweepy
import re

API_KEY = "whSRUcAWngOzMjx2beMHyrJhJ"
API_SECRET_KEY ="IJGUVjQwyR2YJXleoy8aKsOKtAcwlGGnGGopPpjEfvjWMo6al7"
ACCESS_TOKEN = "1513247611700105216-jOsTHYpVGhhsnQbClPdwnVzG2RTHL9"
ACCESS_SECRET_TOKEN = "vq0GK7l6VOtVygirmmWZfiYFTcZoZfdK0LBQgMVz9hfBT"

auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET_TOKEN)
tweepy_api = tweepy.API(auth)

class Player:
    """
    A class that holds player data
    Attributes:
        first_name (str): player first name
        last_name (str): player last name
        year (str): year of the season
        avg_ppg (double): avg points per game
        avg_reb (double): avg rebounds per game
        avg_ast (dobuble): avg assist per game
        avg_steal (dobule): avg steals per game
        avg_blocks (double): avg blocks per game
        avg_to (dobule): avg turnovers per game
    """
    def __init__(self, fname, lname, year, player_id):
        """
            Initilizes player object:
            Args:
                see documentation
        """
        self.first_name = fname
        self.last_name = lname
        self.year = year
    
        response = api.stat_api(player_id, self.year)
        player_stats = api.get_player_stats(response)
        
        self.avg_pgg = player_stats[0]
        self.avg_reb = player_stats[1]
        self.avg_ast = player_stats[2]
        self.avg_steal = player_stats[3]
        self.avg_blocks = player_stats[4]
        self.avg_to = player_stats [5]
        
        
def parse_mention(tweet):
    """
    parse the mention request from the user
    maybe in regex to get the first name, last name,
    and year.
    Args:
        tweet (str): the request we are getting from the user
    Returns:
        retrun the player first name, last name, and year 
        (year will be a string)
    """
    player_name = re.findall("[A-Z][a-z]+\s[A-Z][a-z]+", tweet)
    name_string = player_name[0]
    name_list = name_string.split()
    fname = name_list[0]
    lname = name_list[1]
    year = re.findall("\d+", tweet)
    
    if fname == "Bron":
        fname = "LeBron"

    return fname, lname, year[0]


def main():
    """
    main driver of the code that initlizies the player class
    grabs the mention tweet and parses it
    tweets back information to the user
    """

bot_id = "1513247611700105216"
mention_id = 1

mentions = tweepy_api.mentions_timeline(count = 1, since_id = mention_id) # If 2 people tweet, count = 1 will only reply/like one of them
for mention in reversed(mentions):
    print("Mention Tweet Found")
    print(f"{mention.author.screen_name} - {mention.text}")
    mention_id = mention.id
  
    # call functions
    fname, lname, year = parse_mention(mention.text)
    player_id = api.get_player_id(fname, lname)
  
    if player_id == "error unable to find player":
        message = f"unable to find player check request for typos @{mention.author.screen_name}"
        tweepy_api.update_status(message, in_reply_to_status_id = mention.id_str)
        print("unable to find player exiting code")
        exit()
    else:
        player = Player(fname, lname, year, player_id)
        message = (f"{player.first_name} {player.last_name} averaged {player.avg_pgg} PPG, " 
                    f"{player.avg_ast} AST, {player.avg_reb} REB, {player.avg_blocks} BLKS, " 
                    f"{player.avg_steal} STL, and {player.avg_to} TO in {year} "
                    f"@{mention.author.screen_name}")
   
    if mention.in_reply_to_status_id is None and mention.author.id != bot_id:
        try:
            print("Attempting Reply...")
            print("Attempting Like...")
            # tweet the player stats back to the requesting user.
            tweepy_api.update_status(message, in_reply_to_status_id = mention.id_str)
            tweepy_api.create_favorite(mention.id)
            print("Successfully replied")
            print("Successfully liked")
        except Exception as exc:
            print("Failed to Reply")
            print("Failed to Like")
            print(exc)

if __name__ == "__main__":
    main()






