from flask import Flask, request, render_template,  redirect, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db,  connect_db, Pet
from forms import AddPetForm, EditPetForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pets_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "chickenzarecool21837"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
toolbar = DebugToolbarExtension(app)

connect_db(app)
db.create_all()

##############################################################################


@app.route('/')
def home_page():
    """Show all pets"""
    pets=Pet.query.all()
    
    return render_template("list_pets.html", pets=pets)


@app.route('/add', methods = ['GET', 'POST'])
def add_pet():
    """Handle form submission for creating a new pet"""

    # Create a new instance of AddPetForm
    form = AddPetForm()
    # validate_on_submit() is a method on form that checks if is a POST request AND if token is valid. If so, do the following or else go back to create_pet.html template
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
     

        # pass in data to new instance of Pet class
        new_pet=Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes)
        # add new pet to data base
        db.session.add(new_pet)
        db.session.commit()
        return redirect('/')
  
    else:
        """# As a GET request (or if token is invalid), show the form for creating a new pet"""
        # pass the instance object 'form' representing the form to the template
        return render_template('create_pet.html', form=form)



@app.route('/pet/<int:pet_id>', methods =['GET', 'POST'])
def pet_show_edit(pet_id):
    """Handle form submission for editing a new pet"""

    # lookup data on pet based on its id
    pet = Pet.query.get_or_404(pet_id)
    # 'pet' populates the fields in Pet From in the pet_details.html form
    form = EditPetForm(obj=pet)
    # validate_on_submit() is a method on form that checks if is a POST request AND if token is valid. If so, do the following or else go back to pet_details.html template
    if form.validate_on_submit():
       
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available=form.available.data

        db.session.commit()

        return redirect('/')

    else:
        """Show a page with info on a specific pet"""

        return render_template('pet_details.html', form=form, pet=pet)
