#Define a procedure,

#hashtable_lookup(htable,key)

#that takes two inputs, a hashtable
#and a key (string),
#and outputs the value associated
#with that key.

def hashtable_lookup(htable,key):
    bucket = hashtable_get_bucket(htable,key)
    for unit in bucket:
        if unit[0]== key:
            return unit[1]
    return None

def hashtable_add(htable,key,value):
    bucket = hashtable_get_bucket(htable,key)
    bucket.append([key,value])    


def hashtable_get_bucket(htable,keyword):
    return htable[hash_string(keyword,len(htable))]

def hash_string(keyword,buckets):
    out = 0
    for s in keyword:
        out = (out + ord(s)) % buckets
    return out

def make_hashtable(nbuckets):
    table = []
    for unused in range(0,nbuckets):
        table.append([])
    return table

table = make_hashtable(10)
hashtable_add(table,'1','teste')
hashtable_add(table,'teste','teste')
hashtable_add(table,'abc','teste')
print hashtable_lookup(table,'abc')