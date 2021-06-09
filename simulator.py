from spieltage import Phases
from teams import Country
from randomResult import random_result, random_between_0_and_5
import random
from teams import Teams
from groups import groups

class OutcomeProbability:
    team1_probability: float
    team2_probability: float
    remis_probability: float

    def __init__(self, probability1: float, probability2: float):
        self.team1_probability = probability1
        self.team2_probability = probability2
        self.remis_probability = 1 - probability1 - probability2

def tournament_simulator(phases: Phases):
    spieltage = phases.spieltage
    ko_rounds = phases.ko_rounds

    # Group rounds
    for index in range(len(spieltage)):
        print("Tag " + str(index + 1))
        for teams in spieltage[index]:
            play_group_match(teams[0], teams[1])
        print("=====================")
        print("")

    for group in groups.groups: 
        group.determine_winners()

    groups.determine_thirds()
    print("=====================")

    # Ko phase
    teams_for_next_phase = groups
    
    for ko_round_class in ko_rounds:
        ko_round = ko_round_class(teams_for_next_phase)
        spieltage = ko_round.set_spieltage()
        print("")
        print(ko_round.name)
        for teams in spieltage:
            winner = play_ko_match(teams[0], teams[1])
            ko_round.add_winner(winner)
        
        teams_for_next_phase = ko_round.winners

    print("")
    print("Country results")
    for country in Teams.all_teams:
        print("    " + country.name + ": " + str(country.goals) + " goals")
    print("=====================")
    
    print("")
    print("Winner: " + list(map(lambda x: x.name, teams_for_next_phase))[0])        


def play_group_match(team1: Country, team2: Country):
    team1_strength = team1.strength
    team2_strength = team2.strength
    outcome_chances = assign_probabilities(team1_strength, team2_strength)
    winnercode = determine_winner(outcome_chances)
    team1_score = None
    team2_score = None
    if winnercode == 0:
        [team1_score, team2_score] = set_remis_score()
        team1.set_goals_and_points(team1_score, 0)
        team2.set_goals_and_points(team2_score, 0)
    elif winnercode == 1:
        [team1_score, team2_score] = set_score()
        team1.set_goals_and_points(team1_score, 1)
        team2.set_goals_and_points(team2_score, -1)
    elif winnercode == 2:
        [team2_score, team1_score] = set_score()
        team1.set_goals_and_points(team1_score, -1)
        team2.set_goals_and_points(team2_score, 1)
    print("    " + team1.name + " vs. " + team2.name + ": " + str(team1_score) + " : " + str(team2_score))

def play_ko_match(team1: Country, team2: Country):
    team1_strength = team1.strength
    team2_strength = team2.strength
    outcome_chances = assign_probabilities(team1_strength, team2_strength)
    winnercode = determine_winner(outcome_chances)
    team1_score = None
    team2_score = None
    if winnercode == 0:
        [team1_score, team2_score] = set_remis_score()
        [team1_penalty_score, team2_penalty_score] = play_penalty(0, 0)
        team1_total_score = team1_score + team1_penalty_score
        team2_total_score = team2_score + team2_penalty_score
        team1.set_goals_and_points(team1_total_score, 0)
        team2.set_goals_and_points(team2_total_score, 0)
        print("    " + team1.name + " vs. " + team2.name + ": " + str(team1_score) + " : " + str(team2_score) + " (" + str(team1_total_score) + ":" + str(team2_total_score) + ")")
        if team1_total_score > team2_total_score:
            return team1
        else:
            return team2        
    elif winnercode == 1:
        [team1_score, team2_score] = set_score()
        team1.set_goals_and_points(team1_score, 0)
        team2.set_goals_and_points(team2_score, 0)
        print("    " + team1.name + " vs. " + team2.name + ": " + str(team1_score) + " : " + str(team2_score))
        return team1
    elif winnercode == 2:
        [team2_score, team1_score] = set_score()
        team1.set_goals_and_points(team1_score, 0)
        team2.set_goals_and_points(team2_score, 0)
        print("    " + team1.name + " vs. " + team2.name + ": " + str(team1_score) + " : " + str(team2_score))
        return team2

def assign_probabilities(team1_strength: int, team2_strength: int) -> OutcomeProbability:
    probability1, probability2 = convert_strength_to_probabilities(team1_strength, team2_strength)
    outcome_chances = OutcomeProbability(probability1, probability2)
    return outcome_chances

def convert_strength_to_probabilities(team1_strength: int, team2_strength: int) -> list:
    strength_difference = team1_strength - team2_strength

    if strength_difference == -2:
        return [0.1, 0.7]
    elif strength_difference == -1:
        return [0.2, 0.5]
    elif strength_difference == 0:
        return [0.3, 0.3]
    elif strength_difference == 1:
        return [0.5, 0.2]
    elif strength_difference == 2:
        return [0.7, 0.1]

def determine_winner(outcome_chances: OutcomeProbability):
    random_result = random.uniform(0, 1)
    if random_result < outcome_chances.remis_probability:
        return 0
    elif random_result < outcome_chances.remis_probability + outcome_chances.team1_probability:
        return 1
    else:
        return 2

def set_score():
    winner_score = random_result() + 1
    loser_score = random.randint(0, winner_score - 1)
    return winner_score, loser_score

def set_remis_score():
    end_score = random_result()
    return end_score, end_score

def play_penalty(team1_goals: int, team2_goals: int):
    team1_goals = random_between_0_and_5()
    team2_goals = random_between_0_and_5()
    if team1_goals == team2_goals:
        return play_penalty(team1_goals, team2_goals)
    else:
        return team1_goals, team2_goals





if __name__ == "__main__":
    tournament_simulator(Phases)