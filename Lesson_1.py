              # ################ #
###############     Problem      ##############
              # ################ #
"""
QUESTION 1: Alice has some cards with numbers written on them. 
She arranges the cards in decreasing order, and lays them out 
face down in a sequence on a table. She challenges Bob to pick 
out the card containing a given number by turning over as few 
cards as possible. Write a function to help Bob locate the card.
"""



              # ################ #
###############     Solution     ##############
              # ################ #


def locate_card(cards, query):
    pass





              # ################ #
###############    Test cases    ##############
              # ################ #
test = []

# query occurs in the middle
test.append({
    'input': {
        'cards': [13, 11, 10, 7, 4, 3, 1, 0],
        'query': 7
    },
    'output': 3
})

# query is the first element
test.append({
    'input': {
        'cards': [4, 2, 1, -1],
        'query': 4
    },
    'output': 0
})

# query is the last element
test.append({
    'input': {
        'cards': [-1, 0, 1, 2, 3, 4, 5, 6, 7],
        'query': 7
    },
    'output': 8
})

# cards contain only one element, query
test.append({
    'input': {
        'cards': [7],
        'query': 7
    },
    'output': 0
})


for i in test:
    print(locate_card(**i['input']) == i['output'])

###############################################