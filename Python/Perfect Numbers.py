def classify(number):
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")
    factors = [i for i in range(1, number) if number % i == 0]
    sum_ = sum(factors)
    if sum_ > number:
        return "abundant"
    elif sum_ == number:
        return "perfect"
    elif sum_ < number:
        return "deficient"