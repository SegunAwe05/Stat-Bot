# unit test for stat bot
import Api_Functions as api


# example of correct spelling format
assert api.get_player_id("LeBron", "james") == "265"
assert api.get_player_id("Stephen", "Curry") == "124"
#example of bad player name spelling, official player name is needed
assert api.get_player_id("Lebron", "james") == "error unable to find player"
assert api.get_player_id("Steph", "Curry") == "error unable to find player"


response = api.stat_api("124", "2020")
#Stephen Curry PPG from 2020 = 32
assert api.get_player_stats(response)[0] == 32

response = api.stat_api("265", "2020")
#Lebron James reb per game from 2020 = 7.2
assert api.get_player_stats(response)[1] == 7.2