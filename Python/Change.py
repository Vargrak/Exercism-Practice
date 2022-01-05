import itertools

def find_fewest_coins(coins, target, change=None):
    change, temp_change, can_make = [], [], 0
    if target < 0:
        raise ValueError("target can't be negative")
    coins.reverse()
    for i in range(1, target+1):
        for coin_amt in itertools.combinations_with_replacement(coins, i):
            if sum(coin_amt) == target:
                can_make = 1
                change = coin_amt
                break
        if coin_amt == change:
            break
    if can_make == 0 and target is not 0:
        raise ValueError("can't make target with given coins")
    change = list(change)
    change.reverse()
    return change