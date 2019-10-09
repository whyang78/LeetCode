"""
def canCompleteCircuit(gas, cost):
    for i in range(len(gas)):
        if gas[i] > cost[i]:
            index = i
            break

    com = gas[index] - cost[index] + gas[index+1]
    if index+1 < len(gas)-1:
        if com > cost[index+1]:
            index += 1
        for i in range(index+1):
            com = gas[index] - cost[index] + gas[index+1]
            if com > cost[index]:
                continue
            if i == index:
                return index
            else:
                return -1
"""
def canCompleteCircuit(gas, cost):
    if gas == []:
        return -1
    ind, minv, s = 0, gas[0] - cost[0], gas[0] - cost[0]
    for i in range(1, len(gas)):
        s += gas[i] - cost[i]
        if s < minv:
            minv, ind = s, i
    # check ind
    ind = (ind + 1) % len(gas)
    s = gas[ind] - cost[ind]
    for i in range(1, len(gas) + 1):
        j = (ind + i) % len(gas)
        if s < 0:
            return -1
        s += gas[j] - cost[j]
    return ind