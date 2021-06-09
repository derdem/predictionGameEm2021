from teams import Country, Teams

def sort_points_then_goals(collection):
    return sorted(collection, key=lambda k: (k.points, k.goals), reverse = True)

class Group:
    member1: Country
    member2: Country
    member3: Country
    member4: Country
    first: Country or None
    second: Country or None
    third: Country or None

    
    def determine_winners(self):
        members = [self.member1, self.member2, self.member3, self.member4]
        sorted_members = sort_points_then_goals(members)
        self.first = sorted_members[0]
        self.second = sorted_members[1]
        self.third = sorted_members[2]
        # print(list(map(lambda d: "Name: " + d.name + " Points: " + str(d.points) + " Goals: " + str(d.goals), sorted_members)))

class GroupA(Group):
    member1 = Teams.italy
    member2 = Teams.switzerland
    member3 = Teams.turkey
    member4 = Teams.wales

class GroupB(Group):
    member1 = Teams.belgium
    member2 = Teams.denmark
    member3 = Teams.finland
    member4 = Teams.russia

class GroupC(Group):
    member1 = Teams.netherlands
    member2 = Teams.northmazedonia
    member3 = Teams.ukraine
    member4 = Teams.austria

class GroupD(Group):
    member1 = Teams.england
    member2 = Teams.kroatia
    member3 = Teams.scotland
    member4 = Teams.czechrepublic

class GroupE(Group):
    member1 = Teams.poland
    member2 = Teams.sweden
    member3 = Teams.slowakia
    member4 = Teams.spain

class GroupF(Group):
    member1 = Teams.germany
    member2 = Teams.france
    member3 = Teams.portugal
    member4 = Teams.hungry
class Groups: 
    groups = []
    groups_third = []
    eighth = None
    quarter = None
    half = None
    final = None

    def __init__(self) -> None:
        self.A: Group = self._register(GroupA())
        self.B: Group = self._register(GroupB())
        self.C: Group = self._register(GroupC())
        self.D: Group = self._register(GroupD())
        self.E: Group = self._register(GroupE())
        self.F: Group = self._register(GroupF())

    def _register(self, group: Group) -> Group:
        self.groups.append(group)
        return group

    def determine_thirds(self):
        third_places = []
        for group in self.groups:
            third_places.append(group.third)

        sorted_third_places = sort_points_then_goals(third_places)

        for i in range(4):
            self.groups_third.append(sorted_third_places[i])

        print("Third places top 4")
        for third_place in list(map(lambda d: d.name + " Points: " + str(d.points) + " Goals: " + str(d.goals), self.groups_third)):
            print("    " + third_place)
    
class Eighth:
    name = "Achtelfinale"
    winners = []
    
    def __init__(self, groups: Groups) -> None:
        self.Afirst = groups.A.first
        self.Asecond = groups.A.second
        self.Bfirst = groups.B.first
        self.Bsecond = groups.B.second
        self.Cfirst = groups.C.first
        self.Csecond = groups.C.second
        self.Dfirst = groups.D.first
        self.Dsecond = groups.D.second
        self.Efirst = groups.E.first
        self.Esecond = groups.E.second
        self.Ffirst = groups.F.first
        self.Fsecond = groups.F.second
        self.third1 = groups.groups_third[0]
        self.third2 = groups.groups_third[1]
        self.third3 = groups.groups_third[2]
        self.third4 = groups.groups_third[3]

    def set_spieltage(self):
        return [
            [self.Asecond, self.Bsecond],
            [self.Afirst, self.Csecond],
            [self.Cfirst, self.third1],
            [self.Bfirst, self.third2],
            [self.Dsecond, self.Esecond],
            [self.Ffirst, self.third3],
            [self.Dfirst, self.Fsecond],
            [self.Efirst, self.third4]
        ]

    def add_winner(self, winner: Country):
        self.winners.append(winner)


class Quarter:
    name = "Viertelfinale"
    winners = []

    def __init__(self, teams: list) -> None:
        self.teams = teams

    def set_spieltage(self):
        return [
            [self.teams[5], self.teams[4]],
            [self.teams[3], self.teams[1]],
            [self.teams[2], self.teams[0]],
            [self.teams[7], self.teams[6]],
        ]

    def add_winner(self, winner: Country):
        self.winners.append(winner)

class Half:
    name = "Halbfinale"
    winners = []

    def __init__(self, teams: list) -> None:
        self.teams = teams

    def set_spieltage(self):
        return [
            [self.teams[0], self.teams[1]],
            [self.teams[2], self.teams[3]],
        ]

    def add_winner(self, winner: Country):
        self.winners.append(winner)

class Final:
    name = "Finale"
    winners = []

    def __init__(self, teams: list) -> None:
        self.teams = teams

    def set_spieltage(self):
        return [
            [self.teams[0], self.teams[1]],
        ]

    def add_winner(self, winner: Country):
        self.winners.append(winner)

groups = Groups()

