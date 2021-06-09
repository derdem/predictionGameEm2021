class Country:
    strength = None
    name = ""
    points = 0
    goals = 0

    def __init__(self, name, strength) -> None:
        self.name = name
        self.strength = strength

    def set_goals_and_points(self, goals: int, outcome: int):
        self.setPoints(outcome)
        self.goals += goals

    def setPoints(self, outcome: int):
        remis = 0
        winner = 1
        if outcome == remis:
            self.points += 1
        elif outcome == winner:
            self.points += 3

    
        

class Teams: 
    italy = Country("Italy", 3)
    switzerland = Country("Switzerland", 2)
    turkey = Country("Turkey", 2)
    wales = Country("Wales", 1)
    belgium = Country("Belgium", 2)
    denmark = Country("Denmark", 2)
    finland = Country("Finland", 1)
    russia = Country("Russia", 2)
    netherlands = Country("Netherlands", 3)
    northmazedonia = Country("Northmazedonia", 1)
    ukraine = Country("Ukraine", 1)
    austria = Country("Austria", 2)
    england = Country("England", 3)
    kroatia = Country("Kroatia", 2)
    scotland = Country("Scotland", 2)
    czechrepublic = Country("Czech Republic", 2)
    poland = Country("Poland", 2)
    sweden = Country("Sweden", 2)
    slowakia = Country("Slowakia", 1)
    spain = Country("Spain", 3)
    germany = Country("Germany", 3)
    france = Country("France", 3)
    portugal = Country("Portugal", 3)
    hungry = Country("Hungry", 1)

    all_teams = [
        italy, 
        switzerland, 
        turkey, 
        wales, 
        belgium, 
        denmark, 
        finland, 
        russia, 
        netherlands, 
        northmazedonia, 
        ukraine, 
        austria, 
        england, 
        kroatia, 
        scotland,
        czechrepublic,
        poland,
        sweden,
        slowakia,
        spain,
        germany,
        france,
        portugal,
        hungry
    ]

