from app import db

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(5000))
    delimiter = db.Column(db.String(100))
    def __repr__(self):
        return '<Post {}>'.format(self.body)