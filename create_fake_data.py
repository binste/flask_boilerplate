import models
from application.app import create_app, db

app = create_app()
with app.app_context():
    dimensions = []
    for i in range(3):
        sd = models.SomeDimension(name=f"Dimension{i+1}")
        dimensions.append(sd)
        db.session.add(sd)

    for i in range(40):
        if i % 2 == 0:
            sd = dimensions[0]
        elif i % 3 == 0:
            sd = dimensions[1]
        else:
            sd = dimensions[2]

        db.session.add(
            models.InterestingFact(
                name=f"InterestingFact{i+1}",
                description="Useful description",
                some_dimension=sd,
            )
        )

    db.session.commit()
