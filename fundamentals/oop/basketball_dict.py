#Update the constructor to accept a dictionary with a single player's information instead of individual arguments for the attributes

class Player:
    def __init__(self, player_dict):
        self.name = player_dict["name"]
        self.age = player_dict["age"]
        self.position = player_dict["position"]
        self.team = player_dict["team"]

    def __repr__(self):#prints in terminal in f string form
        return (f"Name - {self.name} Age - {self.age} Position - {self.position} Team - {self.team}")


kevin = {
    "name": "Kevin Durant", 
    "age":34, 
    "position": "Small forward", 
    "team": "Brooklyn Nets"
}
jason = {
    "name": "Jason Tatum", 
    "age":24, 
    "position": "Small forward", 
    "team": "Boston Celtics"
}
kyrie = {
    "name": "Kyrie Irving", 
    "age":32, 
    "position": "Point Guard", 
    "team": "Brooklyn Nets"
}
    
# Create your Player instances here!
# player_jason = ???

player_kevin = Player(kevin)
print(player_kevin)
player_jason = Player(jason)
print(player_jason)
player_kyrie = Player(kyrie)
print(player_kyrie)

#Complete challenge 3: Populate a new list with Player instances from the list of players.
players = [
    {
    "name": "Kevin Durant", 
    "age":34, 
    "position": "small forward", 
    "team": "Brooklyn Nets"
    },
    {
    "name": "Jason Tatum", 
    "age":24, 
    "position": "small forward", 
    "team": "Boston Celtics"
    },
    {
    "name": "Kyrie Irving", 
    "age":32, 
    "position": "Point Guard", 
    "team": "Brooklyn Nets"
    },
    {
    "name": "Damian Lillard", 
    "age":33, 
    "position": "Point Guard", 
    "team": "Portland Trailblazers"
    },
    {
    "name": "Joel Embiid", 
    "age":32, 
    "position": "Power Foward", 
    "team": "Philidelphia 76ers"
    },
    {
    "name": "", 
    "age":16, 
    "position": "P", 
    "team": "en"
    }
]


new_team = []
for val in players:
    player = Player(val)
    new_team.append(player)

print(new_team)