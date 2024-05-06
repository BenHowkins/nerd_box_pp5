# Nerd Box

Nerd Box is an E-commerce site created using Django Frameworks and Libaries.
On the site, users can:
1. Register as a user of the site by creating an account and logging in.
2. Create a personalised account containing their own details.
3. Browse the products available in the store on the relivant pages.
4. Select what products they wish to purchase by putting them into their shopping bag.
5. Purchase the products fromtheir bag using their credit/ debit card.

On the site, admin can:
1. Add and delete products as required.

This has been developed as my 5th Portfollio Project for my Full Stack Software Development Diploma with Code Institute.

The project can be viewed here: [Nerd Box](https://otaku-blog-3f79f19c74fc.herokuapp.com/)


## Table Of Content
1. [User Experience](#user-experience)
    - [Project Goals](#project-goals)
    - [Colour Scheme](#colour-scheme)
2. [Planning](#planning)
    - [Methodology](#methodology)
    - [Models](#models)
    - [Frameworks](#frameworks)
3. [Features](#features)
    - [General](#general)
    - [Home Page](#home-page)
    - [Products Page](#products-page)
    - [Product Detail Page](#product-detail-page)
    - [Register Page](#register-page)
    - [Login Page](#login-page)
    - [Logout Page](#logout-page)
    - [Profile Page](#profile-page)
    - [Bag Page](#bag-page)
    - [checkout Page](#checkout-page)
    - [Product Management Page](#product-management-page)
    - [Edit Product Page](#edit-product-page)
4. [SEO And Web Marketing](#seo-and-web-marketing)
    - [Search Engine Optimization](#seearch-engine-optimization)
    - [Newsletter](#newsletter)
    - [Facebook](#facebook)
5. [Technololgies Used](#technologies-used)
    - [Languages](#languages)
    - [Frameworks, Libraries and Programmes](#frameworks-libraries-and-programmes)
6. [Testing](#testing)
    - [Testing User Stories](#testing-user-stories)
    - [Code Validation](#code-validation)
    - [Device Testing](#device-testing)
    - [Browser Testing](#browser-testing)
    - [Feature Testing](#feature-testing)
    - [Bugs](#bugs)
7. [Deployment](#deployment)
8. [Credit](#credit)
    - [Content](#content)
    - [Code](#code)
9. [Acknowledgements](#acknowledgements)


## User Experience
### Project Goals
- Create a Ecommerce store site centered on monthly mystery, subscription boxes around the themes of Video Games, Movies and Anime.
- It will be created using the Django libaries and external database, storage and hosting sites.
- Ensure that all web pages are clean, fully responsive and provide feeback to the user when possible.
- Implement CRUD Functionality so that users can modify data and interact with the site.
- Implement authentication layers of that pages are robust and have security.

### Users Stories
1. 

### Colour Scheme
The website was designed to have a bright but not too overpowering feel to it. This is because it fits in with the general themes assosiated with the content of the boxes (Video Games, Anime, Movies) but also keeps a level of readablity and isn't too overwhelming

<image src="assets/readme/images/nerd_box_palette.png" width="650px"></image>

## Planning
### Methodology

This project was planned and implemented with agile methodology and principles. This was managed and documented on GitHub Projects.

The GitHub project can be viewed here: [Nerd Box](https://github.com/users/BenHowkins/projects/10)

The EPICS were defined using the GitHub Milestones feature and each User Story was given one of the following milestones:
- Product, Search and Selection: A feature of the project that is used in searching for and selecting products
- Purchasing and Payment: A feature of the project that is used in the purchasing and payment process
- Account Management: A feature of the project that is part of the project's account management functionality
- Site Admin: A function of the project that is part of the site's administrative uses

User Stories contained a list of Acceptance Criteria and Tasks to support the development of the project.
Following MoSCoW Priortisation principles, each User Story was assigned a tag from one of the following:
- Must Have
- Should Have
- Could Have
- Won't Have

### Models
The project uses five created models consisting of two main models: Post and Comment and three submodels: Categories, Opinions and Choices. It also uses the Django allauth User model.
1. The Post model stores the blog post data:
- author is a foreign key connecting to the User model.
- category is a foreign key connecting to the Categories model.
- opinion is a foreign key connecting to the Opinions model.
2. The Comment model stores the data regarding comments made on the blog posts:
- post is a foreign key connecting to the Post model.
- choice is a foreign key connecting to the Choices model.

The  entity relationship diagram below was created using [dbdigram](https://dbdiagram.io/home) and demonstrates the relationship between the models. <br>
<image src="assets/readme/fst_project_diagram.png" width="650px"></image>

### Frameworks
The basic layout of each page was planned using the framework tool [Balsamiq](https://balsamiq.cloud/sn6w1jb/projects). This allowed for there to be a basic idea and plan sor each page. There may be slight changes between the framework and the final page.

A full copy of the design can be found in this [PDF File](assets/readme/framework/nerd_box_framework.pdf)

### Home Page
<br>
<image src="assets/readme/framework/home_page.png" width="650px"></image>

### Products Pages
<br>
<image src="assets/readme/framework/products_page.png" width="650px"></image>

### Product Detail Page
<br>
<image src="assets/readme/framework/product_detail_page.png" width="650px"></image>

### Register Page
<br>
<image src="assets/readme/framework/register_page.png" width="650px"></image>

### Login Page
<br>
<image src="assets/readme/framework/sign_in_page.png" width="650px"></image>

### Logout Page
<br>
<image src="assets/readme/framework/sign_out_page.png" width="650px"></image>

### Profile Page
<br>
<image src="assets/readme/framework/profile_page.png" width="650px"></image>

### Bag Page
<br>
<image src="assets/readme/framework/bag_page.png" width="650px"></image>

### Checkout Page
<br>
<image src="assets/readme/framework/checkout_page.png" width="650px"></image>

### Product Management Page
<br>
<image src="assets/readme/framework/product_management_page.png" width="650px"></image>

### Edit Product Page
<br>
<image src="assets/readme/framework/edit_product_page.png" width="650px"></image> 

## Features

### General
- The website incorporates a responsive design so it can be used across multiple device sizes.
- The website uses a consistent colour scheme across the site of a shade of red for the text, a wheat coloured background for the body of the page and an aqua colour for the header and footer.
- Each page has a responsive navigation bar containing the logo and nav menu. The nav bar turns into a burger menu on mobile devices.
- Each page has a repsonsive footer with a link to the site's Facebook page and Mailchimp signup form to signup to the site newsletter. The link opens in a new browser window.

### Home Page
- The home page has a different background colour to the rest of site. It has a shade of red similar to that of the text to make the first page the customer sees to stand out and be different to the rest of the site.
- Also on the page is a selection of white background text boxes outlining information about the shop.
- At the base of the page above the footer is three text boxes outlining the current themes of the three boxes.<br>
<image src="assets/readme/images/home_page_top.png" width="650px"></image><br>
<image src="assets/readme/images/home_page_bottom.png" width="650px"></image>

### Products Pages
- The product pages display product cards of the available products in the form of a grid.
- Each product card contains a product image, a description, it's price and which category/ theme it is from.
- The grid is made up of a maximium of 4 product cards per row with the number of rows varying on the number of and which categories are selected.
- On mobile devices the product cards a limited to one per row.
- The categories the products pages ccan be filtered into include:
    - Current Anime Boxes Available
    - Current Combo Box Available
    - Current Gaming Boxes Available
    - Current Movie Boxes Available
    - All Current Boxes Available
    - Past Anime Boxes Available
    - Past Gaming Boxes Available
    - Past Movie Boxes Available
    - All Past Boxes Available
- If the user is a Superuser then under each product card will be two buttons, one button labelled 'Edit' which takes the user to the Edit Product Page and allows them to edit the product and one button labelled 'Remove' which will remove the item from the store.
<br>
<image src="assets/readme/images/product_page_top.png" width="650px"></image>
<image src="assets/readme/images/product_page_second_section.png" width="650px"></image>
<image src="assets/readme/images/product_page_third_section.png" width="650px"></image>
<image src="assets/readme/images/product_page_forth_section.png" width="650px"></image>
<image src="assets/readme/images/product_page_fifth_section.png" width="650px"></image>
<image src="assets/readme/images/product_page_bottom.png" width="650px"></image>

### Product Detail Page
- The product detail page give the customer a description of the product and ability to add the product to their bag.
- The page contails:
    - The product image on the left side of the page
    - The product's name on the right side of the image
    - The product's price is below that
    - The product's category is below that
    - A decription of the product is below that
    - The quantity of the product selected for purchase is below that
    - Two buttons, one labelled 'Keep Shoping' which when push takes you back to the products page, the other labbeled 'Add To Bag' which adds the quantity of this product selected to the bag are next toeach other at the bottom of this column.
- On a mobile device the each element is on a row of it's own with the exception of the buttons which are still side to side.<br>
<image src="assets/readme/images/product_detail_page_top.png" width="650px"></image><br>
<image src="assets/readme/images/product_detail_page_bottom.png" width="650px"></image>

### Register Page
- This page displays a form which allows the user to register for an account on Nerd Box.<br>
<image src="assets/readme/images/register_page_top.png" width="650px"></image>
<image src="assets/readme/images/register_page_bottom.png" width="650px"></image>

### Login Page
- This page displays a form which allows the user to log into their Nerd Box account.<br>
<image src="assets/readme/images/sign_in_page_top.png" width="650px"></image>
<image src="assets/readme/images/sign_in_page_bottom.png" width="650px"></image>

### Logout Page
- This page displays a form which allows the user to log out of their Nerd Box account.<br>
<image src="assets/readme/images/sign_out_page.png" width="650px"></image>

### Profile Page
- This page displays two columns of information.
- The left hand side being the input boxes for the user's default delivery information.
- This information includes:
  - The user's phone number (which is required)
  - The first line of the user's address (which is required)
  - The second line of the user's address (if available)
  - The user's town or city (which is required)
  - The user's county, state or locality (if available)
  - The user's post/ zip code (which is required)
  - The user's country they live in (which is required)
- There is also a button below the input boxes to save the input information and update their delivery information
- The right hand side show the information of any past orders the user has made.
- This information includes: 
  - The order number
  - The date and time the order was made
  - The contense of the order
  - The grand total of the order
- On a mobile device displaces the two column in a single column with the delivery information first then the order history after it.
<br>
<image src="assets/readme/images/profile_page_top.png" width="650px"></image>
<image src="assets/readme/images/profile_page_bottom.png" width="650px"></image>

### Bag Page
- This page displays the current contense of the shopping bag.
- If there is nothing currently in the bag a message will be displayed stating 'Your bag is empty'. There is also a button labelled 'Keep Shopping' which takes the user back to the products page when pushed.
- If there is products in the bag then each product and relivant information will be displayed on it's own row.
- This information include:
  - The product image
  - The product name, size (if applicable) and sku number in a single colum in that order.
  - The price of the item
  - The quantity in an input box with two buttons, an 'Update' button which will update the quantity in the bag to whatever is in the quantity input box and a 'Remove' button which removes that item from the bag.
  - The subtotal of this product
- Below the last product is three lines of information, outlining the bag total, delivery charge (if applicable) and the grand total of the two added together.
- At the bottom of the page is two buttons. One labelled 'Keep Shopping' which takes the user back to the products page and one labelled 'Secure Checkout' which will take the user to the checkout page.
- On a mobile device the buttons and grand total information will be moved to the top of the page and each piece of information regard the item will be on it's own line in the same order.
<br>
<image src="assets/readme/images/bag_page_top.png" width="650px"></image>
<image src="assets/readme/images/bag_page_bottom.png" width="650px"></image>

### Checkout Page
- This page displays the information needed to check out safely and is split into two columns.
- The left hand side is input boxes for the user's delivery information.
- This information includes:
  - The customer's full name (which is required)
  - The customer's email address (which is required)
  - The customer's phone number (which is required)
  - The first line of the customer's address (which is required)
  - The second line of the customer's address (if available)
  - The customer's town or city (which is required)
  - The customer's county, state or locality (if available)
  - The customer's post/ zip code (which is required)
  - The customer's country they live in (which is required)
- If the customer has updated any of these in their profile page it will be auto inputted into the corrosponding input box and the email wil be auto filled with the email address they signed up with.
- Below these input boxes is another input box for the customer to input their card details.
- These details include:
  - The card number
  - The card's expiration date
  - THe card's CVC number
- Below this is two buttons, one button labelled 'Adjust Bag' which takes them back to the bag and one button labelled 'Complete Order' which will move forward with the payment.
- On the right hand side is order summary which shows a summary of what the customer is ordering.
- This summary shows the key information of each item being purchased on it's own row.
- This information include:
  - The product image
  - The product name, size (if applicable) and quantity in a single colum in that order.
  - The subtotal of the item
- Below the last product is three lines of information, outlining the order total, delivery charge (if applicable) and the grand total of the two added together.
- On a mobile device order summary information will be moved to the top of the page and each piece of information regard delivery and payment will be below it.
<br>
<image src="assets/readme/images/checkout_page_top.png" width="650px"></image>
<image src="assets/readme/images/checkout_page_second_section.png" width="650px"></image>
<image src="assets/readme/images/checkout_page_bottom.png" width="650px"></image>

### Product Management Page
- This page is only available if the account user is a Superuser and displays the ability to add new products to the store.
- The page contains several input boxes for the user's input the information for a new item.
- This information includes:
  - The item's category (which is required)
  - The item's sku number (which is optional)
  - The item's name (which is required)
  - A description of the item (which is required)
  - A selection box to select if the product has sizes or not (which is opional)
  - The item's price (which is required)
  - A button to select an image for the product (which is optional)
- Below this is two buttons, one button labelled 'Cancel' which cancels the new item and takes them back to the products page and one button labelled 'Add Product' which will confirm the new product and add it to the store.
- On a mobile device the page is no different.
<br>
<image src="assets/readme/images/product_management_page_top.png" width="650px"></image>
<image src="assets/readme/images/product_management_page_bottom.png" width="650px"></image>

### Edit Product Page
- This page is only available if the account user is a Superuser and displays the ability to edit products currently available in the store.
- The page will display the input boxes for the product, preloaded with the current information. The user can then change whichever input boxes they need to change.
- Below the input boxes is two buttons, one button labelled 'Cancel' which cancels the edit and takes them back to the products page and one button labelled 'Edit Product' which will confirm the edit and take the user the the corrisponding product detail page.
- On a mobile device the page is no different.
<br>
<image src="assets/readme/images/edit_product_page_top.png" width="650px"></image>
<image src="assets/readme/images/edit_product_page_second_section.png" width="650px"></image>
<image src="assets/readme/images/edit_product_page_bottom.png" width="650px"></image>

## SEO And Web Marketing

### Search Engine Optimalization

SEO techniques were implemented to the best of my ability. In the meta tags in the head I tried to add a detailed decription and I used keyword such as: subscription box, monthly subscriptions, nerd items, anime, video games, movies, figurines, t-shirts, novels, plushies, posters, figures and bulk buy discounts.

Image alternative text is descriptive. Precaution measures are in place in case alt text isn't added, the template will get alt text from the box name which will contain several key words.

The site has been equipped with sitemap generated [here](https://www.xml-sitemaps.com/) and robots.txt.

### Newsletter

I added a Mailchimp signup link in the footer of the page. When the customer signs up with their email, the admin/owner can send regular interesting content containing advanced knowledge of future themes as well as any upcoming special offer or contents. 

### Facebook

Nerd Box [facebook](https://www.facebook.com/profile.php?id=61558124699986) for marketing purposes to post adverts, interesting content and get users engaged. 

<image src="assets/readme/images/facebook_page_top.png" width="650px"></image>
<image src="assets/readme/images/facebook_page_second_section.png" width="650px"></image>
<image src="assets/readme/images/facebook_page_third_section.png" width="650px"></image>
<image src="assets/readme/images/facebook_page_bottom.png" width="650px"></image>

## Technologies Used
### Languages
- HTML
- CSS
- Javascript
- Python
- [Jinja Templating Langugage](https://jinja.palletsprojects.com/en/3.1.x/)

### Frameworks, Libraries and Programmes
- [Font Awesome](https://fontawesome.com/): this was used to add likes and comments icons to the post detail and home pages to enhance user experience
- [Coolers](https://coolors.co/): this was used to create a colour pallete for the website.
- [Balsamiq](https://balsamiq.com/): this was used to create the framework diagrams for the website.
- [Django](https://www.djangoproject.com/): this was the MVC web framework used.
- [Bootstrap 5](https://getbootstrap.com/): this was the CSS framework used to make the site responsive. 
- [Amazon Web Server](https://aws.amazon.com/): this was used to store static and media files.
- [GitPod](https://gitpod.io/): this was used to write, commit and to push the code to Github. 
- [Github](https://github.com/): this was used for version control. 
- [Heroku](https://dashboard.heroku.com/login): this was used to host and deploy the finished project.
- [ElephantSQL](https://www.elephantsql.com/): this is the SQL database used in production.
- [Chrome DevTools](https://developer.chrome.com/docs/devtools/): this was used throughout the project to check responsiveness and debug.
- [W3C Markup Validator](https://validator.w3.org/): this was used throughout the project to validate HTML code. 
- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/): this was used throughout the project to validate CSS code. 
- [CI Python Linter](https://pep8ci.herokuapp.com/): this was used to validate python code. 

A list of packages and dependencies can be found in the requirements.txt file.

## Testing

### User Stories Testing
1. As a Site User I can See A Paginated List Of Reviews so that I Can Find One To Read And Comment On.
  - The home page displays reviews in an ordered, paginated view.
  - The reviews are displayed in descending date order with the newest reviews on the top of the page.
  - There should be no more than 6 reviews on the page before the scroll bar appears to prevent the page from being too crowded.
2. As a Site User I can View A List Of Posts so that I Can Select One To Read.
  - On the main page there should be a visible list of all available posts to read.
  - The posts should be in descending date order with the newest post at the top of the page.
  - The page should only have a maximum of 6 posts showing at once before it allows older posts to be visible through screen navigation.
3. As a Site User I can Click On A Review Post so that I Can Read The Full Review.
  - When The user clicks on a post they are taken to a new page showing the review.
  - The page shows the review as well as the feature image and any comments that may have already been posted.
4. As a Site User/ Admin I can See The Number Of Likes On Each Post so that I Can See What Is Popular.
  - Have an icon (either a heart or thumbs up) below the review post on both the home page and the review's main page.
  - The icon has a numerical counter displaying the number of likes the review has received.
5. As a Site User/ Admin I can View Comments On Individual Posts so that See Others Opinions And Conversations On The Topic.
  - An icon (a speech bubble) is displayed below the post on the post page to say if/ how many comments it currently has.
  - Upon clicking on the post on the home page and being taken to the post's full page, any comments made by registered users should be visible below the post in descending order with the oldest comments at the top.
  - The comments should be in descending order with the oldest comments at the top.
6. As a Site User I can Create/ Register An Account so that I Can Like And Comment On Post.
  - The user must create a unique username with an email address.
  - The user must create and confirm a password.
  - The user is informed by a message they are successfully registered.
7. As a Site User I can Log Into My Account so that I Can Continue Liking And Commenting On Posts When I Return To The Site.
  - The user must input the username/ email address and password used upon creating the account.
  - If the credentials are correct, they're notified they are logged in and taken to the home page.
  - If the credentials are wrong, they inform the information is incorrect and are asked to try again.
8. As a Site User I can Leave A Comment On A Post so that I Can Give My Opinion And Join The Conversation.
  - When on the main page of a post, a registered user can leave a comment on that post.
  - The comment area should only appear if the user is logged in
  - When the comment is made a message will inform the user it's waiting for approval from the site admin.
  - The comment should only appear once the site admin has approved it.
9. As a Site User I can Update My Comments so that I Can Change Or Add To My Comment.
  - Below each comment a registered user has made there will be a button labelled 'Update'.
  - If the user clicks the button, they are able to make alterations to/ update their comment.
  - When the user has changed the comment, they click the submit button to confirm the alterations.
  - When the user pushes the submit button, they are taken to the home page.
10. As a Site User I can Delete My Comments so that I Can Remove My Comment From The Conversation.
  - Below each comment a registered user has made there will be a button labelled 'Delete'.
  - If the user clicks the button, they will be taken to a page asking if they want to delete the message
  - If the user clicks 'Delete Comment', the comment will be deleted and the user will be taken back to the homepage.
11. As a Site User I can Like Or Unlike A Post so that I Can Interact With A Post And Show My Opinion.
  - Have an icon (either a heart or thumbs up) below the review post on the post page.
  - If the user is logged in then the icon should become clickable.
  - If the user clicks on the icon it will change (go from empty to solid or coloured) to indicate they like the post, this also increases the number next to the icon indicating the number of likes.
  - If the user clicks the icon again it will change back to its original state (solid or coloured to an empty icon) to indicate a dislike, this also decreases the number next to the icon.
12. As a Site Admin I can Create, Read, Update and Delete Posts so that I Can Manage My Blog's Content.
  - The admin/ superuser will be able to write posts that appear on the main site.
  - The post panel should only be visible on the admin page of the site when logged in as a superuser.
  - Once a post is created, the superuser can edit and/or delete the post by clicking the corresponding button.
13. As a Site Admin I can Create Draft Posts so that I Can Finish The Posts At A Later Date When Required.
  - The admin/ superuser will be able to save posts they are writing by saving the post under the status 'Draft'.
  - The draft posts should be saved on the admin page and not visible on the main site until the status is changed to 'Published'.
  - Once a draft post is published, it should appear on the main page.
14. As a Site Admin I can Approve Or Reject Comments so that I Can Filter Out Inappropriate Comments.
  - When a user makes a comment on a post, it doesn't appear automatically under the post.
  - A message appears when a comment is entered stating 'comment awaiting approval by admin'.
  - On the admin page the comment is visible for the admin to read.
  - If the comment is approved, it appears on the site under the post it was made on.
  - If it isn't approved, it will not appear on the site and will be deleted.

### Code Validation
The following validators were used to test the code:
- [W3C Markup Validator](https://validator.w3.org/): No errors were reported when passing the final HTML code through the validator. 
- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/): No errors were reported when passing the final CSS code through the validator. <br>
- [CI Python Linter](https://pep8ci.herokuapp.com//): No errors were reported when passing the final python code through the validator.  <br>

#### Unresolved HTML Error
- Upon passing through the validator, no error were shown.
#### Unresolved Python Error
- When passing the py files through the validator, it stated that the env.py and settings.py had a total of 7 lines deemed 'too long', however these lines were either names of password validators or names of keys, so were all left as they were.

### Device Testing
- The website was manually tested on a:
  - Jumper EZbook S5 Max
  - OPPO A54
  - Amazon Kindle Fire

### Browser Testing
The website was tested on the following browsers with no issues:
- Google Chrome
- Avast Secure Browser
- Mozilla Firefox
- Microsoft Edge

### Feature Testing
The following manual tests were carried out:
#### General: base.html
TEST       | DESIRED RESULT          | PASS/FAIL |
---------- | ----------------------- | --------- |
Logo | When the logo is clicked, the user is brought back to the home page | PASS
Mobile menu | On mobile devices, a burger menu is used to display nav links | PASS
Register nav link | Brings the user to the signup page | PASS
Login nav link | Brings the user to the login page | PASS
Logout nav link | Brings the user to the logout page | PASS
Footer links | When clicked, footer links open in a new browser window | PASS

#### Home Page: index.html
TEST       | DESIRED RESULT          | PASS/FAIL |
---------- | ----------------------- | --------- |
Post Card | A card for each post is visible containing: Feature image, Author's Name, Post's Title, Post Excerpt, Published Date, Number Of LIkes | PASS
Post Card Link | When the title of the card is clicked, the user is brought to the post detail page for the post | PASS
Number Of Likes | The number of likes on the card should be the same as that on the post detail page | PASS
Page Pagination | The post cards should be in rows of 3 posts per row and should have page navigation appear when more than 6 posts are visable | PASS

#### Add Post Page: add_post.html
TEST       | DESIRED RESULT          | PASS/FAIL |
---------- | ----------------------- | --------- |
Register Message | The user should be welcomed with a message saying welcome back to the page and told to fill out the form below if they wish to leavee a post of their own | PASS
Input Form | There should be a labeled form for the user to input a Title for the post, a Slug name, select the Author of the post, select an Image, create an Exerpt decription and the post Content itself with the Title, Slug, Author and Content all being starred to indicate they are authorised fields  | PASS
Confirmation Button | A button should be visable below the message labelled "Submit" which confirms submission of the review | PASS
Data Input Autherisation | After the submit button is pushed the site will check all the required fields have data entered in them and also check the data input against the database to see there is no repeated Titles or Slugs being used. If either of these things happen a error message will appear under the offending field saying either that this field is required or this Title or Slug has been used and to select another one  | PASS
Site Redirection | After pushing the submit button with correct details, the user should be redirected back to the home page | PASS

#### Post Detail Page: post_detail.html
TEST       | DESIRED RESULT          | PASS/FAIL |
---------- | ----------------------- | --------- |
Post Details | The top of the page should display: Author's Name, Post Title, Excerpt and Date Published on the left side of the screen and the Featured Image on the right | PASS
Post Body | The post itself should be displayed directly below the details card | PASS
Likes And Comments Counter | Icons and counters displaying the current number of likes and comment the post has should be visible below the post | PASS
Like And Unlike |  When a user has an account and is logged in they are able to click on the like icon and like the post or click it again and unlike the post | PASS
Leave A Comment Section | If the user has an account and is logged in then there will be a box visable for them to leave a comment. If they aren't logged in the box won't appear | PASS
Comment Authorisation | All comments when left shouldn't display automatically but should show a message stating they are "Await Approval". Once approval is given they should then appear on the page | PASS
Comment List | All approved comment should appear down the left side of the screen in order of creation with the oldest comment at the top and getting newer as you go down, to easily follow the conversation | PASS
Comment Edit Button | A button should appear below any comment a logged in user has made named "Edit". This should take them to the comment edit page. This button should only appear on comments they have made | PASS
Delete Comment Button | A button should appear below any comment a logged in user has made "Delete". This should take them to the comment delete page. This button should only appear on comments they have made | PASS

#### Comment Edit Page: comment_edit.html
TEST       | DESIRED RESULT          | PASS/FAIL |
---------- | ----------------------- | --------- |
Edit Comment Message | The user should be welcomed with a personalised message containing their username stating that they can change their comment | PASS
Comment Edit Box | A textbox should be visable, displaying the original message and allowing the user to make alterations | PASS
Confirmation Button | A button should be visable below the textbox labelled "Update Comment" which confirms any changes made | PASS
Site Redirection | After pushing the button the user should be redirected back to the home page | PASS

#### Comment Delete Page: comment_delete.html
TEST       | DESIRED RESULT          | PASS/FAIL |
---------- | ----------------------- | --------- |
Edit Comment Message | The user should be welcomed with a personalised message containing their username stating that they are deleting their comment and this is unreversable | PASS
Confirmation Button | A button should be visable below the message labelled "Delete Comment" which confirms deletion of the comment | PASS
Site Redirection | After pushing the button the user should be redirected back to the home page | PASS

#### Register Page: signup.html
TEST       | DESIRED RESULT          | PASS/FAIL |
---------- | ----------------------- | --------- |
Register Message | The user should be welcomed with a message saying welcome back to the page and told if they already have an account to log in with a link to the log in page or sign up below if they don't have an account | PASS
Input Details | There should be labeled boxes for the user to input a username, an email address if they wish too and to input a password and another password field to confirm the password match. There is also a submit button to confirm entry of the details | PASS
Input Autherisation | After the submit button is pushed the site will check the data input against the database. If the passwords match and the username is unique the user will be redirected to the home page. If the username is taken the user will be informed it has been taken and asked to pick another one. If the passwords don't match the user will be told they didn't match and asked to try again | PASS
Site Redirection | After pushing the submit button with correct details, the user should be redirected back to the home page and a message should display stating they have signed in with their username | PASS

#### Login Page: login.html
TEST       | DESIRED RESULT          | PASS/FAIL |
---------- | ----------------------- | --------- |
Login Message | The user should be welcomed with a message saying welcome back and log in or sign up with a link to the register page if they don't have an account | PASS
Input Details | There should be labeled boxes for the user's username and password and a submit button to confirm entry of the details | PASS
Input Autherisation | After the submit button is pushed the site will check the data input against the database. If the data is correct the user is redirected back to the home page, if it is incorrect a message will appear stating that either the username and/ or password are incorrect and allow the user to try again | PASS
Site Redirection | After pushing the submit button with correct details, the user should be redirected back to the home page and a message should display stating they have signed in with their username | PASS

#### Logout Page: logout.html
TEST       | DESIRED RESULT          | PASS/FAIL |
---------- | ----------------------- | --------- |
Logout Message | The user should be welcomed with a message stating that they are logging out of their account and see if they are sure | PASS
Confirmation Button | A button should be visable below the message labelled "Log Out" which logs the user out of their account | PASS
Site Redirection | After pushing the button the user should be redirected back to the home page and a message should display stating they have signed out | PASS

### Bugs
#### Resolved Bugs
1. Authorised Comment User Bug- When creating the buttons for the "Edit" and "Delete" comment functionality I was unable to correctly have it so that only the user who created the comment could edit or delete it. I realised that I had: 
  1. I only used a single "=" sign in the equalty check.
  2. I had not used the correct wording in the if statement. I had put "user.name == comment.name" instead of "user.username == comment.name"
once I corrected both these issue both buttons appeared correctly.
2. Edit Comments Bug- Whilst trying to create this functionality I was unable to get it to correctly function without giving me a "No Reverese" or a "Page Not Found" error. After speaking to several Code Institute Tutor I found that I was trying to override the Post and Get methods and instead I should be updating the view. And after reading through and article on [GeeksForGeeks](https://www.geeksforgeeks.org/) I was able to write the correct code.

#### Unresolved Bugs
- Through testing and validations I don't believe that there is any unresolved bugs on the site.

## Deployment
The program was developed in Codeanywhere. It was then commited and pushed to GitHub periodically.
The finished project was then deployed to Heroku. 
Deployment to Heroku was completed using the following steps: 
1. Open and login to [Heroku](https://id.heroku.com/login).
2. From the dashboard, click 'New', then click 'Create new app' from the dropdown menu. 
3. Enter the App name, choose a region, then click 'Create app'.
4. Navigate to the 'Settings' tab.
5. Within 'Settings', navigate to 'Convig Vars'. Click 'Reveal Config Vars'.
6. Add config vars using the 'KEY' and 'VALUE' pairs from env.py.
7. Navigate to the 'Deploy' tab. 
8. Within 'Deploy', navigate to 'Deployment method'. 
9. Click on 'GitHub'. Navigate to 'Connect to GitHub' and click 'Connect to GitHub' 
10. Within 'Connect to GitHub', use the search function to find the repository to be deployed. Click 'Connect'.
11. Navigate to either 'Automatic Deploys' or 'Manual Deploys' to choose which method to deploy the application.
12. Click on 'Enable Automatic Deploys' or 'Deploy Branch' respectively, depending on chosen method. 
13. Once the app is finished building, a message saying 'Your app was successfully deployed' will appear.
14. Click 'View' to see the deployed app. 

## Credit
### Content
- All other content was written by the developer.

### Code
- [Code Institute](https://codeinstitute.net/):
  - Code Insitute full stack walkthrough projects were referred to when setting up the project. Elements of these projects were used and adapted to suit this project.
- [Bootstrap5](https://getbootstrap.com/): was used to add elements including cards for the posts and the navigation bar. 
- [Django](https://www.djangoproject.com/): documentation was referred to throughout development. 

## Acknowledgements
- Thank you to Oisin, Holly, Roo and Joanne from Code Institute Tutor Support for helping me along the way. 
- Thank you to Code Institute for providing me with the tools and skills to complete this project.