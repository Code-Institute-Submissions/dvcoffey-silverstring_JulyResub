# Silverstring

The live website can be found [here](https://silverstring.herokuapp.com/).

Silverstring is an online ecommerce platform dedicated providing customers with guitars and guitar accessories. 

## Testing

Documentation on user stories, testing and deployment can be found in TESTING.md

## UX

This website is designed with these users as the focus.

### Visiter

### Shopper

### Store Owner

The Administrator has full control over the database.

## User Stories

This website is designed with these users as the focus.

As a/an| I want to be able to | So that I can | Addressed
------- | -------- | ------- | ------
Shopper | View a list of products | Select some to purchase | Shop link displays product listings
Shopper | View individual product details | See the price/description/rating/| Clicking on product card in product listings displays product details
Shopper | View the total of my purchases at any time | adjust my purchases accordingly | Clicking on the "shopping cart" icon displays the current total and allows for users to update/remove the quantity of items
Site User | Register for account | Have an account/view my profile | Registration can be accessed by clicking account icon
Site User | Login/logout | Access my account | Option to login/logout on clicking "person" icon
Site User | Have a personalised user profile | View order history/save payment info | Profile page available after login, shows order history/payment info
Site User | See upcoming events | View the catalogue in person | Showcase page lists upcoming events and information
Site User | Leave a review | Let other user know of the quality of a specific product | Product details page contains form input to leave a review
Site User | See product reviews | Learn of other customers experiences with a specific product | Product details page contains list of product reviews
Shopper | Search for a product | Find a specific product | Search form included in store page, can search by name/description
Shopper | See what I've searched for | Quickly decide if what I want is there | Search form filters results by search criteria
Shopper | Select qty of product when purchasing | Ensure I don't select wrong quantity| Qty selector forms included on product details page
Shopper | View cart | See total cost/all items  |  Clicking "bag" icon, lists products, total cost and subtotals.
Shopper | Adjust qty of items in my cart | Make changes to the cart before checkout |  update/remove is available in the cart
Shopper | Enter payment info | Checkout | Payment info can be filled in on checkout page
Shopper | View an order confirmation after checkout | Verify the order | Order confirmation appears on profile page 
Store Owner | Add a product | Add new items to store | Admin user is able to add products via Product management
Store Owner | Edit/update a product | Change product details | Admin user is able to edit products via product/product detail pages
Store Owner | Delete a product | Remove items not for sale | Admin user is able to delete products via product/product detail pages

## Strategy

This site is primarily a B2C wesite, and proof of concept for a working ecommerce platform.
The goal is to provide the user with an intuitave experience, and the ability to browse and purchase instruments online.


## Scope

Visitors should be provided with enough information quickly to determine that this is an online shop.
The user will be able to navigate the site via the navbar.
They will be able to make a profile and  leave a review on products.
They will be able to make a purchase using a credit card.
The user will be able to view upcoming showcases where they can see the products in person.
The admin will have the ability to update the store.


## Structure

The Logo/Brand is always visible at the top left of the page, in the navbar and will verify for the user that they are in the right place.
This also acts as a home button which will redirect the user back to the homepage.
The homepage will appear first with the navbar providing the user to other pages on the site.
On mobile devices the navbar links will be available to the right via a dropdown 'hamburger' icon.

### Three instances of the navbar

#### For the visitor.

1. Home
2. Shop
3. Showcase
4. Account (Login/Register)
5. Cart

#### For the registered user (logged in).

1. Home
2. Shop
3. Showcase
4. Account (My Profile/Logout)
5. Cart

#### For the Administrator (logged in).

1. Home
2. Shop
3. Showcase
4. Account (My Profile/Product Management/Logout)
5. Cart

### The following pages cannot be accesed via the nav bar.

1. Update Product
2. Delete Product

These are only accesible to the site admin via the products and product details page.

### The Collapsible Navbar.
The Navbar will collapse on mobile devices to fit smaller screens.
Navbar links can be accessed via a dropdown menu.

## Skeleton

The following schema was drawn using Draw SQL
https://drawsql.app/

<img src="static/schema/schema.png">


## Surface



## Features

#### Responsiveness

The site scales relatively well from small screens to large.
Some issues can be found  however. These will be discussed in the testing section.

#### Logo/Home Button

The logo is present at all times at the top left of the page. 
It does not take up a large amount of space, but is prominent across the site and provides the user with a link to back to the homepage at all times.

#### Navbar

The user can navigate the site using the navbar.
The navbar will collapse on mobile devices and can bia accessed via a 'hamburger icon'. 

#### Homepage

The hmepage simply contains a hero-image and a text blerb.


#### Store Page

By clicking on the 'Shop' link in the navbar the user will be brought to the product directory page.
This will list all of the products in the database.
Alternatively the user will be brought here with the games filtered by the methods specified above.
The store page contains a search bar which allows the user to search for an item via a text input
The Store page also contains dropdown filters which allow the user to filter the store by category

##### The Categories include
- Electric Guitars, Electric Guitar Strings, Electric Guitar Accessories
- Acoustic Guitars, Acoustic Guitar Strings, Acoustic Guitar Accessories
- Bass Guitars, Bass Guitar Strings, Bass Guitar Accessories


#### Showcase Page

The Showcase Page consists of a table listing the upcoming events including the Location, Date, Time and Admission Fee

#### Account

The account icon will trigger a dropdown menu for the following options

#### Register

New users can register an account with a username and password. 

#### Log in 

Users who already have an account can log in here using their username and password.

#### Log out

Logged in users can log out here.

#### Product Management

This is is only visible to the admin.
It provides a link to the Add Product Page.

#### Add Product Page

The add product page provides the admin with a form where they can input the product fields such as name, description, image, price.
The product can then be added to the store.

#### Product Details

User can view the products full details by clicking on a product card from either in the store page.
This will contain the product's image, description, and the ability to either add the item to the cart or continue shopping.
This page also contains the review section whereby users can see reviews left by visitors, or add their own if they are logged in to a registered account

#### Edit/Delete

Only visible to the admin on the product card or in the product details page.
The delete button will delete the itemn from the database.
The edit button will direct the admin to the update product page where they can alter the products details and price

#### Cart

The cart allows the user to see the items they have clicked to purchase.
Items can be removed, and quantities can be updated here before proceeding to the checkout

#### Checkout

The Checkout will provide users with the ability to input their billing information and purchase the item.
The billing information can also be save to the user profile so that they don't need to fill the form fields every thime a purchase is made.

## Technologies Used

- [HTML5](https://en.wikipedia.org/wiki/HTML5)
    To provide the base structire of the web pages


- [CSS3](https://en.wikipedia.org/wiki/CSS3)
    To provide the styling of pages 


- [Bootstrap](https://www.getbootstrap.com/)
    To simplify page layout and use of classes for simpler styling


- [Javascript](https://www.javascript.com/)
    To provide the site interactivity


- [jQuery](https://jquery.com/)
    Simplifies interactive web design.

- [Font Awesome](https://fontawesome.com/)
    Provides the icons used across the site
    
- [Google Fonts](https://fonts.google.com/)
    Provides the fonts used across the site

- [Gitpod](https://www.gitpod.io/)
    provides the development environment

- [GitHub](https://www.github.com/)
    hosts the files uploaded during production

- [Heroku](https://www.heroku.com/)
    A cloud platform for hosting the app.

- [Amazon Web Services](https://aws.amazon.com/)
   For storing image files and css

- [Django](https://www.djangoproject.com/)
    An open-source Python framework that is designed for quick launches.

- [Stripe](https://www.stripe.com/)
    For processing card payments

- [Paint.net](https://www.getpaint.net/)
    For designing the wireframes and editing images used across the site.


## Sources and acknowledgements

The images and data for each product in this project were sourced on thomann.de.

The hero image was sourced from https://stephenarnoldmusic.com/sonic-branding/harp-guitar-banner/

https://www.w3schools.com/ was used for fast queries, mainly to check syntax and css parameters.

The Code Institute provided most of the educational resource required to build this project and this project is modelled heavily on the Boutique Ado Walkthrough project

Stack Overflow contained many helpful threads which were queried during development.

The Slack community and my fellow students at code institute for providing ispiration and assistance.

This website is built purely for educational purposes.