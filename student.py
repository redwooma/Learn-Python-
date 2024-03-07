class Student:
    # class is an overview of what the student data type is. (template)
    # object is an actual student with a name, major, gpa, etc. (actual)
    # initialized function : can map out the attributes a student should have.
    def __init__(self, name, major, gpa):
        self.name = name
        self.major = major
        self.gpa = gpa

    def on_honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False
