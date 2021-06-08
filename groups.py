from teams import Country, Teams

class Group:
    member1: Country
    member2: Country
    member3: Country
    member4: Country
    first: Country or None
    second: Country or None

    @staticmethod
    def determine_winners(group):
        members = [group.member1, group.member2, group.member3, group.member4]
        sorted_members = sorted(members, key=lambda k: k.points, reverse = True) 
        print(list(map(lambda d: "Name: " + d.name + " Points: " + str(d.points) + " Goals: " + str(d.goals), sorted_members)))

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

groups = [
    GroupA,
    GroupB,
    GroupC,
    GroupD,
    GroupE,
    GroupF
]