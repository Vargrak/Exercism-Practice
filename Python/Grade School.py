class School:
    def __init__(self):
        self.students = {}
        self.was_added = []
        self.highest_grade = 0

    def add_student(self, name, grade):
        if name not in self.students:
            self.students.update({name:grade})
            if grade > self.highest_grade:
                self.highest_grade = grade
            self.was_added.append(True)
        else:
            self.was_added.append(False)

    def roster(self):
        return_roster = []
        for i in range(0, self.highest_grade+1):
            temp = []
            for key in self.students:
                if self.students[key] == i:
                    temp.append(key)
            return_roster.extend(sorted(temp))
        return return_roster

    def grade(self, grade_number):
        grade_roster = []
        for key in self.students:
            if self.students[key] == grade_number:
                grade_roster.append(key)
        grade_roster = sorted(grade_roster)
        return grade_roster

    def added(self):
        return self.was_added