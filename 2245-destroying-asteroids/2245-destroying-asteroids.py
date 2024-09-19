class Solution(object):
    def asteroidsDestroyed(self, mass, asteroids):
        """
        :type mass: int
        :type asteroids: List[int]
        :rtype: bool
        """
        sort_asteroids=sorted(asteroids)
        planet_size=mass
        for i in sort_asteroids:
            if planet_size>=i:
                planet_size+=i
            else:
                return False
        
        return True
        