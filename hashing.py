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
    tests_qty=0
    for item in hash_table[pos]:
        tests_qty+=1
        if(key == item[key_name]):
            return tests_qty, item 
    return tests_qty, False
