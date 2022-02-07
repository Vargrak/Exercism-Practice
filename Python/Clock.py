class Clock:
    def __init__(self, hour, minute):
        self.hour = hour%24
        self.hour += minute//60
        self.minute = minute%60
        self.time_boundary_pass()

    def __repr__(self):
        return f'Clock({str(self.hour)}, {str(self.minute)})'

    def __str__(self):
        return f"{str(self.hour).rjust(2, '0')}:{str(self.minute).rjust(2, '0')}"

    def __eq__(self, other):
        return self.hour == other.hour and self.minute == other.minute

    def __add__(self, minutes):
        self.minute += minutes
        self.hour += self.minute//60
        self.time_boundary_pass()
        return self.__str__()

    def __sub__(self, minutes):
        self.minute -= minutes
        self.hour -= abs(self.minute//60)
        self.time_boundary_pass()
        return self.__str__()

    def time_boundary_pass(self):
        while self.hour > 23:
            self.hour -= 24

        while self.hour < 0:
            self.hour += 24

        while self.minute > 59:
            self.minute -= 60

        while self.minute < 0:
            self.minute += 60