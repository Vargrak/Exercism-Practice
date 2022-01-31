import datetime
def add(moment, gigasecond=1000000000):
    new_time = moment + datetime.timedelta(0,gigasecond)
    return new_time