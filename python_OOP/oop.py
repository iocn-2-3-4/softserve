#!/usr/bin/python

class NotEmployeeException:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return " there is not Employee in manager's team " + str(self.value)

class WrongEmployeeRoleError:
    def __str__(self):
        return "Employee {} has unexpected role! ".format(self.second_name)


class SalaryGivingError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return " there is not Employee in manager's team " + str(self.value)

class Department(object):
    def __init__(self, manager):
        self.manager = manager

    def give_salary(self):
        if self.manager.team:
            for employee in self.manager.team:
                print "{} {}: got salary: {}".format(employee.first_name, employee.second_name, employee.salary)
        else:
            raise SalaryGivingError

    def add_team_members(self,employee=[]):
        self.manager.add_to_team(employee)

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

    def get_salary(self):
        if 2 < self.experience <= 5:
            self.salary += 200
        elif self.experience > 5:
            self.salary = self.salary * 1.2 + 500
class NotEmployeeException:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return " there is not Employee in manager's team " + str(self.value)

class WrongEmployeeRoleError:
    def __str__(self):
        return "Employee {} has unexpected role! ".format(self.second_name)


class SalaryGivingError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return " there is not Employee in manager's team " + str(self.value)

class Department(object):
    def __init__(self, manager):
        self.manager = manager

    def give_salary(self):
        if self.manager.stuff:
            for employee in self.manager.stuff:
                print "{} {}: got salary: {}".format(employee.first_name, employee.second_name, employee.current_salary())
        else:
            raise SalaryGivingError


    def add_stuff_members(self,employee=[]):
        self.manager.stuff.append(employee)

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


    def with_bonus(self):
        amount_salary = self.salary
        if self.experience > 5:
            return amount_salary * 1.2 + 500
        elif self.experience > 2:
            return  amount_salary + 200
        else:
            return amount_salary

    def current_salary(self):
        return self.bonus()

class Developer(Employee):
    def __init__(self, manager, *args):
        self.manager = manager
        super(Developer, self).__init__(*args)

    def __repr__(self):
        return "{} {}, manager: {}, experience: {},".format(self.first_name, self.second_name, self.manager, self.experience)

    def current_salary(self):
        return self.with_bonus()

class Designer(Employee):
    def __init__(self, eff_coeff, manager, *args):
        self.eff_coeff = eff_coeff
        self.manager = manager
        super(Designer, self).__init__(*args)

    def current_salary(self):
        return self.with_bonus() * self.eff_coeff

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
        sal = self.with_bonus()
        stuff = self.stuff
        if len(stuff) > 10:
            sal = sal + 300
            print sal
        elif len(stuff) > 5:
            sal = sal + 200
        for emp in stuff:
            if type(emp) == Developer:
                dev = dev + 1
            if dev > 0.5*len(stuff):
                sal1 = sal*1.1
            elif dev < 0.5*len(stuff):
                sal1 = sal
        return sal1



#
d = Developer("manager1", "name", "second name", 1500, 7)
e = Developer("manager2", "name", "second name", 3500, 7)
c = Developer("manager3", "name", "second name", 1500, 7)
b = Developer("manager4", "name", "second name", 1500, 7)
a = Developer("manager5", "name", "second name", 1500, 7)
km = Developer("manager555", "name555", "second555 name5555", 4500, 7)

# # print
# # d.give_salary()
# # print d.current_salary()
# print d
# print d.current_salary()
# print d.bonus()
# m = Developer("manager2", "name", "second name", 500, 4)
# print m
des = Designer(0.9, "manager3", "name", "second name", 1500, 6)
# print des.current_salary()
# print des.with_bonus()
#
# mgr = Manager(["s","d","2","4","d","x"], "name", "second name", 1500, 7)
mgr = Manager([d,e], "name", "second name", 2500, 2)
# print mgr.current_salary()
# print mgr.stuff
# print mgr.with_bonus()

ui = Department(mgr)
ui.add_stuff_members(km)
ui.give_salary()

