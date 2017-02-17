class Employee(object):
    def __init__(self, first_name, second_name, salary, experience):
        self.first_name = first_name
        self.second_name = second_name
        self.salary = salary
        self.experience = experience
        amount_salary = salary
        first_name = 0
        second_name = 0
        salary = 500
        experience = 1

    def __repr__(self):
        return "{} {}, experience: {},".format(self.first_name, self.second_name, self.experience)

    # def get_bonus(self):
    #     if 2 < self.experience <= 5:
    #         self.salary += 200
    #         return self.salary
    #     elif self.experience > 5:
    #         self.salary = self.salary * 1.2 + 500
    #     return self.salary

    def bonus(self):
        amount_salary = self.salary
        if self.experience > 5:
            return amount_salary * 1.2 + 500
        elif self.experience > 2:
            return  amount_salary + 200

    # def give_salary(salary):
    #     print salary
    #     return salary

    def current_salary(self):
        a = self.bonus()
        return a

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
        return self.bonus() * self.eff_coeff

    def __repr__(self):
        return "{} {}, manager: {}, experience: {},".format(self.first_name, self.second_name, self.manager, self.experience)

class Manager(Employee):
    def __init__(self, stuff, first_name, second_name, salary, experience):
        self.first_name = first_name
        self.second_name = second_name
        self.salary = salary
        self.experience = experience
        self.stuff = stuff

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



#
# d = Developer("manager", "name", "second name", 1500, 7)
# # print
# # d.give_salary()
# # print d.current_salary()
# print d
# print d.current_salary()
# print d.bonus()
# m = Developer("manager2", "name", "second name", 500, 4)
# print m
des = Designer(0.9, "manager3", "name", "second name", 1500, 6)

print des.current_salary()
print des.bonus()
#
# mgr = Manager(["s","d","2","4","5","f","d","d","d","d","d","d"], "name", "second name", 1500, 7)
# print mgr.current_salary()
# print mgr.bonus()
