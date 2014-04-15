Python - Hash Notes

ord('1-ltr str') -> number
chr(number) -> '1-ltr str'

chr(ord(a)) -> a

#hash_str v1
def hash_str(keyword, hash_size):
	return ord(keyword[0]) % hash_size

#hash_str v2 - adds all letters together in keyword, then mods them
def hash_str2(keyword, hash_size):
    pos = 0 #this will also cause blanks to return 0
    for each in keyword:
        pos += ord(each) #alternate:  pos = (pos + ord(each)) % hash_size
    return pos % hash_size


#function below us used to test the above hash function
#arguments have a function, good example to see that you can do this
def test_hash_func(func, keys, size):
	results = [0] * size
	keys_used = []
	for w in keys:
		if w not in keys_used:
			hv = func(w, size)
			results[hv] += 1
		return results

# Define a procedure, make_hashtable,
# that takes as input a number, nbuckets,
# and returns an empty hash table with
# nbuckets empty buckets.

def make_hashtable(nbuckets):
    new_table = []
    for each in range(nbuckets):
        new_table.append([]) #this can't be an assignment as you are addint elements to a list     
    return new_table

#define a procedure called hashtable_get_bucket
#takes two inputs, the table and a value
#outputs the bucket where the keyword would go
def hashtable_get_bucket(hashTable,keyword):
	return hashTable[hash_string(keyword,len(hashTable)]

#simple hash function that adds together the ordinal value of each string char
#then mods it and returns
def hash_string(keyword,buckets):
	output = 0
	for each in keyword:
		output = (output + ord(each)) % buckets
	return output

#function to add something to the hash, without taking anything into account
#uses hash function to find location then appends it
def hashtable_add(htable, keyword, value): 
    htable[hash_string(keyword,len(htable))].append([keyword,value])
    return htable
