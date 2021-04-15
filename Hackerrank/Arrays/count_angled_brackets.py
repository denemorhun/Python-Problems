# Balance angle brackets

def solution(angles):

    openCount = 0
    closedCount = 0

    for b in angles: 
        if b == '>':
            if openCount == 0:
                closedCount += 1
                
            else:
                openCount -= 1
    
        else:
            openCount += 1

    print('closedCount', closedCount)
    print('openCount', openCount)        

    angles = list(angles)

    for i in range(openCount):
        angles.append( '>')
    
    for i in range(closedCount):
        angles.insert(0, '<')
            
    print (angles)

    return "".join(angles)





print(solution('<<<<>>'))
print(solution('<<<<'))
print(solution('>>>>'))