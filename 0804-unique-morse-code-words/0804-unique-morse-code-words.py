#   Created by Elshad Karimov on 23/04/2020.
#   Copyright © 2020 AppMillers. All rights reserved.

#  How to create a Tuple?

newTuple = ('a', 'b', 'c', 'd', 'e')
newTuple1 = tuple('abcde')

print(newTuple1)

# Access Tuple elements

print(newTuple[0]) 


#  Traverse through tuple

for i in newTuple:
    print(i)


for index in range(len(newTuple)):
    print(newTuple[index])


#  How to search for an element in Tuple?

print('a' in newTuple)

def searchInTuple(pTuple, element):
    for i in pTuple:
        if i == element:
            return pTuple.index(i)
    return 'The element does not exist'

print(searchInTuple(newTuple, 'a'))

# Tuple Operations / Functions
myTuple = (1,4,3,2,5)
myTuple1 = (1,2,6,9,8,7)

print(myTuple + myTuple1) 
print(myTuple * 4)      
print(2 in myTuple1)

myTuple1.count(2)
myTuple1.index(2)


class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        code_list=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        alpha_list=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
                    
        alpha_code_map={alpha_list[i]:code_list[i] for i in range(len(alpha_list))}
        
        start=''
        collector=[]
        for val in words:
            for alp in val:
                start+=alpha_code_map[alp]
            if start not in collector:
                collector.append(start)
            start=''
        return len(collector)
                    
        





