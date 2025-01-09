def solution(skill, skill_trees):
    count = 0
    inList = []
    for i in range(len(skill_trees)) :
        temp = []
        for j in range(len(skill_trees[i])) :
            if skill_trees[i][j] in skill :
                temp.append(skill_trees[i][j])
        inList.append(temp)

    for i in range(len(inList)) :
        temp = ''.join(inList[i])
        if len(inList[i]) == len(skill) :
            if temp == skill :
                count += 1
        else :
            print(skill[:len(temp)])
            if temp == skill[:len(temp)] :
                count += 1
    return count