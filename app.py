import os
from lib.database_connection import get_flask_database_connection
from lib.listing_repository import *
from lib.listing import *
from lib.user_repository import *
from lib.user import *
from flask import Flask, request, render_template, redirect

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==


@app.route('/add_listing', methods=['GET'])
def get_add_listing():
    return render_template('add_listing.html')

# get all listings on homepage
@app.route('/home', methods=['GET'])
def get_listings():
    connection = get_flask_database_connection(app)
    repository = ListingRepository(connection)
    listings = repository.all()
    return render_template('home.html', listings=listings)

# add anchors to listings page
@app.route('/home/<int:listing_id>', methods=['GET'])
def show_listing(listing_id):
    connection = get_flask_database_connection(app)
    repository = ListingRepository(connection)
    listing = repository.find(listing_id)
    return render_template('/show_listing.html', listing=listing)

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
