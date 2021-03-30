''' Count occurences of concurrent letters
    aaaa, bbb, cc, a 

    Solution:

                       i 012345678
                         aaabbbcca

'''

def count_occurrences(s):
    print("input will be", s)

    output = []

    count = 1

    for i in range(1, len(s)):
        # compare s[i] with s[i-1]
        if s[i] is s[i-1]:
            count +=1
        else:
            output.append((s[i-1], count))
            count = 1
            
    # very last chacater needs to be added
    output.append((s[-1], count))

    return output


  

if __name__ == '__main__':

   inputarray = "AAAAAABBCCCDDDDDA"
   print(count_occurrences(inputarray))

   inputarray = "AAAAAAAAAAAAAAABBCCCDDDDDAA"
   print(count_occurrences(inputarray))
   
   inputarray = "A"
   print(count_occurrences(inputarray))
            