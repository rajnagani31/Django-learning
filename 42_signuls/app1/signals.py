from django.contrib.auth.models import User
from django.contrib.auth.signals import user_logged_in,user_logged_out,user_login_failed
from django.dispatch import receiver
from django.db.models.signals import pre_init,pre_save,pre_delete,post_init,pre_migrate,post_save,post_migrate,post_delete

# ------------------------------------> 2 method for signal register 1.decoreter/ 2. .coneact method
@receiver(user_logged_in,sender=User)
def login_success(sender,request,user ,**kwargs):
    print("--------------------")

    print("🖊 logged-in signal.. Run Sucessfully")
    print("Request:",request)
    print("User:",user)
    # print("Name",user.name)
    print("Password:",user.password)
    print("Sender:",sender)
    print(f"Kward :{kwargs}")

    print("Sucessfully Login")

# user_logged_in.connect(login_success,sender=User)   


# -------> logged out

@receiver(user_logged_out,sender=User)
def log_out_success(sender,request,user ,**kwargs):
    print("--------------------")

    print(" logged-out signal.. Run Sucessfully")
    print("Request:",request)
    print("user",user)
    print("Sender:",sender)
    print(f"Kward :{kwargs}")
    print("Sucessfully Logout")


# ----------------------> Login Fail
@receiver(user_login_failed)
def login_fail(sender,request,credentials,**kwargs):
    print("--------------------")

    print("🖊 logged-in signal.. Failed")
    print("Request:",request)
    print("credentials:",credentials)
    print("Sender:",sender)
    print(f"Kward :{kwargs}")
    print("login Failed")


# ------------->pre save
@receiver(pre_save,sender=User)
def pre_save(sender,instance,**kwargs):
    print("--------------------")
    print("Pre Save")
    print("Sender:",sender)
    print("Insatance:",instance)
    print("Kwargs",kwargs)

# ------------->post save
@receiver(post_save,sender=User)
def post_save_(sender,instance,created,**kwargs):
    if created:
        print("--------------------")
        print("Post Save created")
        print("Sender:",sender)
        print("Insatance:",instance)
        print("Kwargs",kwargs)

    else:
        print("--------------------")
        print("Post Save Updated")
        print("Sender:",sender)
        print("Insatance:",instance)
        print("Kwargs",kwargs)    

# -----------------------> pre delete
@receiver(pre_delete,sender=User)
def pre_delete_(sender,instance,**kwargs):
        print("--------------------")
        print("pre delete")
        print("Sender:",sender)
        print("Insatance:",instance)
        print("Kwargs",kwargs)

# -----------------------> post delete
@receiver(post_delete,sender=User)
def post_delete_(sender,instance,**kwargs):
        print("--------------------")
        print("Post delete")
        print("Sender:",sender)
        print("Insatance:",instance)
        print("Kwargs",kwargs)
 
# -----------------------> post delete
@receiver(pre_init,sender=User)
def pre_init_(sender,*arg,**kwargs):
        print("--------------------")
        print("Pre init")
        print("Sender:",sender)
        print("Arg:",arg)
        print("Kwargs",kwargs)
 
 # -----------------------> post delete
@receiver(post_init,sender=User)
def post_init_(sender,*arg,**kwargs):
        print("--------------------")
        print("Post init")
        print("Sender:",sender)
        print("Arg:",arg)
        print("Kwargs",kwargs)
 
