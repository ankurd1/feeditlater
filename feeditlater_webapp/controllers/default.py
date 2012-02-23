import string
import random

def index():
    user_reg_form = SQLFORM(db.users, fields=['email'])
    if user_reg_form.validate():
        user = db(db.users.email==user_reg_form.vars.email).select().first()
        if (user is None):
            #generate a secret key, insert into table and redirect
            new_secret = ''.join(random.choice(string.ascii_uppercase +
                string.digits) for x in range(20))
            db.users.insert(email=user_reg_form.vars.email, secret=new_secret)
            return dict(user_secret=new_secret, user_reg_form=None)
        else:
            return dict(user_secret=user.secret, user_reg_form=None)

    return dict(user_reg_form=user_reg_form, user_secret=None)

def submit_link():
    if 'secret' in request.get_vars and 'url' in request.get_vars:
        if (IS_URL()(request.get_vars['url'])[1] is not None):
            return dict(msg="Invalid")
        user = db(db.users.secret==request.get_vars['secret']).select().first()
        if user is None:
            return dict(msg="Invalid")
        else:
            db.links.insert(user_id=user.id, url=request.get_vars['url'])
            return dict(msg="Success")
    else:
        return dict(msg="Invalid")

