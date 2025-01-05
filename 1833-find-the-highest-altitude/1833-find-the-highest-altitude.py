class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        altitude=[0]*(len(gain)+1)
        top=1

        for i in range(len(gain)):
            altitude[top]=altitude[top-1]+gain[i]
            top+=1

        return max(altitude)


        