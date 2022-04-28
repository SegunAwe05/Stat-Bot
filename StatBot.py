
import Api_Functions as api
import tweepy

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
    pass


def main():
    """
    in this function we want to have a infitie while loop 
    so the bot is running while the program is running.
    We then want to iterite throught the account mentions 
    if its greater than 0.
    For each mention which will be a request from another account
    we want to read their request, parse it to get the information we need, 
    pass the information into the player object, then tweet back
    the stats of the player.
    """

    mentions = tweepy_api.mentions_timeline(tweet_mode = "exteneded")
    while mentions > 0:
        for mention in reversed(mentions):
            player_info = parse_mention()
            player_info = Player()
            tweepy_api.update_status("@" + mention.user.screen_name + player_info, mention.id)



    
    pass

if __name__ == "__main__":
 
    main()

