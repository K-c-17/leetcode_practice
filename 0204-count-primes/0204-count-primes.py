from math import sqrt

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        prime=[True]*n

        if n==0 or n==1:
            return 0
        
        prime[0],prime[1]=False,False

        for i in range(2,int(n**0.5)+1):
            if prime[i]:
                for j in range(i+i,n,i):
                    # print(i,j)
                    prime[j]=False
        
        return sum(prime)
        
        
        
        
        
        
        
        
        
        
        #brute force O(n*sqrt(n))
        count=0
        prime=[]

        for i in range(2,n):
            is_prime=1
            for j in range(2,int(sqrt(i))+1):
                if i%j==0:
                    is_prime=0
                    break
            if is_prime==1:
                count+=1
                prime.append(i)
        
        print(prime)
        return count

        
        