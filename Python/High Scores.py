def latest(scores):
    return scores[-1]

def personal_best(scores):
    scores = sorted(scores)
    return scores[-1]

def personal_top_three(scores, top_three = None):
    top_three = []
    scores = sorted(scores)
    if len(scores) < 3:
        top = len(scores)
    else:
        top = 3
    for i in range(-1, -top-1, -1):
        top_three.append(scores[i])
    return top_three