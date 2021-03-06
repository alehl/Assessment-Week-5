"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise directions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()

# -------------------------------------------------------------------
# Start here.


# Part 2: Write queries

# Get the brand with the **id** of 8.
>>> Model.query.get(8)

# Get all models with the **name** Corvette and the **brand_name** Chevrolet.
>>> Model.query.filter_by(name ='Corvette', brand_name = 'Chevrolet').all()

# Get all models that are older than 1960.
>>> Model.query.filter(Model.year > 1960).all()

# Get all brands that were founded after 1920.
>>> Model.query.filter(Brand.founded > 1920).all()
""" I struggled with this one, but realized I had a typo on model.py "Discounted" instead of "Discontinued" """

# Get all models with names that begin with "Cor".
>>> Model.query.filter(Model.name.like('Cor%')).all()

# Get all brands with that were founded in 1903 and that are not yet discontinued.
>>> Brand.query.filter(Brand.founded == '1903', Brand.discontinued.is_(None)).all()

"""This one doesn't work... but something like this, right?"""

# Get all brands with that are either discontinued or founded before 1950.
""" I kept getting errors for this one, not sure what I'm getting wrong""" 

# Get any model whose brand_name is not Chevrolet.
>>> Model.query.filter(Model.brand_name != 'Chevrolet').all()

# Fill in the following functions. (See directions for more info.)

def get_model_info(year):
    '''Takes in a year, and prints out each model, brand_name, and brand
    headquarters for that year using only ONE database query.'''

    model_info = db.session.query(Model, 
    								Brand).filter(Model.year = year).join(Brand)

    for model, brand in models.all():
    	print model.name, model.brand_name, brand.headquarters

def get_brands_summary():
    '''Prints out each brand name, and each model name for that brand
     using only ONE database query.'''

    brand_summary = db.session.query(Brand, 
    									Model).join(Model)

    for brand, model in brands.all():
    	print brand.name, model.name

# -------------------------------------------------------------------


# Part 2.5: Advanced and Optional
def search_brands_by_name(mystr):
    pass
	"""Sorry, this is beyond me"""

def get_models_between(start_year, end_year):
    pass

    """Sorry, this is beyond me"""

# -------------------------------------------------------------------

# Part 3: Discussion Questions (Include your answers as comments.)

# 1. What is the returned value and datatype of ``Brand.query.filter_by(name='Ford')``?
  <flask_sqlalchemy.BaseQuery object at 0x108c17590>

# 2. In your own words, what is an association table, and what *type* of relationship
# does an association table manage?

""" An association table glues two tables with data. It can have more than one foreign key. 
It is a "many to many" relationship type of table, even though M2M tables don't really exist. """
