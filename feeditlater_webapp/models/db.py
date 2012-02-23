if request.env.web2py_runtime_gae:
    db = DAL('gae')
    session.connect(request, response, db)
else:
    db = DAL('sqlite://storage.db')

db.define_table('users',
        Field('email', label="Email", unique=True, notnull=True,
            requires=IS_EMAIL()),
        Field('secret', notnull=True)
        )

db.define_table('links',
        Field('user_id', db.users),
        Field('url', length=128, notnull=True),
        Field('created_on', 'datetime')
        )
