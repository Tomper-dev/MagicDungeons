'''

        Magic Dungeons game.
        A text-based RPG.

'''
try:
    # import section
    from random import choice as ran
    from time import sleep as sle

    # variable section
    weapons = [
        ['Hand', 5, 0],
        ['Wooden Sword', 7, 700]
    ]

    monster = [
        ['Orc', 7, 40, 40],
        ['Blerg', 7, 20, 20]
    ]

    pickaxes = [
        ['Wooden Pickaxe', 0, 600],
    ]

    axes = [
        ['Wooden Axe', 0, 500],
    ]

    inv = []

    helmets = [
        ['Cooper Helmet', 20, 300],
    ]

    chestplates = [
        ['Cooper Chestplates', 30, 400],
    ]

    leggings = [
        ['Cooper Leggings', 30, 200]
    ]

    boots = [
        ['Cooper Boots', 20, 200]
    ]

    items = [
        weapons,
        pickaxes,
        axes,
        helmets,
        chestplates,
        leggings,
        boots
    ]

    stats = {
        'Name': str(input('Name: ')),
        'Level': 1,

        'xp': 0,
        'MaxXp': 50,

        'Life': 50,
        'MaxLife': 50,

        'Helmet': None,
        'Chestplate': None,
        'Leggings': None,
        'Boots': None,

        'Axe': None,
        'Pickaxe': None,
        'Weapon': weapons[0][0],
        'Weapon Damage': weapons[0][1],
        'Active Equipment': None,

        'Money': 100.00,
        'Defeated': 0
    }

    life = stats['Life']

    # function section
    def attack(atkvar, monsterlife):
        return monsterlife - atkvar


    def levelup(levelvar, life, money, maxxpvar, xpvar):
        levelvar += 1
        life += 50
        money += 500
        maxxpvar += 50
        xpvar -= stats['MaxXp']


    # Principal game section

    print(f'Magic Dungeons'.center(30, '='))
    sle(1)
    while True:
        option = str(input('Command ("Wiki" for available commands): ').upper())
        if option == 'WIKI':
            print("""
            Hunt - Search and battle a monster!
            Mine - Dig to find ores, money and XP! (Pickaxe required)
            Chop - Cut wood to get wood, money and XP! (Axe required)
            Inv - See your items on your inventory!
            Buy - Buy some items!
            Items - See the items that you can buy!
            Stats - Show your stats!
            
            
            End - Close the game.
            """)
        elif option == 'HUNT':
            while True:
                m = ran(monster)
                print(f'{stats["Name"]} found {m[0]}!')
                attack(stats['Weapon Damage'], m[2])
                attack(m[1], life)
                sle(1)
                print(f'{stats["Name"]} dealt {stats["Weapon Damage"]}')
                print(f'{m[0]} dealt {m[1]}')
                print(f'{stats["Name"]}\'s health is {life}')
                print(f'{m[0]}\'s life is at {m[3]}')
                if stats['Life'] <= 0:
                    print('YOU DIED!')
                    death = True
                    break
                elif monster[3] <= 0:
                    print('THE MONSTER DIED!')
                    stats['XP']['xp'] += 7
                    stats['Money'] += 50


except Exception as error:
    print(f'An error ocurred. ID={error.__class__}')
