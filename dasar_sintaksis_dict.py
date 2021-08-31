users = {
    'id' : 1,
    'name' : 'Leanne Gram',
    'username' : 'Bret',
    'email' : 'Sincere@april.biz',
    'address' : {
        "street": "Kulas Light",
        "suite": "Apt. 556",
        "city": "Gwenborough",
        "zipcode": "92998-3874",
        "geo": {
            "lat": "-37.3159",
            "lng": "81.1496"
        }
    }
}

print(users['email'])
print(users['address']['geo']['lng'])

import json
print('\nUbah dictionary Python ke JSON')
result = json.dumps(users)
print(result)
print(type(result))