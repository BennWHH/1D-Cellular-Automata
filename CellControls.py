def stateBasedOnNeighbors(rule, left, curr, right):
    if left == 1 and curr == 1 and right == 1:
        return rule[0]
    elif left == 1 and curr == 1 and right == 0:
        return rule[1]
    elif left == 1 and curr == 0 and right == 1:
        return rule[2]
    elif left == 1 and curr == 0 and right == 0:
        return rule[3]
    elif left == 0 and curr == 1 and right == 1:
        return rule[4]
    elif left == 0 and curr == 1 and right == 0:
        return rule[5]
    elif left == 0 and curr == 0 and right == 1:
        return rule[6]
    elif left == 0 and curr == 0 and right == 0:
        return rule[7]

def newGeneration(rule, currentCellStates, generations):
    nextCellStates = [0] * len(currentCellStates)
    for i in range(generations):
        for i in range(len(currentCellStates)):
            if i == 0:
                left = currentCellStates[len(currentCellStates)-1]
            else:
                left = currentCellStates[i-1]

            curr = currentCellStates[i]

            if i == len(currentCellStates)-1:
                right = currentCellStates[0]
            else:
                right = currentCellStates[i+1]

            nextCellStates[i] = stateBasedOnNeighbors(rule, left, curr, right)
        for i in range(len(currentCellStates)):
            currentCellStates[i] = nextCellStates[i]
        print(currentCellStates)
    return currentCellStates