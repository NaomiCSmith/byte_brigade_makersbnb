from playwright.sync_api import Page, expect

# Tests for your routes go here

"""
We can render the home page
"""
def test_get_home(page, test_web_address):
    # We load a virtual browser and navigate to the /home page
    page.goto(f"http://{test_web_address}/home")

    # We look at the <p> tag
    p_tag = page.locator("p")

    # We assert that it has the text "This is the home."
    expect(p_tag).to_have_text("This is the home.")

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
    expect(page.locator("label[for='price']")).to_have_text("Price per Night (GBP)")

    expect(page.locator("span.instructions").nth(0)).to_have_text("Enter a name that describes your listing, e.g., 'Rose Cottage'")
    expect(page.locator("span.instructions").nth(1)).to_have_text("Describe the features and atmosphere of your listing, e.g., 'A cozy cottage with a beautiful garden view.'")
    expect(page.locator("span.instructions").nth(2)).to_have_text("Specify the nightly rate for renting this listing.")

# Test subbmit button
def test_submit_button(page, test_web_address):
    page.goto(f"http://{test_web_address}/add_listing")
    submit_button = page.locator("input[type='submit']")

    expect(submit_button).to_be_visible()
    expect(submit_button).to_have_value("Add My Listing!")

def test_post_new_listing(page, test_web_address):
    page.goto(f"http://{test_web_address}/home")
    page.click("text=Add a property")

    page.fill("input[name=name]", 'Test Listing')
    page.fill("input[name=description]", "Test description")
    page.fill("input[name=price]", 100)
    page.click("text=Add My Listing!")

    expect(page.locator("h1").nth(3)).to_have_text("4: Test Listing")

    page.click("text=4: Test Listing")

    expect(page.locator("h1")).to_have_text("4: Test Listing")
    expect(page.locator("h2")).to_have_text("4: Test Listing")
    expect(page.locator("h3")).to_have_text("4: Test Listing")
    # complete when you know what home page looks like
#     page.click("text= Add new listing")
#     page.fill("input[name=title]", 'Test Listing')
#     page.fill("input[name=description]", "Test description")
#     page.fill("input[name=price_per_night]", "100")
#     page.click("text=Add listing")
    # complete when you know what home page looks like


# test home listings
"""
GET /home
When: I open up the home
Then: I receive a list of all listings in the repository
"""
def test_get_listings(db_connection, page, test_web_address):
    db_connection.seed("seeds/makersbnb.sql")
    page.goto(f"http://{test_web_address}/home")
    div_tags = page.locator("div")
    expect(div_tags).to_have_text([
      "1: Alpine Retreat Lodge",
      "2: City Chic Loft",
      "3: Seaside Serenity"
    ])
