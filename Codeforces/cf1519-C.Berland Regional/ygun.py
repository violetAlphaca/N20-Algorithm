from pprint import pprint as pp

# TLE @case5
T = int(input())

for t in range(T):
    n = int(input())
    univOfStudents = []
    skillOfStudents = []
    univs = {}
    skillForUnivs = {}  # index: univ, value: [skillOfStudents]
    # get univOfStudents
    univOfStudents = list(map(int, input().split()))

    # get skillOfStudents for univOfStudents
    skillOfStudents = list(map(int, input().split()))

    for i in range(n):
        if univOfStudents[i] not in skillForUnivs:
            skillForUnivs[univOfStudents[i]] = {"skills": [], "acc": [0]}
        if univOfStudents[i] not in univs:
            univs[univOfStudents[i]] = True
        skillForUnivs[univOfStudents[i]]["skills"].append(skillOfStudents[i])

    # sort
    for univ in univs:
        skillForUnivs[univ]["skills"].sort(reverse=True)
        for studentSkill in skillForUnivs[univ]["skills"]:
            skillForUnivs[univ]["acc"].append(
                studentSkill + skillForUnivs[univ]["acc"][-1])

    # get answer list for each size
    for size in range(1, n+1):
        localAns = 0
        for univ in univs:
            totalStudents = len(skillForUnivs[univ]["skills"])
            localAns += skillForUnivs[univ]["acc"][totalStudents // size * size]
        print(localAns, end=' ')
    print('')
