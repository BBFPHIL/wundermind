from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class UserProfile(models.Model):
    
    user = models.OneToOneField(User)
    
    POS_TYPE = (
        ('Backend', 'Backend'),
        ('Frontend', 'Frontend'),
        ('Graphic Designer', 'Graphic Designer'),
        ('Sys Admin', 'Sys Admin'),
        ('Software Engineer', 'Software Engineer'),
        )

    SKILL_TYPE = (
        ['Python', 'Python'],
        ('PHP',  'PHP'),
        ('JavaScript', 'Javascript'),
        ('C++', 'C++'),
        ('Ruby', 'Ruby'),
        ('JAVA', 'JAVA'),
        ('C', 'C'),
        ('C#', 'C#'),
        ('Obj-C', 'Obj-C'),
        ('Lua', 'Lua'),
        ('Haskell', 'Haskell'),
        ('ErLang', 'ErLang'),
        ('MySQL', 'MySQL'),
        ('Postgresql', 'Postgresql'),
        ('Node.js', 'Node.js'),
        ('Backbone.js', 'Backbone.js'),
        ('Celery', 'Celery'),
        ('Hadoop', 'Hadoop'),
        ('JQUERY', 'JQUERY'),
        ('CSS', 'CSS'),
        ('HTML', 'HTML'),
        ('JSON', 'JSON'),
        ('XML', 'XML'),
        ('Unix', 'Unix'),
        ('Django', 'Django'),
        ('MongoDB', 'MongoDB'),
        ('CouchBase', 'CouchBase'),
        ('Perl', 'Perl'),
        ('Assembly', 'Assembly'),
        ('A++', 'A++'),
        ('Alice', 'Alice'),
        ('Action!', 'Action!'),
        ('AWK', 'AWK'),
        ('Arc', 'Arc'),
        ('AppleScript', 'AppleScript'),
        ('Ada', 'Ada'),
        ('.NET', '.NET'),
        ('BASIC', 'BASIC'),
        ('COBOL', 'COBOL'),
        ('Boomerang', 'Boomerang'),
        ('BREW', 'BREW'),
        ('git', 'git'),
        ('Bourne shell', 'Bourne shell'),
        ('Clojure', 'Clojure'),
        ('Memcache', 'Memcache'),
        ('Cherrypy', 'Cherrypy'),
        ('Lisp', 'Lisp'),
        ('F#', 'F#'),
        ('Hugo', 'Hugo'),
        ('J++', 'J++'),
        ('MATLAB', 'MATLAB'),
        ('Numpy', 'Numpy'),
        ('SciPy', 'SciPy'),
        ('Mathematica', 'Mathematic'),
        ('Mercurial', 'Mercurial'),
        ('S-PLUS', 'S-PLUS'),
        ('VBA', 'VBA'),
        ('YQL', 'YQL'),
        ('Oracle', 'Oracle'),
        ('Redhat', 'Redhat'),
        ('Ubuntu', 'Ubuntu'),
        ('Windows', 'Windows'),
        ('SQLite', 'SQLite')
        )


    position_type = models.CharField('position', choices=POS_TYPE)

    github_url = models.URLField()
    
    profile_pic = models.ImageField()
    
    about_me = models.TextField()
    
    skills = models.CharField('skills', choices=SKILL_TYPE)
    
    #crew_associated = models.ForeignKey(Crew)

    
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)
            
        post_save.connect(create_user_profile, sender=User)



class Crew(models.Model):
    
    crew_name = models.CharField(max_length=128)
    
    crew_desc = models.TextField()
    
    crew_logo = models.ImageField() #This could be a really cool thing for each teams identity
    
    members = models.ManyToManyField(User, through='UserProfile')

    

class Barracks(models.Model):
    
    project_name = models.CharField(max_length=128)
    
    project_desc = models.CharField(max_length=128)
    

    



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
