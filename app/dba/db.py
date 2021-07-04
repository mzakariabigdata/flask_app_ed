from flask_sqlalchemy import SQLAlchemy
from dba.models import db

def add(book):
    db.session.add(book)
    db.session.commit()