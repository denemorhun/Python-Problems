#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'segments' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING message as parameter.
#

'''
# SMS compliant segment is 160 chars

# if len(sms) < 160, do not generate single messages

# suffix is 5 characters, (x/5), which both suffix and segment must fit in segment

# words are deliminated by space

# do not split words

# space between words should be preserved in the segment until that violates space. space then goes to next segment. 

Can use splicing by python to split messages and append suffix. 
'''

def segments(message):
    lastSpace = 0
    
    currentStart = 0

    output = []
    
    # the number of segments 
    totalSplit = 0
    
    character_count = 0
    
    i = 0
    
    # traverse the message 
    while i < len(message):
        character_count += 1
        
        size = len(message) - 1
        
        # check if last character is space
        if message[i] == ' ':
            lastSpace = i
        
            # segment is 160, however, 5 goes to suffix
            if character_count == 155:
                # if last character is space
                if message[i] != ' ':
                    if (i < len(message) - 1 and message[i+1] == ' ') or i == len(message) - 1:
                        lastSpace = i
                totalSplit += 1
                        
                count = 0
                
                output.append(message[currentStart:lastSpace + 1])
                
                if i > lastSpace:
                    i = lastSpace
                
                currentStart = i + 1
                
            i += 1
            
        # return nessage 
        if currentStart < len(message):
            if totalSplit == 0:
                return [message]
            
            # splice the message by appending the previous section
            output.append(message[currentStart:])
            totalSplit += 1
            
            print(totalSplit)
        # append each suffix to end of each segment 
        for i, segment in enumerate(output):
            
            string = f'{segment} ({i+1}/{totalSplit})'
            
            print(string)
            
            output[i] = f'{segment} ({i+1}/{totalSplit})'
            print (output)
         
    print(len(output))
    return output

print(segments("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi id tristique quam, in ullamcorper metus. Duis lacinia dolor non quam porta, non turpis duis. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi id tristique quam, in ullamcorper metus. Duis lacinia dolor non quam porta, non turpis duis.Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi id tristique quam, in ullamcorper metus. Duis lacinia dolor non quam porta, non turpis duis."))
