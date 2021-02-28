count_occurrences 

def count_occurrences(string):
    
    list_of_chars = []
    
    c = 0
    
    for i in range(len(string)):
        
        if string[i] == string[i+1]:
            c += 1
            if i == len(string):
                   return list_of_chars
                   
        else:                                                                     list_of_chars.append((string[i],c))
            c = 0

                   
    return list_of_chars
        
        
                   
count_occurrences("aaaabbbcca")
            

            