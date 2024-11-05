from lib.listing import *


def test_class_listing_constructs():
    listing = Listing(1, "Haunted Mansion", "Spend the night in our haunted mansion!", 50, "31/10/2024", 1)

    assert listing.id == 1
    assert listing.name == "Haunted Mansion"
    assert listing.description == "Spend the night in our haunted mansion!"
    assert listing.price_per_night == 50
    assert listing.availability == "31/10/2024"
    assert listing.user_id == 1

def test_equality():
    listing1 = Listing(1, "Gingerbread house", "Please don't eat our walls!", 100, "01/09/2024", 2)
    listing2 = Listing(1, "Gingerbread house", "Please don't eat our walls!", 100, "01/09/2024", 2)

    assert listing1 == listing2

def test_listings_format():
    listing = Listing(1, "test name", "test description", 20, "04/05/2024", 3)

    assert str(listing) == "Listing(1, test name, test description, 20, 04/05/2024, 3)"