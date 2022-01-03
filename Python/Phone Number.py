class PhoneNumber:
    AREA_CODE = -10
    EXCHANGE_CODE = -7
    COUNTRY_CODE = 0
    NUM_LEN_MIN = 10
    NUM_LEN_MAX = 11

    def __init__(self, number):
        self.number = number
        self.number = self.number_processing(number)
        self.area_code = self.area_code(number)

    def number_processing(self, number):
        ignored = "()[]{}?_-#$+\/. "
        number = ''.join(char for char in self.number if char not in ignored)
        number = self.validate_number(number)
        return number
        
    def validate_number(self, number):
        if number.isdigit() is False:
            for char in number:
                if char.isdigit() is False:
                    if char.isalpha() is False:
                        raise ValueError("punctuations not permitted")
                    elif char.isalpha() is True:
                        raise ValueError("letters not permitted")
        if len(number) < self.NUM_LEN_MIN:
            raise ValueError("incorrect number of digits")
        if len(number) > self.NUM_LEN_MAX:
            raise ValueError("more than 11 digits")
        if number[self.EXCHANGE_CODE] == "1":
            raise ValueError("exchange code cannot start with one")
        elif number[self.EXCHANGE_CODE] == "0":
            raise ValueError("exchange code cannot start with zero")
        if number[self.AREA_CODE] == "0":
            raise ValueError("area code cannot start with zero")
        elif number[self.AREA_CODE] == "1":
            raise ValueError("area code cannot start with one")
        if len(number) == self.NUM_LEN_MAX:
            if number[self.COUNTRY_CODE] != "1":
                raise ValueError("11 digits must start with 1")
            number = number[1:]
        return number

    def area_code(self, number):
        number = self.number_processing(number)
        return number[0:3]

    def pretty(self):
        number = self.number
        self.number_processing(number)
        number = "(" + number[0:3] + ")-" + number[3:6] + "-" + number[6:10]
        return number