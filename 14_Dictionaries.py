# FriendFace Post
# user_id = 209
# message = "I love my family."
# language = "English"
# datetime = "20230215T124231Z"
# location = (44.590533, -104.715556)

post = {"user_id": 209, "message": "I love my family.", "language":"English",
		"datetime":"20230215T124231Z", "location": (44.590533, -104.715556)}

print(type(post))
print(post)
post2 = dict(message = "I love you too.", language = "English")
post2["user_id"] = 209
post2["datetime"] = "19771116T093001Z"
print(post2)

# To access specific key with value
print(post['message'])

# To avoid error that key is not in the dictionary
if 'location' in post2:
	print(post2['location'])
else:
	print("The post does not contain location value.")

# Another way to do this is using try and except

try:
	print(post2['location'])
except:
	print("The post does not have location value.")

# Use get() method to get the key value
loc = post2.get('location', None)
print(loc)

# To iterate over all the keys
for keys in post.keys():
	value = post[keys]
	print(keys, "=", value)

print("Another Method")
# Another way to iterate over all the key value pairs 
for key, values in post.items():
	print(key, "=", values)
