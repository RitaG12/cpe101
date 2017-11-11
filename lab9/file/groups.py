def groups_of_3(list):
    answer = [ ]
    index = 0
    for i in range(0,len(list), 3):
        for i in range(1,4):
            subList = [ ]
            subList.append(list[index])
            subList.append(list[index+1])
            subList.append(list[index+2])
        answer.append(subList)
    return answer
