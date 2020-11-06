import flask_sqlalchemy
from app import db
#not sure what our main python file will be called
#left it as 'app' for now

class Users(db.Model):
    email = db.Column(db.String(120), primary_key=True)
    user_id = db.Column(db.Integer)
    first_name = db.Column(db.String(120))
    last_name = db.Column(db.String(120))
    descr = db.Column(db.String(250))
    user_type = db.Column(db.String(120))
    gen_link_1 = db.Column(db.String(250))
    gen_link_2 = db.Column(db.String(250))
    gen_link_3 = db.Column(db.String(250))
    image = db.Column(db.String(250))
    doc = db.Column(db.String(250))

    def __init__(self, e, u_id, fname, lname, des, u_type, gl1, gl2, gl3, img, d):
        self.email = e
        self.user_id = u_id
        self.first_name = fname
        self.last_name = lname
        self.descr = des
        self.gen_link_1 = gl1
        self.gen_link_2 = gl2
        self.gen_link_3 = gl3
        self.image = img
        self.doc = d

    # do we need this?
    def __repr__(self):
        email = '<Email: %s, >' % self.email
        user_id = '<User ID: %s, >' % self.user_id
        fname = '<First Name: %s, >' % self.first_name
        lname = '<Last Name: %s, >' % self.last_name
        name = fname + lname
        des = '<Description: %s, >' % self.descr
        gl1 = '<Link 1: %s, >' % self.gen_link_1
        gl2 = '<Link 2: %s, >' % self.gen_link_2
        gl3 = '<Link 3: %s, >' % self.gen_link_3
        im = '<Image Link: %s, >' % self.image
        doc = '<Document Link: %s, >' % self.doc
        links = gl1 + gl2 + gl3 + im + doc
        res = email + user_id + name + des + links
        return res
