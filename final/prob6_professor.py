#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 08:20:07 2017

@author: umesh
"""

class Person(object):
    def __init__(self, name):
        self.name = name
    def say(self, stuff):
        return self.name + ' says: ' + stuff
    def __str__(self):
        return self.name

class Lecturer(Person):
    def lecture(self, stuff):
        return 'I believe that ' + Person.say(self, stuff)

class Professor(Lecturer):
    def say(self, stuff):
        return 'Prof. ' + self.name + ' says: ' + self.lecture(stuff)

# Prob 6-1
#class ArrogantProfessor(Professor):
#    def say(self, stuff):
#        #return 'It is obvious that ' + self.say(stuff)
#        return self.name + ' says: ' + 'It is obvious that ' + Person.say(self, stuff)
#
#    def lecture(self, stuff):
#        return 'It is obvious that ' + Person.say(self, stuff)

# Prob 6-2
#class ArrogantProfessor(Professor):
#    def say(self, stuff):
#        #return 'It is obvious that ' + self.say(stuff)
#        return self.name + ' says: ' + 'It is obvious that ' + Lecturer.lecture(self, stuff)
#
#    def lecture(self, stuff):
#        return 'It is obvious that ' + Lecturer.lecture(self, stuff)


#  Prob 6-3
# Prob 6-2
class ArrogantProfessor(Professor):
    def say(self, stuff):
        #return 'It is obvious that ' + self.say(stuff)
        return self.name + ' says: ' + 'It is obvious that ' + Lecturer.lecture(self, stuff)

    def lecture(self, stuff):
        return 'It is obvious that ' + Lecturer.lecture(self, stuff)




# testing condition
e = Person('eric')
le = Lecturer('eric')
pe = Professor('eric')
ae = ArrogantProfessor('eric')

print(e.say('the sky is blue'))
print(le.say('the sky is blue'))
print(le.lecture('the sky is blue'))
print(pe.lecture('the sky is blue'))

print(ae.say('the sky is blue'))
print(ae.lecture('the sky is blue'))

# 6-3
print(pe.say('the sky is blue'))
print(ae.say('the sky is blue'))