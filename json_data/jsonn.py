import json

"""SERIALIZATION EXAMPLE"""
data = {'President': {'Name': 'Vladmir Putin',
                      'Country': 'Russia'}}

with open('data_file.json', 'w') as write_file:
    json.dump(data, write_file)

json_string = json.dumps(data, indent=4)
print(json_string)

""""DESERIALIZATION"""
blackjack_hand = (8, 'Q')
encoded_hand = json.dumps(blackjack_hand)
decoded_hand = json.loads(encoded_hand)

print(blackjack_hand == encoded_hand)
print(type(blackjack_hand))
print(type(decoded_hand))
print(blackjack_hand == tuple(decoded_hand))

with open('data_file.json', 'r') as read_file:
    data = json.load(read_file)
    print(data)

json_string = """
{
'researcher':{
     'name': 'Ford Prefect',
     'species': 'Betelgeusian',
     'relatives': [
        {
           'name': 'Zaphod Beeblerox',
           'species': 'Betelgeusian'
        }
    ]
  }
}
     """

data = json.loads(json_string)
print(data)
