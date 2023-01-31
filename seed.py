"""Seed file to add data to Bogly database"""
from models import db, Pet
from app import app

# Create all tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it
Pet.query.delete()


# Add pets
Woofly = Pet(name="Woofly", species="Beagle", photo_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS-j6Fu175vRzTcFnWNjF2dgo_FREFV7KQ6tg&usqp=CAU', age='1', notes = "Such a lovebug!", available=True)

Porchetta = Pet(name="Porchetta", species="Porcupine", photo_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQlvk6cklM1qBpTDtZ_mMvAptsS4V4_oCvAfA&usqp=CAU', age = '3', notes = 'Watch out for her quills!', available=True)

Snargle = Pet(name="Snargle", species='Maine Coon', photo_url="https://cattitudedaily.com/wp-content/uploads/2019/11/flehmen-response-cat.jpg", age='2', notes='Makes funny faces!', available=True)

# Add new objects to session so they'll persist
db.session.add_all([Woofly, Porchetta, Snargle])

# Commit -- otherwise this never gets saved
db.session.commit()