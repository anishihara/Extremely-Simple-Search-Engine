#Define a procedure,

#hashtable_update(htable,key,value)

#that updates the value associated
#with key. If key is already in the
#table, change the value to the new
#value. Otherwise, add a new entry
#for the key and value.

#Hint: Use hashtable_lookup as a
#starting point.

def hashtable_update(htable,key,value):
    table_value = hashtable_lookup(htable,key)
    if table_value:
        bucket = hashtable_get_bucket(htable,key)
        for unit in bucket:
            if unit[0] == key:
                unit[1] = value
                return
    else:
        hashtable_add(htable,key,value)

def hashtable_lookup(htable,key):
    bucket = hashtable_get_bucket(htable,key)
    for entry in bucket:
        if entry[0] == key:
            return entry[1]
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
hashtable_update(table,'abc','teste modificado')
print table