## User Stories

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

## Manual Testing

-The logo and home links are functioning correctly and lead the user to the home page.

-The store link leads the user to the store page and displays the products appropriately 

-The Navbar and Nav padding change state at the appropriate screen sizes

-Users can access the showcase page via the Navbar

-The dropdown account menu items appear for the appropriate users and direct them to the correct pages.

-The cart icon will navigate the user to the cart, If the cart is empty it was display as such and provide a link for the user to return to the store page.

-If the cart has content the users can navigate to the checkout page.

-The user can effectively update and remove items from the cart.

-The checkout form will save data to the user profile if the checkbox is selected.

-The logout and log in pages function appropriately

-The edit/Delete buttons appear only for the admin and not a regular user

-Stripe payments function appropriately

#### The review functionality is not working and has been disabled. 
##### This is a problem I could not fix, I spent too much time trying to get it to work.
##### This time was intended for improving the readme, testing, proper code indentation and code comments
##### The automated email service has not been implemented for the same reason
 

## Deployment

### preparation
-Go to aws.amazon.com to and register an account
-Create a new bucket to store the media files/css
-Go to stripe.com to reveal your keys there

This website is deployed on [Heroku](https://www.heroku.com/), following these steps:
- Install the following packages to your local environment.
- [gunicorn](https://gunicorn.org/): `gunicorn` 
- [gninx](https://www.nginx.com/): `gninx` 
- [psycopg2-binary](https://pypi.org/project/psycopg2-binary/): 
- [dj-database-url](https://pypi.org/project/dj-database-url/): 
- type `pip3 freeze > requirements.txt` in the terminal to add the installed packages to the requirements.txt.
- Create a `Procfile` write `web: gunicorn silverstring.wsgi:application` in the file.
- `git add` and `git commit` and `git push` all the changes to the Github repositoty of this project.
- Create a new app in Heroku. Select the nearest region and click **Create app**.
- In Heroku navigate to  **Resources** , then **Add-ons** and find **Heeroku Postgres**, select **Hobby Dev — Free** and click **Submit Order Form** to add it to your project.
- Navigate back to the  Heroku Dashboard and click on **Setting** > **Reveal Config Vars** to set the following values:

AWS_ACCESS_KEY_ID:	Your AWS Access Key
AWS_SECRET_ACCESS_KEY: 	Your AWS Secret Access Key
DATABASE_URL: 	Your Postgres Database URL
SECRET_KEY: 	Your Secret Key
STRIPE_PUBLIC_KEY: 	Your Stripe Public Key
STRIPE_SECRET_KEY: 	Your Stripe Secret Key
STRIPE_WH_SECRET: 	Your Stripe WH Key
USE_AWS: 	True

- Migrate the database models to the Postgres database using the following commands in the terminal: python3 manage.py migrate
- Create a superuser for the Postgres database using the following command: python3 manage.py createsuperuser
- Install boto3 and django-storages via the terminal to connect AWS S3 bucket to Django.
- Freeze to requirements.txt
- Add the following in settings.py.
 
if 'USE_AWS' in os.environ:
    # Cache Control
    AWS_S3_OBJECT_PARAMETERS = {
        'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
        'CacheControl': 'max-age=94608000',
    }

    # Bucket Config
    AWS_STORAGE_BUCKET_NAME = 'kaur-health'
    AWS_S3_REGION_NAME = 'eu-west-1'
    AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3-eu-west-1.amazonaws.com'

    # Static and media files
    STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    STATICFILES_LOCATION = 'static'
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
    MEDIAFILES_LOCATION = 'media'

    # Override static and media URLs in production
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'

    # Roots
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

- In Heroku enable automatic deployment from github
- Push all changes using git push heroku master.
