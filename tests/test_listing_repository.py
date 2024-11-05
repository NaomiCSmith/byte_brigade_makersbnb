from lib.listing_repository import *
from lib.listing import *

# find all
def test_find_all_listings(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    listing_repository = ListingRepository(db_connection)


    listings = listing_repository.all()
    assert listings == [
        Listing(1, "Alpine Retreat Lodge", "A cozy, rustic lodge in the mountains featuring three bedrooms, a fireplace, and a hot tub with scenic woodland views.", 220, 4),
        Listing(2, "City Chic Loft", "A sleek, modern loft in the heart of the city with an open floor plan and panoramic views, ideal for urban adventurers.", 200, 2),
        Listing(3, "Seaside Serenity", "A peaceful coastal retreat with stunning ocean views, a private balcony, and luxurious modern amenities.", 100, 1)
        ]

# find one
def test_find_one_listing(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    listing_repository = ListingRepository(db_connection)

    listing = listing_repository.find(2)

    assert listing == Listing(2, "City Chic Loft", "A sleek, modern loft in the heart of the city with an open floor plan and panoramic views, ideal for urban adventurers.", 200, 2)

# # create
def test_create_listing(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    listing_repository = ListingRepository(db_connection) 

    listing = listing_repository.create(Listing(None, "Cloud palace", "Very fluffy!", 1000, 1))

    listings = listing_repository.all()

    assert listings == [
        Listing(1, "Alpine Retreat Lodge", "A cozy, rustic lodge in the mountains featuring three bedrooms, a fireplace, and a hot tub with scenic woodland views.", 220, 4),
        Listing(2, "City Chic Loft", "A sleek, modern loft in the heart of the city with an open floor plan and panoramic views, ideal for urban adventurers.", 200, 2),
        Listing(3, "Seaside Serenity", "A peaceful coastal retreat with stunning ocean views, a private balcony, and luxurious modern amenities.", 100, 1),
        Listing(4, "Cloud palace", "Very fluffy!", 1000, 1)
        ]


# # delete
def test_delete_listing(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    listing_repository = ListingRepository(db_connection) 

    listing_repository.delete(2)

    listings = listing_repository.all()

    assert listings == [
        Listing(1, "Alpine Retreat Lodge", "A cozy, rustic lodge in the mountains featuring three bedrooms, a fireplace, and a hot tub with scenic woodland views.", 220, 4),
        Listing(3, "Seaside Serenity", "A peaceful coastal retreat with stunning ocean views, a private balcony, and luxurious modern amenities.", 100, 1)
        ]