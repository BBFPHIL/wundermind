from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


#File upload function for upload_to attribute

def content_file_name(instance, filename):
    return '/'.join(['content', instance.user.email, filename])


class Crew(models.Model):

    crew_name = models.CharField(max_length=128)

    crew_desc = models.TextField()

    crew_logo = models.FileField(upload_to=content_file_name) #This could be a really cool thing for each teams identity                                                                             

    members = models.ManyToManyField(User, through='UserProfile')

    def __unicode__(self):
        return "{0} {1} {2} {3} {4} {5}".format(self.crew_name, self.crew_desc, self.crew_logo, self.members)




class UserProfile(models.Model):
    
    user = models.OneToOneField(User)
    crew = models.ForeignKey(Crew)
    
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

    skill_rating = models.DecimalField('Skill Rating', max_digits=2, decimal_places=2) #Rating the skills through JavaScript

    position_type = models.CharField('position', max_length=128, choices=POS_TYPE)
    
    github_url = models.URLField()
    
    profile_pic = models.FileField(upload_to=content_file_name)
    
    about_me = models.TextField()
    
    skills = models.CharField('skills', max_length=128, choices=SKILL_TYPE)

        
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)
            
        post_save.connect(create_user_profile, sender=User)


    def __unicode__(self):
        return "{0} {1} {2} {3} {4} {5}".format(self.skill_rating, self.position_type, self.github_url, self.about_me, self.skills)


class Barracks(models.Model):
    
    project_name = models.CharField(max_length=128)
    
    project_desc = models.CharField(max_length=128)
    
    message = models.TextField()

    members = models.ForeignKey(User)
    
    crew = models.ForeignKey(Crew)

    pub_date = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return "{0} {1} {2} {3} {4} {5}".format(self.project_name, self.project_desc, self.members, self.crew)
