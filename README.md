# Dry Drops

Dry Drops is an e-commerce website operating in the field of alcohol-free beverages.

This fully responsive website was built using the Django framework in Python.

The payment system uses a service called Stripe. To test this system, dummy card details can be used. A list of these can be found [here](https://stripe.com/docs/testing#cards).

![Responsive](assets/images/responsive.png)

## User Experience (UX)

A list of my user stories and their tasks can be found [here](https://github.com/delboy/drydrops/issues).

### EPIC | Navigation
- As a shopper, I can navigate around the site so that I can easily view the desired content.
- As a shopper, I can view a list of products so that I can choose what products to purchase.
- As a shopper, I can click on a product to see its details so that I can view the description, price and any customer reviews.
- As a shopper, I can easily identify different product categories so that I can quickly view the type of products I'm looking for.
- As a shopper, I can search for products so that I can find the products I'm specifically looking for.
- As a shopper, I can sort the products so that I can easily find products based on price, reviews, category, or title.
- As a shopper, I can view products I have saved so that I can navigate to them easily without having to find them again.

### EPIC | Accounts
- As a User, I can register for an account so that I can use the features afforded to members.
- As a user, I can receive a confirmation email when creating an account so that I know the registration was successful.
- As a user, I can easily log in and out so that I can access my account.
- As a user, I can easily see my login status so that I know if I'm logged in or out.
- As a user, I can view my previous orders so that I can keep a record of what purchases I've made.
- As a user, I can save my delivery information so that I do not have to refill it out for future orders.
- As a user, I can recover my password in case I forget it so that I can regain access to my account.

### EPIC | Admin
- As an admin, I can add products so that I can update the site's inventory.
- As an admin, I can edit a product so that I can keep the products information up to date.
- As an admin, I can delete a product so that I can remove products no longer available.
- As an admin, I can feature products so that I can display them on the home page.

### EPIC | Purchasing
- As a shopper, I can add items to my bag in different quantities so that I can store the items until I'm ready to buy.
- As a shopper, I can view my bag so that I can identify the total cost of the transaction and the items I will be purchasing.
- As a shopper, I can adjust the quantity of the items in my bag so that I can easily make changes before I purchase.
- As a shopper, I can always see a running subtotal so that I can keep an eye on how much I'm spending.
- As a shopper, I can see a summary of my purchase before I buy so that I know exactly what I'm ordering and how much it all costs.
- As a shopper, I can pay for goods as a guest so that I can still use the site without having to sign up for an account.
- As a shopper, I can easily enter my payment details so that I can checkout quickly with no problems.
- As a shopper, I can view confirmation of my purchases so that I know the order was received and can review what I've purchased.
- As a shopper, I can receive an email of my order so that I can keep it for my records.


### EPIC | Interaction
- As a user, I can save my favorite products so that they are easily accessible for future purchases.
- As a user, I can leave reviews on products so that I can share my experience with others.
- As a user, I can sign up for the website's newsletter so that I can keep up to date with new products and promotions.
- As a user, I can connect to the site's social media pages so that I can follow them and keep up to date with their products and promotions.
- As a user, I can contact the business so that I can find out any information that I require.

## Design

### Colour Scheme

- I wanted the color scheme to be similar to the color of dark ales and wines to fit in with the site's theme, so the main color I chose was a dark reddish-brown, along with a lighter shade and a couple more neutral tones to balance it out.  

 ![Colour Scheme](assets/images/colour-scheme.png)

### Typography 

I will be using two fonts from Google Fonts.
- Imbue for the logo and headers.
- Roboto Serif for paragraphs and general text.

### Imagery

### Wireframes

Wireframes for each page are linked here:

* [Home Page](assets/documents/home.pdf)
* [Products](assets/documents/products.pdf)
* [Product Details](assets/documents/product-details.pdf)
* [About](assets/documents/about.pdf)
* [Contact](assets/documents/contact.pdf)
* [Register](assets/documents/register.pdf)
* [Account](assets/documents/account.pdf)
* [Sign in/out](assets/documents/log.pdf)
* [Bag](assets/documents/bag.pdf)
* [Checkout](assets/documents/checkout.pdf)
* [Success](assets/documents/success.pdf)
* [Product Management](assets/documents/product-management.pdf)

### Database Schema

![Database Schema](assets/images/schema.png)

### Search Engine Optimisation

The purpose of the About Us page was not so much designed in mind to inform the user, but more so to have an opportunity to use some keywords, and link the user to any other relevant website, all to help boost the site's ranking in search engine results. 

The initial keywords and phrases I came up with were:

## Short Tail Keywords
- Alcohol-Free
- Teetotal Drinks
- 0% Alcohol
- Zero Alcohol
- 0% Beer/Wine/Cider/Spirits
- Dry Drinks
- Low alcohol
- No alcohol
- Halal drinks
- Quitting Alcohol

## Long Tail Keywords
- Drinks for quitting alcohol
- Drinks for designated drivers
- Drinks for recovering alcoholics
- Alcohol-free beverages
- Alcohol-free drinks for pregnant women
- Drinks that are suitable for people practicing sobriety
- Drinks that are suitable for people who are straight edge

These phrases can also be used in the metadata at the head of the page.

## Features

### Nav Bar

- #### Links
    - To help navigate the user around, four links to the main sections of the site are present at the top of every page.
    - The links collapse into a hamburger menu once the screen size becomes too small to fit all the elements comfortably. 
    - The link to the current page will be highlighted by an underline to help users understand what page they are on.
    - The Shop link drops down into a sub-menu where the user can navigate to all products or choose from one of the four product categories.

    ![Navbar-Links](assets/images/navbar-links.png) 

- #### Search Bar
    - The search bar is located in the middle of the navbar and can be used to search all products.
    - Using the search bar will search both the product's title and description for a match.
    - On smaller screens, the bar collapses into a search Icon that upon clicking drops down into the full search bar.

    ![Navbar-Search](assets/images/navbar-search.png) 

- #### Account
    - Located on the right side of the navbar is the account Icon where the user can manage their account.
    - Clicking the account Icon opens a dropdown menu with options for the user to register or sign in.
    - If a user is signed in the dropdown options change to 'My Profile' and 'Logout'.
    - If a user is signed in the Icons text changes from 'sign in/up' to 'My Account'.
    - If the user signed in is a super user then a third option of 'Product Management' is available. 

    ![Navbar-Account](assets/images/navbar-account.png) 

- #### Bag
    - Located on the right side of the navbar next to the accounts menu is the bag Icon.
    - Beneath the bag icon users can find a running total of the cost of all the items in their bag.
    - Once a product is added to the bag, a number displaying the total quantity of items appears, located at the top right of the bag icon.
    - Clicking the bag icon navigates the user to the shopping bag page which displays a summary of what's been added.

    ![Navbar-Bag](assets/images/navbar-bag.png)

- #### Banner 
    - A banner running across the top of the navbar informs the user of any current offers.
    - The banner message will change to reflect how close the user is to achieving the offer.
    - The banner sticks to the top of the page at all times to keep the user constantly aware of how far they are from achieving the offer. 

    ![Navbar-Banner](assets/images/navbar-banner.jpg)


### Home Page
    
- #### Hero Image
    - The hero image welcomes the user with a short message advertising what the site sells along with the website's slogan.
    - A message informing the user that they receive free delivery on their first order when if sign up is also present.
    - A button labeled 'Shop Now' takes the user to the products page.
    - The image will change depending on the size of the screen.

    ![Hero-Image](assets/images/home-hero.png)
    
- #### Categories
    - The categories section lists the four categories of products that are stocked.
    - Clicking one of the categories takes the user to the shop displaying only products from that category. 

    ![Hero-Categories](assets/images/home-categories.png)

- #### Top Products
    - The Top products section lists the top 4 products based on customer reviews.
    - The list will order by the highest rating first. If any products have the same rating they will be put in order of how many reviews they have received.   

    ![Hero-Top-Products](assets/images/home-top-products.png)

- #### Footer 
    - The footer appears at the bottom of every page.
    - The footer is broken up into 4 sections. The logo, quick links, Contact Us, and Newsletter.
    - The Quick Links section has links to all parts of the site.
    - The Contact Us section lists the company's address, phone number, email and social media account.
    - Clicking the phone number will call it, clicking the email address will open your default email programme and clicking the social media links will take you to the relevant website.
    - The Newsletter section has an option to input your email and sign up for the weekly newsletter.

    ![Footer](assets/images/footer.png)

### Accounts

- #### Register Page
    - The register page is used to create an account.
    - Once submitting the form an authentication link will be emailed to the address the user provided. 

    ![Accounts-Register](assets/images/accounts-register.png)

- #### Login Page
    - The login page is used to log in users with an existing account.
    - A Forgot Password link is also present that enables users to recover their password.

    ![Accounts-Login](assets/images/accounts-login.png)

- #### Log out Page
    - The logout page is used to log out users who are signed in.

    ![Accounts-Logout](assets/images/accounts-logout.png)

### Profile

- #### Delivery Details
    - The delivery details section stores the user's delivery address and phone number.
    - The information provided here is used to autofill the delivery address when placing an order.

    ![Profiles-Delivery](assets/images/profiles-delivery.png)

- #### Order History
    - The order history section is a table that keeps a record of every order the user has placed.
    - The table displays the order number, date it was ordered, items ordered, quantities of items and the order total.
    - Clicking the order number will take the user to a more detailed summary of the order.
    - A scroll bar appears once the user has more orders than the box can contain. 

    ![Profiles-Order-History](assets/images/profiles-order-history.png)

- #### Favorite Items
    - The favorite items section keeps a list of all products that the user has liked.

    ![Profiles-Favorites](assets/images/profiles-favourites.png)

### All Products

- #### Categories Side-nav
    - The category side-nav section only appears on large screens and lists all the product categories.
    - Clicking any of the categories in this section filters the products to that option.

    ![Products-Sidenav](assets/images/products-sidenav.png)

- #### What's Hot Carousel
    - The Whats hot carousel displays any product that an admin has selected to be featured.
    - Clicking the product will take the user to that product's detail page.
    - Buttons on the edge of the carousel enable the user to scroll through all the featured products.

    ![Products-Whats-Hot](assets/images/products-whats-hot.png)

- #### Sorting
    - The sort-by box is located to the top right of the products section on medium and large screens, and centered on smaller screens.
    - Clicking the box opens up a dropdown menu with various options on how to sort the products. 

    ![Products-sort](assets/images/products-sort.png)

- #### Products
    - The products page is fully responsive, adjusting how many products are on each row depending on the user's screen size.
    - Each product card shows an image of the product, its title, price, category, and rating.
    - An 'Add to Bag' button can be used to add the item to the bag.
    - Any products that have been liked by the user displays a red heart in the top right corner. 
    - If the user is a superuser, admin buttons will appear at the bottom of the product card.
    - If the user is a superuser and the product has been featured, a featured banner will appear across the product card. 

    ![Products-Products](assets/images/products-products.png)

### Products Details

- #### Product Info
    - The product info section shows information about the product along with buttons to add the item to the user's favorite list, and buttons to add the item to the bag in multiple quantities.
    - The product's rating is an average of all the product's reviews and displays the result in stars. Next to the stars is also a number indicating how many reviews the product has received in total. 
    - Clicking the products category will take users to the products page showing only items from that category.
    - If the user is a super user, admin buttons will appear underneath the image.

    ![Products-Product-Info](assets/images/products-product-info.png)

- #### Like Button
    - The like button is located underneath the product's title.
    - The heart button renders as empty if either the user is signed out or the product is not liked by the user.
    - Liking a product fills in the heart and adds the product to the user's favorite items list on their profile page.
    - Unliking a product unfills the heart and removes the product from the user's favourite items list on their profile page.
    - If the heart is clicked when no user is signed in, an 'Account Required' modal pops up informing the user that they need to either sign in or create an account to use that feature.
     
    ![Products-Like](assets/images/products-like.png)

- #### Quantity Buttons
    - The quantity buttons are located underneath the product details and are used to add items to the bag.
    - The plus and minus buttons increase and decrease the input value. 
    - If the value is set to 1 the minus quantity will be disabled. Respectively if the value is set to 99 the plus button is disabled.
    - Clicking the 'Add to Bag' button takes the number in the input field and adds that amount of products to the bag.
    - Trying to add an amount less than one or above 99, renders an error message informing the user of the parameters needed to be successful.
    - Underneath the input is a link that takes users back to the store.  

    ![Products-Quantity-Button](assets/images/products-qty-btns.png)


- #### Customer Reviews
    - If the product has received any reviews they will appear underneath the product details.
    - The reviews consist of the number of stars awarded by the user, their written comment, followed by the user name and how long ago the comment was left.
    - If the user is signed in and they have left a review on a product, that review will also have edit and delete buttons. Users can use these to manage their reviews.

     ![Products-Reviews](assets/images/products-reviews.png)

- #### Add Review
    - The add review form is located next to the product's reviews on large screens or underneath on small screens.
    - The form consists of two fields, rating and review.
    - Leaving out either the rating or the review notifies the user that the fields are required.  
    - The user can rate the product between 1 and 5 stars. Clicking a star fills the star and every star before it.
    - Any profanity in the review will cause the form to fail and a toast will inform the user.
    - To stop users leaving multiple reviews on one product, the form only renders when no reviews for that product, from that user exist.

    ![Products-Add-Review](assets/images/products-add-review.png)

### Product Management

- #### Add Product
    - The add product page is accessed by the account dropdown menu, under product management. It is only accessible by superusers.
    - The form lists all the necessary fields to create a new product. 
    - The user must fill out all the fields that are labeled 'required' with an Asterix. If the form is submitted with any of these fields left blank then an error message will appear above that particular field, notifying the user of the issue.
    - The SKU field must be unique. An error message will appear if an already existing SKU is attempted.
    - If a price is added with more than 6 digits the form will fail and an error message will appear under the price field.
    - The featured checkbox can be checked so that the item will appear in the 'What's Hot' section on the products page.
    - The user has the option to add an image. If none is chosen then a default image is used.
    - Clicking the 'Add Product' button at the bottom of the form will create the product providing there are no errors on the from.

    ![Products-Management-Add](assets/images/product-management-add.png)

- #### Edit Product
    - The Edit Product page can be accessed from two places. By clicking the 'edit' button at the bottom of the product's card. Or by clicking the edit button located under the image on the products detail page.
    - Accessing the page loads what is essentially the add product page, with the details of the product already filled in. 
    - The image field displays a thumbnail of the current image and has a checkbox option to remove it. Checking this will change the image to the default image.
    - Clicking the 'Update Product' button will save any changes made to the existing product.  

    ![Products-Management-Edit](assets/images/product-management-edit.png)

- #### Delete Product
    - The Delete Product button can be found in two places. One is next to the 'edit' button at the bottom of the product's card. The second is to the right of the 'edit' button on the products detail page. 
    - Clicking either of the delete buttons will bring up a warning modal, asking the user if they are sure they want to delete the product, and informing them that it is irreversible. 
    - Once the warning modal has been activated if the user then clicks the delete button the product will be removed from the database. 
    - If however, the user presses the cancel button, the modal is closed and no effect has taken place. 

    ![Products-Management-Delete](assets/images/product-management-delete.png)

### Bag

- #### Items
    - The bag page displays all items that the user has added to it. 
    - The page will list the items added with its image, followed by its title and SKU.
    - Clicking either the image or the product's title will take you to that product's detail page. 

    ![Bag-Items](assets/images/bag-items.png)

- #### Quantity and Price
    - The price and quantity section has three elements, the product's price, the quantity in the bag, and the subtotal of that item's line.
    - The quantity element has buttons either side for the user to increase or decrease the total of that item in the bag.
    - The minus quantity button will be disabled if the quantity of the item is one. Respectively the plus button will also be disabled if the quantity of the item is 99.
    - Next to the subtotal on large screens, or under the input buttons on smaller screens, is the update and delete buttons.
    - Clicking the 'update' button saves any changes to the quantity and updates the item's subtotal.
    - Clicking the red trash can icon removes the item completely from the user's bag. 
    - Manually inputting the number zero or anything below and clicking 'update' will remove the item from the bag. 
    - Manually inputting a number above 99 and clicking 'update' will result in an error message informing the user of the correct parameters. 
    
    ![Bag-Qty-Price](assets/images/bag-qty-price.png)
    
- #### Totals and messaging
    - At the end of the line items is a summary of the costs.
    - The summary features the bags total, delivery charges and the grand total to pay.
    - In between the bag total and the delivery total, users will either find a message informing them of how much more they need to spend to receive free delivery, or it will show how much delivery they would of paid if they didn't receive the offer. This message will also be different if it is the user's first ever order, in which case it will display 'FREE DELIVERY on your first order!'. 
    - Beneath the grand total is two buttons. From here the user can either continue to the checkout or return to the products page by clicking 'Continue Shopping'.

    ![Bag-Qty-Totals](assets/images/bag-totals.png)

### Checkout

- #### Details
    - The details section appears on the left on large screens or underneath the order summary on smaller screens.
    - Here the user fills out his or her contact details, delivery address, and card number.
    - If the user is anonymous, a link to create an account or login will be present.
    - If the user is signed in a checkbox to save the delivery information can be checked.
    - If the user is signed in and has delivery information checked the delivery details and email address will be automatically filled in. 
    - Any field with an Asterix is required. If a user tries to complete the form with any of these fields left blank the affected field will highlight that it needs to be filled in.   

    ![Checkout-Details](assets/images/checkout-details.png)

- #### Order Summary
    - The order summary section appears on the right on large screens or at the top on smaller screens. 
    - This section lists all the items about to be purchased, along with the quanity, subtotal and a grand total.
    - Next to the order summary title will be a number reflecting the total number of items that appear in the order. 
    - Clicking the image or title of any items in the summary will take the user to that product's detail page. 

    ![Checkout-Order-Summary](assets/images/checkout-order-summary.png)

- #### Payment
    - Underneath the delivery details is the card payment box which is run by [Stripe](https://dashboard.stripe.com/login). 
    - Only numbers can be entered card payment box and incorrect card numbers will automatically show an invalid card number error.
    - The site can be tested by using the dummy card number 4242 4242 4242 4242 with the expiry date 04/24 and the CVC code 242.
    - At the end of the section is a button to complete the order or to return back to the bag. There is also a warning message informing the user of how much their card is about to be charged.

    ![Checkout-Payment](assets/images/checkout-payment.png)


- #### Loading Spinner
    - Upon clicking the complete order button, as long as the form is valid, a loading spinner will render until the information is processed completely. 
    
    ![Checkout-Spinner](assets/images/checkout-spinner.png)

- #### Confirmation 
    - Once the order has been processed the user is taken to the checkout success page.
    - This page summarises the completed order. It lists the order number, order date, the items ordered with their quantities, the delivery address, and the billing info. 
    - A confirmation email is also sent to the email address provided, and this is noted at the top of the page. 
    - At the end of the summary is a button that the user can use to take them back to the main shop.99
    
     ![Checkout-Confirmation](assets/images/checkout-confirmation.png)

### About Us

- #### Image
    - The about us page features an image of the fictional founder of Dry Drops, Jack Daniels.
    - Underneath the image is a link to both the contact us page, and the products page.

    ![About-us-image](assets/images/about-us-img.png)

- #### Bio
    - The bio section runs next to the image, or underneath if on a small screen.
    - The bio gives a fictional account of how Dry Drops was founded. This was used to create an opportunity to use keywords related to the site's business to help boost search ratings.

    ![About-us-bio](assets/images/about-us-bio.png)

- #### Links
    - At the bottom of the page are links to 3 different alcohol and substance abuse charities.
    - These links were included to increase the search rating of the website. 
    - Hovering over these links will lighten their appearance.
    - Clicking the links will open up the respective website in another tab. This is to stop the user from being taken away from the main site.  

    ![About-us-links](assets/images/about-us-links.png)

### Contact

- #### Contact Info 
    - The contact info has all of Dry Drops contact information, including their address, phone number, email address and social media links. 
    - Hovering over the social media links changes their color. Clicking the links takes you to the respective website which opens in a new tab.
    - The facebook link particularly takes you to the websites business page on facebook. 

    ![Contact-info](assets/images/contact-info.png)

- #### Messaging
    - The message section enables the user to send an email directly to dry drops.
    - All the fields are required. Failing to fill out any field will result in a message highlighting which field has been left blank.
    - Once all the fields are completed, hitting the 'Send Message' button will send the message. 
    - Both Dry Drops and the user will receive an email on completion, laying out who send the message and what was said.  

    ![Contact-Messaging](assets/images/contact-msg.png)

### Toasts and Pop-ups

- #### Toasts
    - Toasts appear in the top right-hand corner of the display informing the user of any actions they have performed.
    - The bottom right corner of the toast box will change color depending on whether the message is portraying a successful action, general info, warning, or an error. 

    ![Toast](assets/images/toast.png)

- #### Pop-ups
    - If there is no user signed in, the session is new, and 8 seconds elapse, a pop-up will appear one time.
    - The pop-up message informs the user of the free delivery offer to new user's first order and has a link to the registration page. 

    ![Pop-up](assets/images/pop-up.png)

## Technologies

### Languages used

- [HTML5](https://en.wikipedia.org/wiki/HTML5)
- [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
- [Javascript](https://en.wikipedia.org/wiki/JavaScript)
- [Python](https://www.python.org/)

### Libraries and Programs Used

- [Git](https://git-scm.com/)
    - Version control.
- [GitHub](https://github.com/)
    - For storing code and deploying the site.
- [Gitpod](https://www.gitpod.io/)
    - Used for building and editing my code.
- [Django](https://www.djangoproject.com/)
    - A python based framework that was used to develop the site.
- [Bootstrap](https://getbootstrap.com/)
    - For help designing the html templates.
- [Google Fonts](https://fonts.google.com/)
    - Used to style the website's logo.
- [Font Awesome](https://fontawesome.com/)
    - Used to obtain the icons used.
- [Google Developer Tools](https://developers.google.com/web/tools/chrome-devtools)
    - Used to help fix problem areas and identify bugs.
- [AWS](https://aws.amazon.com/)
    - Used to store static files and images.
- [Favicon.io](https://favicon.io/)
    - Used to generate the site's favicon.
- [SQlite](https://www.sqlite.org/index.html)
    - Used for debugging.
- [PostgreSQL](https://www.postgresql.org/)
    - Database used through heroku.
- [SmartDraw](https://cloud.smartdraw.com/)
    - To draw out the database schema.
- [Balsamiq](https://balsamiq.com/)
    - To create the wireframes.
- [W3C Markup Validation Service](https://validator.w3.org/) 
    - Used to validate HTML code.
- [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/#validate_by_input)
    - Used to validate CSS code.
- [Pep8](http://pep8online.com/)
    - Used to validate Python code.
- [JSHint](https://jshint.com/)
    - Used to validate JS code.
- [Crispy forms](https://django-crispy-forms.readthedocs.io/en/latest/)
    - Used to help render forms.
- [Profanity Filter](https://github.com/ReconCubed/django-profanity-filter)
    - App used to remove profanity from comments.
- [Tinyjpg](https://tinyjpg.com/)
    - Used to compress images.
- [Screen to Gif](https://www.screentogif.com/)
    - Used to create gifs for my readme.
- [Stripe](https://stripe.com/en-gb)
    - Used to take payments and generate webhooks.
- [Heroku](https://www.heroku.com/)
    - To deploy the project.

    