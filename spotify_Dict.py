

playlist={"name":"Patagonia Bus",
          "author": "Mako",
          "created": 'september',
          'songs': [
              {'title':'song1','artist': ['culture abuse'], 'album':'album 1', 'duration':2.50},
                 ]
}

total_duration=0
for song in playlist['songs']:
    total_duration=total_duration+song['duration']
print(int(total_duration-0.15))

# updated={key.capitalize(): value.capitalize() for key, value in playlist.items()}
# print(updated)

# list1 = ["CA", "NJ", "RI"]
# list2 = ["California", "New Jersey", "Rhode Island"]
#
# answer={list1[i]:list2[i] for i in range  (len(list2))}
# print(answer)

# person=[["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]
# answer={k:v for k,v in person}
# print(answer)
#
# answer1={}.fromkeys(['a','e','i','o','u'], 0)
# print(answer1)
# answer2=dict.fromkeys('aeiou',0)
# print(answer2)
values = [10,20,30]
static_variables=tuple(values)
print(static_variables)
stuff = [1,3,1,5,2,5,1,2,5]
stuff2=set(stuff)
print(stuff2)


