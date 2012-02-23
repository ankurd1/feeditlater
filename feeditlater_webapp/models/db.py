db = DAL("sqlite://storage.db")

db.define_table('users',
        Field('email', label="Email", unique=True, notnull=True,
            requires=IS_EMAIL()),
        Field('secret', notnull=True)
        )

db.define_table('links',
        Field('user_id', db.users),
        Field('url', length=128, notnull=True)
        )
