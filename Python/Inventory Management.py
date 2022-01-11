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

def list_inventory(inventory, inv_rm = None):
    inv_rm = []
    for key in inventory:
        if inventory[key] == 0:
            inv_rm.append(key)
    for key in inv_rm:
        inventory.pop(key)
    return list(inventory.items())