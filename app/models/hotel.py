from app.models import db


class Hotel(db.Model):
    __tablename__ = "hotel"

    id = db.Column(db.Integer, primary_key=True)
    hotel_name = db.Column(db.String(50), nullable=False, unique=True)
    address = db.Column(db.String(100), nullable=False)
    room_quantity = db.Column(db.Integer, nullable=False)
    stars = db.Column(db.String(2), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    def add(self, hotel):

        db.session.add(hotel)
        db.session.commit()

    @classmethod
    def update(cls):
        db.session.commit()
