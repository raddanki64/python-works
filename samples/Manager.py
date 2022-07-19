from Employee import Employee


class Manager(Employee):
    def __init__(self, lastname, firstname, count):
        self.count = count
        Employee.__init__(self, lastname, firstname)

    def dump(self):
        super().dump()
        print("Reports cnt: %d" % self.count)



