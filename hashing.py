class HashTable():
    def __init__(self, table_size):
        self.table_size = table_size
        self.dict = {}
        self.__start_hash_table()
    def hash(self, key):
        return key % self.table_size
    def __start_hash_table(self):
        for i in range(self.table_size):
            self.dict[i] = []
    def insert(self, key, item):
        pos = self.hash(key)
        self.dict[pos].append(item)
    def search(self, key, key_name):
        pos = self.hash(key)
        for item in self.dict[pos]:
            if(key == item[key_name]):
                return item 
        return False
