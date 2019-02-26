import snap

#basic types are TInt, TFlt, TStr
#defining a vector of integers
v = snap.TIntV()

#adding elements
v.Add(1)
v.Add(2)
v.Add(3)
v.Add(4)
v.Add(5)
print(v.Len())

#accessing elements
print(v[3])

#setting values
v.SetVal(2, 6)

#printing using an iterator
for item in v:
	print item

#printing using an index
for item in range(0, v.Len()):
	print(item, v[item])

#Hash table types - The types are named as per the following conevntion: <key_type><value_type>H
#defining a hash table with integer keys and string values
h = snap.TIntStrH()

#adding elements
h[1] = "one"
h[2] = "two"
h[3] = "three"
h[4] = "four"
h[5] = "five"

print(h.Len())

#retrieving the value for a specific key
print(h[3])

#changing the value corresponding to a specific key
h[3] = "Three"
print(h[3])

for key in h:
	print key, h[key]
