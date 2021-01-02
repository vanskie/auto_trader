import json

testData = {
    "hacker": {
            "name": "vanskie",
            "age": 25
        }
    }

with open('hacker.json', 'w') as hackerFile:
    json.dump(testData, hackerFile, indent=4)

with open('hacker.json', 'r') as hackerFile:
    result = json.load(hackerFile)

print(result)
print(result['hacker'])
print(result['hacker']['name'])
