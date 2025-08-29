class Hashtable:
    def __init__(self):
        self.size = 10
        self.table = [[] for _ in range(self.size)]  # create empty buckets

    def _hash(self, key):
        return hash(key) % self.size    

    def set(self, key, value):
        index = self._hash(key)
        bucket = self.table[index]
        for i, (k, v) in enumerate(bucket):
            if k == key:  # update if key exists
                bucket[i] = (key, value)
                return
        # if not found, insert new key-value
        bucket.append((key, value))

    def get(self, key):
        index = self._hash(key)
        bucket = self.table[index]
        for k, v in bucket:
            if k == key:
                return v
        return None


# Example usage
h = Hashtable()
h.set("name", "Alice")
print(h.get("name"))   # ✅ Output: Alice

                
                