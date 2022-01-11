def create_inventory(items):
    return {key: items.count(key) for key in items}

def add_items(inventory, items):
    for item in items:
        inventory[item] = inventory.get(item, 0) + 1
    return inventory

def decrement_items(inventory, items):
    for item in items:
        if inventory[item] > 0 and item in inventory.keys():
            inventory[item] = inventory.get(item, 0) - 1
    return inventory

def remove_item(inventory, item):
    if item in inventory.keys():
        inventory.pop(item)
    return inventory

def list_inventory(inventory):
    return inventory.items()