class Employee(object):
    def __init__(self, lastname, firstname):
        self.lastname = lastname
        self.firstname = firstname

    def dump(self):
        print("Last name: %s, first name: %s" % (self.lastname, self.firstname))




