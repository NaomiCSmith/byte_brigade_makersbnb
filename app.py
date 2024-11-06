import os
from flask import Flask, request, render_template, redirect, url_for
from lib.database_connection import get_flask_database_connection
from lib.listing_repository import *
from lib.listing import *
from lib.user_repository import *
from lib.user import *
from datetime import datetime


# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

@app.route('/add_listing', methods=['GET'])
def get_add_listing():
    return render_template('add_listing.html')



# request a booking page
@app.route('/request_booking/<id>', methods=['GET'])
def get_request_booking(id):
    connection = get_flask_database_connection(app)
    listing_repository = ListingRepository(connection)

    listing = listing_repository.find(id)

    id = listing.id
    name = listing.name
    description = listing.description
    price = listing.price

    return render_template('request_booking.html', id=id, name=name, description=description, price=price)





# request a booking
@app.route('/request_booking/<id>', methods=['POST'])
def post_request_booking(id):
    start_date = request.form.get("start_date")
    end_date = request.form.get("end_date")

    start_date_datetime = datetime.strptime(start_date, "%Y-%m-%d")
    end_date_datetime = datetime.strptime(end_date, "%Y-%m-%d")


    if has_invalid_date_parameters(request.form):
        return "Both start and end dates are required!", 400
    elif start_date_datetime.date() < datetime.now().date():
        return "Start date cannot be in the past"
    elif end_date_datetime <= start_date_datetime:
        return "End date must be after start date"
        

    return redirect(url_for('request_booking_successful', id=id, start_date=start_date, end_date=end_date))

def has_invalid_date_parameters(form):
    return 'start_date' not in form or 'end_date' not in form









# booking confirmation page
@app.route('/request_booking_successful', methods=['GET'])
def request_booking_successful():
    id = request.args.get("id")
    start_date = request.args.get("start_date")
    end_date = request.args.get("end_date")

    connection = get_flask_database_connection(app)
    listing_repository = ListingRepository(connection)
    listing = listing_repository.find(id)
    listing_name = listing.name

    return render_template('request_booking_successful.html', start_date=start_date, end_date=end_date, name=listing_name)

# add_listing_branch
@app.route("/listings/new", methods=['POST'])
def post_new_listing():
    connection = get_flask_database_connection(app)
    repository = ListingRepository(connection)

    name = request.form['name']
    description = request.form['description']
    price = int(request.form['price'])
    # user_id = request.form['user_id'] #TODO#
    user_id = 1
    listing = Listing(None, name, description, price, user_id)

    if not listing.is_valid():
        errors = listing.generate_errors()
        print(errors)
        return render_template('add_listing.html', errors=errors)
    
    repository.create(listing)
    return redirect(f"/home")

# get all listings on homepage
@app.route('/home', methods=['GET'])
def get_listings():
    connection = get_flask_database_connection(app)
    repository = ListingRepository(connection)
    listings = repository.all()
    print(listings)
    return render_template('home.html', listings=listings)

# add anchors to listings page
@app.route('/home/<int:listing_id>', methods=['GET'])
def show_listing(listing_id):
    connection = get_flask_database_connection(app)
    repository = ListingRepository(connection)
    listing = repository.find(listing_id)
    return render_template('/show_listing.html', listing=listing)


# http://local:5001/sign_up
@app.route('/sign_up', methods=['GET'])
def get_sign_up_form():
    return render_template('sign_up.html')

@app.route('/sign_up', methods=['POST'])
def create_account():
    if has_invalid_user_parameters(request.form):
        return "You need to submit a username, email address, and password to create an account", 400
    connection = get_flask_database_connection(app)
    repository = UserRepository(connection)
    user = User(None, request.form['username'], request.form['email'], request.form['password'])
    repository.create(user)
    return render_template('successful_sign_up.html'), 200

# invalid parameters
def has_invalid_user_parameters(form):
    return 'username' not in form or \
        'email' not in form or \
            'password' not in form

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
