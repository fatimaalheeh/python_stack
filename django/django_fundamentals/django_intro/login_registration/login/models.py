from django.db import models

class Users(models.Model):

    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at =models.DateTimeField(auto_now_add=True) 
    updated_at =models.DateTimeField(auto_now=True) 
#MTV's Best practice:
#handling data is better be done in models not in views,
#HOW?
#check this out:
def register(name,pswd):
    Users.objects.create(name=name, password=pswd)

def check_user(name,pswd):
    #suppose username stored in the database is unique
    #is the user_name in the database?
    user=Users.objects.filter(name=name)
    #set a variable to contain the value returned by the filter, if it's none:
    if user == None:
        return False
    #if the value is not null:
    if user[0].password ==pswd:
        return True
    return False    # this line is none of your businessz