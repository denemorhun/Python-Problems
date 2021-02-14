''' competitoins '''

# Hint: we only need to keep track of winners

def tournamentWinner(competitions, results):
	
	winners = {}
    # Competitions and results have equal length. 
	for i in range(len(competitions)):
	# capture away or home team as winner
        if results[i] == 0:
            r = 1
        else:
            r = 0
        
        print('r', r)
        
        winner = competitions[i][r] 
        
        print(f'winner of {i}th game ', winner)
		
		# if winner present in table increment by 3 pts
        if winner in winners.keys():
			winners[winner] += 3
		# if winner absent initialize with 3 pts
        else:
			winners[winner] = 3
			
	print(*winners, *winners.values())
		
	# find team with largest accumulation of pts
	v = max(winners, key=winners.get)

	return v




if __name__ == '__main__':
    input = {"competitions": [["HTML", "C#"], ["C#", "Python"], ["Python", "HTML"]],
  "results": [0, 0, 1]}

    result = tournamentWinner(input["competitions"], input["results"])

    print('The winner is, ' + result)
        
        
