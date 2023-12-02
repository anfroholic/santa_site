
story = {
    'Greeting':[ 
        {"name": "Merry Christmas",
         "snippet": "Merry Cristmas to everyone!"}, 
        {"name": "Happy Holidays",
         "snippet": "Hello from the north pole, We hope you're all having happy holidays"},
        {"name": "Special Request",  # the term 'Special Request' is special and will inject the text input field and more
         "snippet": "eg. Hello from Santo to the [insert family name] Family"},
    ],
    "Enjoy Family": [
        {"name": "Grandmas",
         "snippet": "I hope you're having a wonderful time at Grandma's"},
        {"name": "Meals",
         "snippet": "I hope you enjoyed your turkey dinner"},
    ],
    "Storytime": [
        {"name": "Night Before Christmas",
         "snippet": "Twas the night before Christmas and all through the house..."},
        {"name": "Santa's Christmas Adventures",
         "snippet": "Have you heard of hte great Forest of Burzee"}
    ],
    # Some Goodness section could be good here. eg 'I have heard you have been good boys and girls'
    # also a good section to get custom moneys as you can say their actual names!!
    "Presents": [
        {"name": "Garage",
         "snippet": "I left you some presents in the garage"},
        {"name": "Kitchen",
         "snippet": "I left you some presents in the kitchen"},
        {"name": "Upstairs",
         "snippet": "I left you some presents upstairs"},
        {"name": "Downstairs",
         "snippet": "I left you some presents downstairs"},
        {"name": "Tree",
         "snippet": "I left you some presents under the tree"},
    ]
}



lookup = {}
for name, choices in story.items():
    for choice in choices:
        lookup[choice['name']] = name