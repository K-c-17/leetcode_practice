class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        '''
        mapping=defaultdict(list)
        for i in range(len(nums)):
            mapping[nums[i]].append(i)
        #print("Mapping is: ",mapping)
        
        for j in mapping:
            if len(mapping[j])>=2:
                for i in range(len(mapping[j])-1):
                    if abs(mapping[j][i+1]-mapping[j][i])<=k:
                        return True
        return False
        '''
        seen = set()
        
        for i in range(len(nums)):
            if nums[i] in seen:
                return True
            seen.add(nums[i])
            if len(seen) > k:
                seen.remove(nums[i - k])
        
        return False