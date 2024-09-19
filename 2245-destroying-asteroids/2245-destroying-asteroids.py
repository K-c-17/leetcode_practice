class Solution(object):
    def asteroidsDestroyed(self, mass, asteroids):
        """
        :type mass: int
        :type asteroids: List[int]
        :rtype: bool
        """
        sort_asteroids=sorted(asteroids)

        for i in sort_asteroids:
            if mass>=i:
                mass+=i
            else:
                return False
        
        return True
        