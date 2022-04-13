
import requests
import json

## get player ID
def get_player_id(first_name, last_name):
    """
    gets player ID from API
    
    Args:
        first_name (str): Player first name
        last_name (str): Player last name
    Returns:
        the player id in string Ex "124"
         
    """
    
    url = "https://api-nba-v1.p.rapidapi.com/players"

    querystring = {"search":last_name}
    headers = {
	    "X-RapidAPI-Host": "api-nba-v1.p.rapidapi.com",
	    "X-RapidAPI-Key": "1743d88febmsh05b21d50c3a6e02p118d8djsnb38c4acc127e"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    data = json.loads(response.text)
    
    player_dict = dict()
    for key, val in data.items():
        if key == "response":
            # val is has become a list
            for index in val:
                for item, item_data in index.items():
                    if first_name == item_data:
                        player_dict = dict(index)
                        break
    
    if player_dict:
        for key, val in player_dict.items():
            if key == "id":
                player_id = val
        return str(player_id)
    else:
        return "error unable to find player"
    

def stat_api(id, year):
    """
    Gets stat information for player using player id
    
    Args:
        id (str): player id
        year (str) year of the season Ex "2020"
    Returns:
        response - All the data from the API call
    """
    

    url = "https://api-nba-v1.p.rapidapi.com/players/statistics"
    querystring = {"id":id,"season":year}

    headers = {
	    "X-RapidAPI-Host": "api-nba-v1.p.rapidapi.com",
	    "X-RapidAPI-Key": "1743d88febmsh05b21d50c3a6e02p118d8djsnb38c4acc127e"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    return response


def get_player_stats(api_response):
    """
    Calcualtes the avergages of a player stat
    Args:
        api_resoonse (str): the data from the api call
    returns:
        All of the stats in a tuple 
    """

    json_data = json.loads(api_response.text)
    points = 0
    reb = 0
    ast = 0
    steal = 0
    blocks = 0
    turnovers = 0
    game_count = 0

    for key, val in json_data.items():
        if key == "response":
            for line in val:
                for stat, data in line.items():
                    if stat == "points":
                        if data == None:
                            continue
                        else:
                            points += data
                            
                    if stat == "totReb":
                        if data == None:
                            continue
                        else:
                            reb += data
                    
                    if stat == "blocks":
                        if data == None:
                            continue
                        else:
                            blocks += data
                        
                    if stat == "assists":
                        if data == None:
                            continue
                        else:
                            ast += data
                    
                    if stat == "steals":
                        if data == None:
                            continue
                        else:
                            steal += data
                    
                    if stat == "turnovers":
                        if data == None:
                            continue
                        else:
                            turnovers += data
                        game_count += 1    

                    
    avg_ppg = points / game_count
    avg_reb = reb / game_count
    avg_steal = steal / game_count
    avg_ast = ast / game_count
    avg_blocks = blocks / game_count
    avg_to = turnovers / game_count
    
    return round(avg_ppg), round(avg_reb, 1), round(avg_ast), round(avg_steal), round(avg_blocks, 1), round(avg_to)
