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
    
    # create a var with the value of 0
    position = 0

    while True:
        if cards == []:
            return -1

        if cards[position] == query:
            return position

        position += 1

        if position == len(cards):
            return -1


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

# cards does not contain query
test.append({
    'input': {
        'cards': [9, 7, 5, 2, -9],
        'query': 6
    },
    'output': -1
})

# cards is empty
test.append({
    'input': {
        'cards': [],
        'query': 7
    },
    'output': -1
})

# query occurs multiple times
test.append({
    'input': {
        'cards': [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 0, 0, 0, 0, 0],
        'query': 6
    },
    'output': 2
})


for i in test:
    print(locate_card(**i['input']) == i['output'])

###############################################