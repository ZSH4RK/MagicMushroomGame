import random as rn

normalseed = rn.randint(0, 1000000000)
mapx = 1000
mapy = 1000

mushrooms = {
    'Shadowshroom': {
        'name': 'Shadowshroom',
        'type': 'mushroom',
        'rarity': 'common',
        'affects': {
            'realm': 1,
        },
        'description': 'sends you too shadow realm'
    },
    'Poisonshroom': {
        'name': 'Poisonshroom',
        'type': 'mushroom',
        'rarity': 'uncommon',
        'description': 'decrease health to 20 over 2 goes'
    },
    'Haochengshroom': {
        'name': 'Haochengshroom',
        'type': 'potato',
        'rarity': 'exotic',
        'description': 'completely useless, 1 in 10 million'
    },
    'Blueshroom': {
        'name': 'Blueshroom',
        'type': 'fungi',
        'rarity': 'rare',
        'description': 'attackes to head, does 5 damage and blocks vision'
    },
    'ITwithshroom': {
        'name': 'ITwithshrooms',
        'type': 'mushroom',
        'rarity': 'epic',
        'description': 'increases intelligence by 50%'
    },
    'shroomberg': {
        'name': 'shroomberg',
        'type': 'mushroom',
        'rarity': 'uncommon',
        'description': 'increase height by 50, decreases width by 50'
    },
    'ethdeshroom': {
        'name':
        'ethdeshroom',
        'type':
        'fish',
        'rarity':
        'fish',
        'description':
        'Decreases Charisma by 50%, decreases speed by 10, increases defence by 40'
    },
    'strashroom': {
        'name': 'strashroom',
        'type': 'fish',
        'rarity': 'uncommon',
        'description': 'decreases intelligence by 40, increases strength by 20'
    },
    'zakthefish': {
        'name':
        'zakshroom',
        'type':
        'fish',
        'rarity':
        'rare',
        'description':
        'gives 10 health, increases strength by 10, decreases defence by 10'
    },
    'Gizmoshroom': {
        'name':
        'Gizmoshroom',
        'type':
        'mushroom',
        'rarity':
        'uncommon',
        'description':
        'increases speed by 10, decreases stamina by 10, health increases by 5'
    }
}
