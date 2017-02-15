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

    def __str__(self):
        return "{} {}, experience: {},".format(self.first_name,
                                               self.second_name,
                                               self.experience)

    def get_salary(self):
        if 2 < self.experience <= 5:
            self.salary += 200
        elif self.experience > 5:
            self.salary = self.salary * 1.2 + 500
        return self.salary


class Developer(Employee):
    pass


class Designer(Employee):
    def __init__(self, eff_coeff, *args):
        self.eff_coeff = eff_coeff
        super(Designer, self).__init__(*args)

    def get_salary(self):
        Employee.get_salary(self)
        self.salary *= self.eff_coeff
        return self.salary


class Manager(Employee):
    def __init__(self, first_name, second_name, salary, experience, team = []):
        """
        :type team: list if Developers or Designers
        """
        self.team = team
        super(Manager, self).__init__(first_name, second_name, salary, experience)

    def get_salary(self):
        Employee.get_salary(self)
        team_counter = len(self.team)
        if 5 < team_counter <= 10:
            self.salary += 200
        elif team_counter >= 10:
            self.salary += 300
        dev_counter = 0
        for employee in self.team:
            if isinstance(employee, Developer):
                dev_counter += 1
        print "Developers in team: ",dev_counter
        if dev_counter > team_counter % 2:
            self.salary *= 1.1
        return self.salary

    def add_to_team(self, employee):
        if self.team == []:
            raise NotEmployeeException
        elif isinstance(employee, Manager):
            raise WrongEmployeeRoleError
        else:
            self.team.append(employee)


d = Developer("name", "second name", 500, 4)
print d
print d.get_salary()
a = Developer("name2", "second name", 500, 4)
b = Developer("name3", "second name", 500, 4)
d = Developer("name4", "second name", 500, 4)
e = Developer("name5", "second name", 500, 4)
f = Developer("name6", "second name", 500, 4)

c = Designer(0.75,"name", "second name", 500, 2)
print c
print c.get_salary()

m = Manager("Manager", "Managerenko", 500, 7, ["D","C","K",d,a,b,e,f])
print m
print m.get_salary()
