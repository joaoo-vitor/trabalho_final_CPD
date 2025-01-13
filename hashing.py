def hash(key, M):
    return key % M

def start_hash_table(M):
    hash_table = {}
    for i in range(M):
        hash_table[i] = []
    return hash_table

def insert_hash_table(key, item, hash_table, M):
    pos = hash(key, M)
    hash_table[pos].append(item)

def search_hash_table(key, key_name, hash_table, M):
    pos = hash(key, M)
    for item in hash_table[pos]:
        if(key == item[key_name]):
            return item 
    return False
