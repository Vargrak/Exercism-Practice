def distance(strand_a, strand_b, count=0):
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")

    for index, x in enumerate(strand_a):
        if x != strand_b[index]:
            count += 1
    
    return count