list = [2,3,5,[5,3,1,[4,2,"thelist"]]]
print(list[3][3][2])

l = {"Key First" : "Value Next",
     "Sky Colour": "Blue",
     "Water Colour": ["Transparent","Nothing"]}
watercolourvalue = l["Water Colour"]
print((watercolourvalue[1]))

s = [{"Skycolour" : "Blue",
     "Water Colour": "Light Blue",
     "Suncolour" : "Yellow"},

     {"SkyColour" : "Black",
     "Water Colour": "Dark Blue",
     "Sun Colour" : "nothing"}]
print(s[1]["Water Colour"])
