class Garden:
    """Dictionary for conversion of input string to words"""
    plant_dict = {"R":"Radishes",
                  "C":"Clover",
                  "G":"Grass",
                  "V":"Violets"}

    """Diagram is a set of unspaced letters representing each plant. Students can be specificed. If not specified the default list will be used. List is alphabetically sorted."""
    def __init__(self, diagram, students=["Alice", "Bob", "Charlie", "David", "Eve", "Fred", "Ginny", "Harriet", "Ileana", "Joseph", "Kincaid", "Larry"]):
        self.diagram = [row for row in diagram.split("\n")]
        self.students = sorted(students)

    """Splits the input diagram into two or more rows based on newlines. Student's index * 2 determines their responsible plants on the rows from the diagram.
    After the plants are found, they are converted via the dictionary into a list of plants that the input student is responsible for."""
    def plants(self, student):
        plants_temp = ""
        assigned_plants = []
        for row in self.diagram:
            index = self.students.index(student) * 2
            plants_temp = f"{plants_temp}{row[0+index:2+index]}"
        for letter in plants_temp:
            assigned_plants.append(self.plant_dict.get(letter))
        return assigned_plants