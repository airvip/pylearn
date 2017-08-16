#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by airvip on 2017/8/16 17:14.

class School(object):

    def __init__(self,name,addr):
        self.name = name
        self.addr = addr
        self.students = []
        self.staffs = []

    def enroll(self,stu_obj):
        print("for student %s register school no"%stu_obj.name)
        self.students.append(stu_obj)

    def hire(self,staff_obj):
        self.staffs.append(staff_obj)
        print("fire a new worker %s"%staff_obj.name)

class SchoolMember(object):
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex

    def tell(self):
        pass

class Teacher(SchoolMember):
    def __init__(self,name,age,sex,salary,course):
        super(Teacher,self).__init__(name,age,sex)
        self.salary = salary
        self.course = course

    def tell(self):
        print("""
        ---- info of Teacher:%s ----
        Name:%s
        Age:%s
        Sex:%s
        Salary:%s
        Course:%s
        """%(self.name,self.age,self.age,self.sex,self.salary,self.course))

    def teach(self):
        print("%s is teaching course [%s]"%(self.name,self.course))

class Student(SchoolMember):
    def __init__(self,name,age,sex,stu_id,grade):
        super(Student,self).__init__(name,age,sex)
        self.stu_id = stu_id
        self.grade = grade

    def tell(self):
        print("""
        ---- info of Student:%s ----
        Name:%s
        Age:%s
        Sex:%s
        Stu_id:%s
        Grade:%s
        """%(self.name,self.age,self.age,self.sex,self.stu_id,self.grade))

    def pay_tuition(self,amout):
        print("%s has paid tution for $%s"%(self.name,amout))


school = School('free school',"china yn")

t1 = Teacher("airvip",20,"M",200000,"Python")
t2 = Teacher("yay",19,"F",100000,"Ps")

s1 = Student("lusy",25,"F",1000,"Ps")
s2 = Student("Lari",27,"F",1001,"Python")

t1.tell()
school.hire(t1)

s1.tell()
s2.tell()
school.enroll(s1)
school.enroll(s2)

print(school.students)
print(school.staffs)

school.staffs[0].teach()

for stu in school.students:
    stu.pay_tuition(5000)
