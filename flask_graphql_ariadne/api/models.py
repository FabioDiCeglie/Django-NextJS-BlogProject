from app import db

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    coverImage = db.Column(db.String)
    date = db.Column(db.Date)
    author_name = db.Column(db.String)
    author_picture = db.Column(db.String)
    description = db.Column(db.String)
    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "coverImage": self.coverImage,
            "date": str(self.date.strftime('%d-%m-%Y')),
            "author_name": self.author_name,
            "author_picture": self.author_picture,
            "description": self.description,
        }
