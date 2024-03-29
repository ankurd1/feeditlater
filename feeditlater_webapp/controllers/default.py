import string
import random
import datetime

def index():
    response.title = "FeedItLater"
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
    response.view = 'generic.json'
    if 'secret' in request.post_vars and 'url' in request.post_vars:
        if (IS_URL()(request.post_vars['url'])[1] is not None):
            return dict(msg="Failed")
        user = db(db.users.secret==request.post_vars['secret']).select().first()
        if user is None:
            return dict(msg="Failed")
        else:
            db.links.insert(user_id=user.id, url=request.post_vars['url'],
                    created_on=datetime.datetime.now())
            return dict(msg="Success")
    else:
        return dict(msg="Failed")


def feed():
    response.view = 'default/submit_link.html'
    if (len(request.args) != 0):
        secret = request.args[0]
        user = db(db.users.secret==secret).select().first()
        if user is None:
            return dict(msg="Invalid")
        else:
            entries = []
            for link in user.links.select():
                entries.append(dict(title=link.url, link=link.url,
                    description='', created_on=link.created_on))
            response.view = 'generic.rss'
            return dict(title=user.email + "'s feed-it-later feed", 
                    link='', description='', created_on='',
                    entries=entries)
    else:
        return dict(msg="Invalid")
