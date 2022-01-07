def triplets_with_sum(number, triplet_list = None, c = 0):
    triplet_list = []
    for k in range(1, number):
            for m in range(2, number):
                for n in range(1, m):
                        a = k*((m**2) - (n**2))
                        b = k*(2*m*n)
                        c = k*((m**2) + (n**2))
                        if a + b + c == number:
                            if a > 0 and b > 0 and c > 0:
                                temp = sorted([a, b, c])
                                if temp not in triplet_list:
                                    triplet_list.append(temp)
                        if c > number:
                            break
                if c > number:
                        break
    return sorted(triplet_list)