from django.db import models
from django.contrib.auth.models import User


"""
Define users with the Django User class
"""

"""
THIS IS NOT NECCESSARY!!! ITS ALREADY DONE!!!!

class Members(models.Model):
    
    first_name = models.first_name(max_length=30)
    last_name = models.last_name(max_length=30)
    email = models.email()
    password = models.password()
    #Facebook DOB
    #Picture from FB
    #website url from Github


class Crew(models.Model):
    
    crew_name = models.CharField(max_length=128)
    crew_leader = models.CharField() #Foreign Key?
    members = models.ManyToMany(Members, through='MemberProfile')
    stack_type = models.CharField(max_length=128)
"""    
"""

class MemberProfile(models.Model):    
    
    members = models.ForeignKey(Members)
    crew = models.ForiegnKey(Crew)
    skills = models.CharField(max_length=128)
    


class PositionType(models.Model):

    member = models.ForiegnKey(MemberProfile) #Related to Members profile                                                                                                                            
    back_end =models.BooleanField(False)
    front_end = models.BooleanField(False)
    graphic_artist =models.BooleanField(False)
    sys_admin =models.BooleanField(False)
    software_engineer = models.BooleanField(False)



"""

    #Members
    







"""
Many To Many Relationship
"""

"""
class Person(models.Model):
    name = models.CharField(max_length=128)

    def __unicode__(self):
        return self.name

class Group(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(Person, through='Membership')


class Membership(models.Model):
    person = models.ForeignKey(Person)
    group = models.ForeignKey(Group)
    date_joined = models.DateField()
    invite_reason = models.CharField(max_length=64)
"""
