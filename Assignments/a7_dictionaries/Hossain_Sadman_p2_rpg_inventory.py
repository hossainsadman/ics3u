"""
A7 - 2: RPG INVENTORY
"""

__author__ = 'Hossain, Sadman'

MAX_WEIGHT = 200


### write your functions here following FDR ###
def display_inv(inventory):
    """Print player inventory, including numbers of each item and total 
    number of items."""

    total = 0
    unadded = []
    print('Inventory:')
    for key in inventory.keys():
        num = inventory[key]
        print(num, key)
    print('Total items: {}'.format(get_weight(inventory)))


def get_weight(inventory) -> int:
    """Return total weight of items in player inventory."""
    weight = 0
    for key in inventory.keys():
        weight += inventory[key]
    return weight


def add_to_inv(inventory, loot):
    """Add loot to player inventory. If loot item is not already in player
    inventory, add a new item."""

    unadded = []
    for item in loot:
        if get_weight(inventory) == MAX_WEIGHT:
            unadded.append(item)
        else:
            try:
                inventory[item] += 1
            except KeyError:
                inventory[item] = 1
    if get_weight(inventory) == MAX_WEIGHT:
        print("These items were not added:")
        print(*unadded)
        # Another way to print all items in list separated by spaces on one line
        # for item in unadded:
        #     print(item, end = ' ')
        # print()


def drop(inventory, item, number = 1): 
    """Remove a number of items (default: 1) from player inventory.
    If number of items to drop exceeds the inventory amount, remove item from
    player inventory."""

    if inventory[item] > number:
        inventory[item] -= number
    else:
        inventory.pop(item)


if __name__ == '__main__':
    bag = {'gold': 100, 'dagger': 10, 'wheat': 70, 'arrow': 17}
    display_inv(bag)

    slime_loot = [ 'gold', 'cloth', 'wheat', 'arrow', 'silver', 'ruby']
    add_to_inv(bag, slime_loot)
    display_inv(bag)

    drop(bag, 'wheat')
    display_inv(bag)

    drop(bag, 'wheat', 73)
    display_inv(bag)