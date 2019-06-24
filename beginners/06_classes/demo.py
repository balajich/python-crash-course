class Student:

    def __init__(self, name):
        self.name = name

    def name(self):
        return self.name



if __name__ == '__main__':
    s = Student('Balaji')
    s.name = 'Sankar'
    s.last_name = 'xyz'
    print(s.name)
    print(s.last_name)
    # print(s.name())
