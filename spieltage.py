from groups import groups, Eighth, Quarter, Half, Final

spieltag1 = [
    [groups.A.member3, groups.A.member1],
    [groups.A.member4, groups.A.member2],
    [groups.B.member2, groups.B.member3],
    [groups.B.member1, groups.B.member4],
    [groups.D.member1, groups.D.member2],
    [groups.C.member4, groups.C.member2],
    [groups.C.member1, groups.C.member3],
]

spieltag2 = [
    [groups.D.member3, groups.D.member4],
    [groups.E.member1, groups.E.member3],
    [groups.E.member4, groups.E.member2],
    [groups.F.member4, groups.F.member3],
    [groups.F.member2, groups.F.member1],
]

spieltag3 = [
    [groups.B.member3, groups.B.member4],
    [groups.A.member3, groups.A.member4],
    [groups.A.member1, groups.A.member2],
    [groups.C.member3, groups.C.member2],
    [groups.B.member2, groups.B.member1],
    [groups.C.member1, groups.C.member4],
]

spieltag4 = [
    [groups.E.member2, groups.E.member3],
    [groups.D.member2, groups.D.member4],
    [groups.D.member1, groups.D.member3],
    [groups.F.member4, groups.F.member2],
    [groups.F.member3, groups.F.member1],
    [groups.E.member4, groups.E.member1],
]

spieltag5 = [
    [groups.A.member1, groups.A.member4],
    [groups.A.member2, groups.A.member3],
    [groups.C.member3, groups.C.member4],
    [groups.C.member2, groups.C.member1],
    [groups.B.member4, groups.B.member2],
    [groups.B.member3, groups.B.member1],
]

spieltag6 = [
    [groups.D.member2, groups.D.member3],
    [groups.D.member4, groups.D.member1],
    [groups.E.member3, groups.E.member4],
    [groups.E.member2, groups.E.member1],
    [groups.F.member3, groups.F.member2],
    [groups.F.member1, groups.F.member4],
]


spieltage = [
    spieltag1,
    spieltag2,
    spieltag3,
    spieltag4,
    spieltag5,
    spieltag6,
]

ko_rounds = [
    Eighth,
    Quarter,
    Half,
    Final
]

class Phases:
    spieltage = spieltage
    ko_rounds = ko_rounds
