#WIP 
from collections import Counter
import random
discount = {1:1,
            2:0.95,
            3:0.90,
            4:0.80,
            5:0.75}

def total(basket):
    books = Counter(basket)

    while total_books:=sum([books[x] for x in books]) > 0:
        group = [x for x in books if books[x] != 0]
        purchase_bundle = random.sample(group, random.randint(1, len(group)))
        books = {key:books[key]-1 for key in purchase_bundle}
        print(books)
        print(purchase_bundle)

            
    


        

print(total([5, 5, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3]))