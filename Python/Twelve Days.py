verses = {1:"a Partridge in a Pear Tree.",
          2:"two Turtle Doves, ",
          3:"three French Hens, ",
          4:"four Calling Birds, ",
          5:"five Gold Rings, ",
          6:"six Geese-a-Laying, ",
          7:"seven Swans-a-Swimming, ",
          8:"eight Maids-a-Milking, ",
          9:"nine Ladies Dancing, ",
          10:"ten Lords-a-Leaping, ",
          11:"eleven Pipers Piping, ",
          12:"twelve Drummers Drumming, ",}

days =   {1:"first",
          2:"second",
          3:"third",
          4:"fourth",
          5:"fifth",
          6:"sixth",
          7:"seventh",
          8:"eighth",
          9:"ninth",
          10:"tenth",
          11:"eleventh",
          12:"twelfth",}

def recite(start_verse, end_verse):
    """Recites the twelve days of christmas, for the highest day only, if start and end verse are the same."""
    twelve_days = ""
    if start_verse == end_verse:
        """Dictionaries store most of the verse and are called by the input verses"""
        twelve_days = f"On the {days.get(start_verse)} day of Christmas my true love gave to me: "
        for i in range(end_verse, 0, -1):
            """adds and if the day 1 verse is not by itself. Rest of fstring concatenates the verses together"""
            if i == 1 and end_verse > 1:
                twelve_days =f"{twelve_days}and "
            twelve_days = f"{twelve_days}{verses.get(i)}"
        return [twelve_days]

    else:
        """Works similarly to the above, except it iterates through every day if the start and end verse are not the same; from the specified
        start day to the end day. Each seperate day is appended to a list and the entire list is returned after it is done cycling."""
        twelve_days_list = []
        for x in range(start_verse, end_verse+1):
            twelve_days = f"On the {days.get(x)} day of Christmas my true love gave to me: "
            for i in range(x, 0, -1):
                if i == 1 and x > 1:
                    twelve_days =f"{twelve_days}and "
                twelve_days = f"{twelve_days}{verses.get(i)}"
            twelve_days_list.append(twelve_days)
        return twelve_days_list