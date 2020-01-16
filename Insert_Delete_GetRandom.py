import random
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.item = []
        

    def insert(self, val: int) -> bool:
        if val in self.item:
            return False
        self.item.append(val)
        return True
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        

    def remove(self, val: int) -> bool:
        
        try:
            del self.item[self.item.index(val)]
        except:
            return False
        
        return True
        
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.sample(self.item,1)[0]
        
    

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
