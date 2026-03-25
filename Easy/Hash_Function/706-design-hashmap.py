class MyHashMap:

    def __init__(self):
        self.size = 1000
        self.data = [[] for _ in range(self.size)]
        

    def _hash(self,key):
        return key % self.size
    def put(self, key: int, value: int) -> None:

        idx = self._hash(key)
        bucket = self.data[idx]

        #update
        for ent in bucket:
            if ent[0]==key:
                ent[1]=value
                return

        bucket.append([key,value])        

    def get(self, key: int) -> int:
        idx = self._hash(key)
        bucket = self.data[idx]
        for ent in bucket:
            if ent[0]==key:
                return ent[1]

        return -1

        

    def remove(self, key: int) -> None:
        idx = self._hash(key)
        bucket = self.data[idx]
        
        for i in range(len(bucket)):
            if bucket[i][0] == key:
                bucket.pop(i)
                return

        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)