from pony import orm
from decimal import Decimal
from datetime import datetime

db = orm.Database()


class User(db.Entity):
    name = orm.PrimaryKey(str)
    password_hash = orm.Required(bytes)
    balance = orm.Required(Decimal)
    profile_picture = orm.Optional(str)
    is_parent = orm.Required(bool)
    auth_token = orm.Optional(str)
    token_expiration_date = orm.Optional(datetime)


class ScheduledPayment(db.Entity):
    sender_name = orm.Required(str)
    receiver_name = orm.Required(str)
    days = orm.Required(int)
    schedule = orm.Required(int)
    amount = orm.Required(Decimal)
    desc = orm.Optional(str)


class Log(db.Entity):
    sender_name = orm.Required(str)
    receiver_name = orm.Required(str)
    amount = orm.Required(Decimal)
    new_balance_sender = orm.Required(Decimal)
    new_balance_receiver = orm.Required(Decimal)
    time = orm.Required(datetime)
    desc = orm.Optional(str)
