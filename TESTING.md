## Testing

### Links

-The logo and home links are functioning correctly and lead the user to the home page.

-The store link leads the user to the store page and displays the products appropriately 

-The Navbar and Nav padding change state at the appropriate screen sizes

-Users can access the showcase page via the Navbar

-The dropdown account menu items appear for the appropriate users and direct them to the correct pages.

-The cart icon will navigate the user to the cart, If the cart is empty it was display as such and provide a link for the user to return to the store page.

-If the cart has content the users can navigate to the checkout page.

### Cart

-The user can effectively add, update and remove items from the cart.

-The continue shopping and secure checkout buttons are functioning correctly 

### Accounts

-The checkout form will save data to the user profile if the checkbox is selected.

-The logout, log in, register and reset password pages function appropriately

-The edit/Delete buttons appear only for the admin and not a regular user

-Stripe payments function appropriately

-Allauth templates have been Refactored and appropriate fields can be reached.

-Fields and links are functioning correctly


### Emails

-Emails are effectively being sent when:
-A new account is registered to confirm email, link in email is functioning
-a password is reset, link in email is functioning
-A product is ordered, a confirmation email is received

### Payments

-Payments can be seen as processed correctly using stripe webhooks

### Scalability

-The checkout and cart screens did not scale well on mobile devices which rendered payment impossible, this has been refactored and now all elements of the screen are accessible.

-The showcase page has a slight overflow on small '320px" devices, it can be scrolled easily however.

-The navbar collapses correctly on mobile devices

-I would like the cart to be more apparent on mobile devices as it is collapsed into the navbar, this  is an unforseen design flaw

### Reviews

- Reviews can be added and will appear on the product page.
(This was my greatest issue during this project and took up a lot of time which I would like to have spent making the overall UX nicer.
It was a migration issue which I had to contact tutor support to help with).

- A product can be deleted by the admin even if it has reviews attatched

### Admin 

-The product management( add, edit and delete ) will not appear for standard users, only the admin.

-The add, edit and delete functions are working appropriately.
