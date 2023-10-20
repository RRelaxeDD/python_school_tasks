request = int(input("enter room number: "))

dictionary = {
    101: {
        "key": 1234, 
        "access": True
    },
    102: {
        "key": 1337, 
        "access": True
    },
    103: {
        "key": 8943, 
        "access": True
    },
    104: {
        "key": 5555, 
        "access": False
    }
}

response = dictionary.get(request)

if not response:
    response = dictionary[None]

key = response.get("key")
access = response.get("access")
print(key, access)