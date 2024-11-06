from playwright.sync_api import Page, expect

# Tests for your routes go here

"""
We can render the index page
"""
def test_get_index(page, test_web_address):
    # We load a virtual browser and navigate to the /index page
    page.goto(f"http://{test_web_address}/index")

    # We look at the <p> tag
    p_tag = page.locator("p")

    # We assert that it has the text "This is the homepage."
    expect(p_tag).to_have_text("This is the homepage.")

# Test title
def test_get_add_listing_page(page, test_web_address):
    page.goto(f"http://{test_web_address}/add_listing")
    expect(page).to_have_title("Makersbnb | Add a Listing")

# Test headings and form structure
def test_form_structure(page, test_web_address):
    page.goto(f"http://{test_web_address}/add_listing")

    expect(page.locator("h1")).to_have_text("Create a New Listing")
    expect(page.locator("h2").nth(0)).to_have_text("Listing Details")
    expect(page.locator("h2").nth(1)).to_have_text("Pricing Information")

# Test visibility of label and instructions
def test_labels_and_instructions(page, test_web_address):
    page.goto(f"http://{test_web_address}/add_listing")

    expect(page.locator("label[for='name']")).to_have_text("Listing Name")
    expect(page.locator("label[for='description']")).to_have_text("Description")
    expect(page.locator("label[for='price_per_night']")).to_have_text("Price per Night (GBP)")

    expect(page.locator("span.instructions").nth(0)).to_have_text("Enter a name that describes your listing, e.g., 'Rose Cottage'")
    expect(page.locator("span.instructions").nth(1)).to_have_text("Describe the features and atmosphere of your listing, e.g., 'A cozy cottage with a beautiful garden view.'")
    expect(page.locator("span.instructions").nth(2)).to_have_text("Specify the nightly rate for renting this listing.")

# Test submit button
def test_submit_button(page, test_web_address):
    page.goto(f"http://{test_web_address}/add_listing")
    submit_button = page.locator("input[type='submit']")

    expect(submit_button).to_be_visible()
    expect(submit_button).to_have_value("Add My Listing!")


# def test_post_add_listing(page, test_web_address):
#     page.goto(f"http://{test_web_address}/add_listing")

#     page.click("text= Add new listing")
#     page.fill("input[name=title]", 'Test Listing')
#     page.fill("input[name=description]", "Test description")
#     page.fill("input[name=price_per_night]", "100")
#     page.click("text=Add listing")
    # complete when you know what home page looks like



# renders the request a booking page with correct title
def test_get_request_booking_page(page, test_web_address):
    id = 1

    page.goto(f"http://{test_web_address}/request_booking/{id}")

    h1_tag = page.locator("h1")

    # We assert that it has the text
    expect(h1_tag).to_have_text("Request a booking")

# checks for correct listing information - name, description, price
def test_get_listing_information(page, test_web_address):
    id = 3

    page.goto(f"http://{test_web_address}/request_booking/{id}")

    listing_name = page.locator("p").nth(0).inner_text()

    description = page.locator("p").nth(1).inner_text()

    price = page.locator("p").nth(2).inner_text()

    expect(listing_name).to_have_text("Listing name: Seaside Serenity")
    expect(description).to_have_text("Description: A peaceful coastal retreat with stunning ocean views, a private balcony, and luxurious modern amenities.")
    expect(price).to_have_text("Price per night: £100")
