class Employee(object):
    def __init__(self, first_name, second_name, salary, experience):
        self.first_name = first_name
        self.second_name = second_name
        self.salary = salary
        self.experience = experience
        first_name = 0
        second_name = 0
        salary = 500
        experience = 1

    def __repr__(self):
        return "{} {}, experience: {},".format(self.first_name, self.second_name, self.experience)

    # def give_salary(salary):
    #     print salary
    #     return salary

    def current_salary(self):
        return self.salary

class Developer(Employee):
    def __init__(self, manager, *args):
        self.manager = manager
        super(Developer, self).__init__(*args)

    def __repr__(self):
        return "{} {}, manager: {}, experience: {},".format(self.first_name, self.second_name, self.manager, self.experience)

class Designer(Employee):
    def __init__(self, eff_coeff, manager, *args):
        self.eff_coeff = eff_coeff
        self.manager = manager
        super(Designer, self).__init__(*args)

    def current_salary(self):
        return self.salary * self.eff_coeff

    def __repr__(self):
        return "{} {}, manager: {}, experience: {},".format(self.first_name, self.second_name, self.manager, self.experience)

class Manager(Employee):
    # stuff
    # stuff["d", "d", "d", "d", "dev"]
    def __init__(self, stuff, first_name, second_name, salary, experience):
        self.first_name = first_name
        self.second_name = second_name
        self.salary = salary
        self.experience = experience
        # self.stuff = stuff["d","d","d","d","dev"]
        self.stuff = stuff
        # self.stuff = stuff[a,s,d,f,gh,h]
        # self.stuff = tuple(stuff)
        # stuff = []
        # super(Developer, self).__init__(*args)

    def get_stuff(self):
        stuff = self.stuff
        return stuff

    def current_salary(self):
        dev = 0
        sal = self.salary
        stuff = self.stuff
        if len(stuff) > 10:
            sal = sal + 300
        elif len(stuff) > 5:
            sal = sal + 200
        for emp in stuff:
            if emp == "d":
                dev = dev + 1
            if dev > 0.5*len(stuff):
                sal = sal*1.1
        return sal




d = Developer("manager", "name", "second name", 1500, 4)
# print d
# d.give_salary()
# print d.current_salary()
print d
m = Developer("manager2", "name", "second name", 500, 4)
# print m
des = Designer(0.9, "manager", "name", "second name", 1500, 4)
# print des.current_salary()
print des

mgr = Manager(["s","d","2","4","5","f","d","d","d","d","d","d"], "name", "second name", 1500, 7)
print mgr
print mgr.get_stuff()
print mgr.current_salary()
