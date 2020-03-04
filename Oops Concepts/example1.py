# instance method vs classmethod vs staticmethod
# instance variables vs class variables


class Student:

    count = 0

    def __init__(self, name, ht):
        self.name = name
        self.ht = ht

        Student.count = Student.count + 1

    def display(self):
        print("Name: {} Ht: {}".format(self.name, self.ht))

    @classmethod
    def get_total(cls):
        print("Total count : {}".format(cls.count))

    @staticmethod
    def get_avg(list_x):
        return sum(list_x)//len(list_x)



s1 = Student("S1", 23)

s2 = Student("S2", 24)

s3 = Student("S3", 25)

#s1.get_total()
Student.get_total()


resp = s3.get_avg([10, 20, 30, 40])
print(resp)





