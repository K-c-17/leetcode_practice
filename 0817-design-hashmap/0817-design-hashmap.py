class MyHashMap(object):

    def __init__(self):
        self.hashmap={}
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        self.hashmap[key]=value
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.hashmap.keys():
            return self.hashmap[key]
        else:
            return -1
        

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        if key in self.hashmap.keys():
            del self.hashmap[key]
            return
        else:
            return 
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)