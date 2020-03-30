from application import db

class Insults(db.Model):
    insult_id = db.Column(db.Integer, primary_key=True)
    insult = db.Column(db.Text, nullable=False)


    def __repr__(self):
        return f"Insults('{self.insult_id}','{self.insult}')"
