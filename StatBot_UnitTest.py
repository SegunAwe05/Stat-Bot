# unit test for stat bot

import Api_Functions as api
import StatBot as sb
import tweepy

# example of correct spelling format
assert api.get_player_id("LeBron", "james") == "265"
assert api.get_player_id("Stephen", "Curry") == "124"

#example of bad player name spelling, official player name is needed
assert api.get_player_id("Lebron", "james") == "error unable to find player"
assert api.get_player_id("Steph", "Curry") == "error unable to find player"

#API request of status code 200 is good
response = api.stat_api("124", "2020")
assert response.status_code == 200 

#Stephen Curry PPG from 2020 = 32
assert api.get_player_stats(response)[0] == 32


#API request of status code 200 is good
response = api.stat_api("265", "2020")
assert response.status_code == 200 

#Lebron James reb per game from 2020 = 7.2
assert api.get_player_stats(response)[1] == 7.2

#More than 0 mentioned tweets
mentions = tweepy.mentions_timeline()
assert mentions > 0
print(len(mentions) + " number of mentioned tweets")

#No mentioned tweets
mentions = tweepy.mentions_timeline()
assert mentions == 0, "There are no mentioned tweets"

# testing if names are parsed
tweet = "Kevin Durant 2021"
assert sb.parse_mention(tweet)[0] == "Kevin"
assert sb.parse_mention(tweet)[1] == "Durant"
assert sb.parse_mention(tweet)[2] == "2020"