def slices(series, length):
    if len(series) == 0:
        raise ValueError("series cannot be empty")
    if length > len(series):
        raise ValueError("slice length cannot be greater than series length")
    if length == 0:
        raise ValueError("slice length cannot be zero")
    if length < 0:
        raise ValueError("slice length cannot be negative")

    yield_series = []
    for i in range(0, len(series)):
        yield_series.append(series[i:i+length])
        if i+length >= len(series):
            break
    return yield_series
