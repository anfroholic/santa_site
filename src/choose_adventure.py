
story = {
    'Greeting':[ 
        {"name": "Merry Christmas",
         "snippet": "Merry Cristmas to everyone!",
         "pic": "see_no"}, 
        {"name": "Happy Holidays",
         "snippet": "Hello from the north pole, We hope you're all having happy holidays",
         "pic": "hear_no"},
        {"name": "Special Request",  # the term 'Special Request' is special and will inject the text input field and more
         "snippet": "eg. Hello from Santa to the Robinson Family"},
    ],
    "Enjoy Family": [
        {"name": "Grandmas",
         "snippet": "I hope you're having a wonderful time at Grandma's",
         "pic": "cough"},
        {"name": "Meals",
         "snippet": "I hope you enjoyed your turkey dinner",
         "pic": "goofy"},
    ],
    "Storytime": [
        {"name": "Night Before Christmas",
         "snippet": "Twas the night before Christmas and all through the house...",
         "pic": "book"},
        {"name": "Santa's Christmas Adventures",
         "snippet": "Have you heard of the great Forest of Burzee",
         "pic": "phone"}
    ],
    # Some Goodness section could be good here. eg 'I have heard you have been good boys and girls'
    # also a good section to get custom moneys as you can say their actual names!!
    "Presents": [
        {"name": "Garage",
         "snippet": "I left you some presents in the garage",
         "pic": "see_no"},
        {"name": "Kitchen",
         "snippet": "I left you some presents in the kitchen",
         "pic": "hear_no"},
        {"name": "Upstairs",
         "snippet": "I left you some presents upstairs",
         "pic": "hear_no"},
        {"name": "Downstairs",
         "snippet": "I left you some presents downstairs",
         "pic": "point"},
        {"name": "Tree",
         "snippet": "I left you some presents under the tree",
         "pic": "what"},
    ]
}

adventures = [
    {'family': 'the hendersons', 'Greeting': 'Happy Holidays', 'Enjoy Family': 'Meals', 'Storytime': 'Night Before Christmas', 'Presents': 'Upstairs'},
    {'family': 'the smiths', 'Greeting': 'Special Request: happy birthday to tommy and suzie', 'Enjoy Family': 'Grandmas', 'Storytime': 'Night Before Christmas', 'Presents': 'Kitchen'}, 
    {'family': 'the jacksons', 'Greeting': 'Merry Christmas', 'Enjoy Family': 'Meals', 'Storytime': "Santa's Christmas Adventures", 'Presents': 'Tree'},
    {'family': 'the johnsons', 'Greeting': 'Special Request: charlie has been very bad this year', 'Enjoy Family': 'Meals', 'Storytime': "Santa's Christmas Adventures", 'Presents': 'Downstairs'},
]

lookup = {}
for name, choices in story.items():
    for choice in choices:
        lookup[choice['name']] = name