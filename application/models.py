from application.app import db


class InterestingFact(db.Model):
    __tablename__ = "interesting_fact"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.VARCHAR(20))
    description = db.Column(db.VARCHAR(80))
    some_dimension_id = db.Column(db.Integer, db.ForeignKey("some_dimension.id"))

    some_dimension = db.relationship(
        "SomeDimension", back_populates="interesting_facts"
    )


class SomeDimension(db.Model):
    __tablename__ = "some_dimension"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.VARCHAR(20))

    interesting_facts = db.relationship(
        "InterestingFact", back_populates="some_dimension"
    )

