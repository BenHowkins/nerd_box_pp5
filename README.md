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
    - [User Stories](#user-stories)
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
    - [Email Confirmation Page](#email-confirmation-page)
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
    - [Automated Testing](#automated-testing)
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
#### User Stories that have been satisfied in ths project through particular apps or their creation:
| ID | User Story | How/ Where It Was Satisfied |
| ---------- | ----------------------- | --------- |
| [1](https://github.com/BenHowkins/nerd_box_pp5/issues/1) | As a User I can Create An Account On The Site so that I Can Have A Personal Account To View And Use On The Site | Registration Page and Profile App |
| [2](https://github.com/BenHowkins/nerd_box_pp5/issues/2) | As a User I can Log Into My Account so that Upon Returning To The Site I Can Continue From Where I Left Off With The Same Details | Login Page and Profile App |
| [2](https://github.com/BenHowkins/nerd_box_pp5/issues/2) | As a User I can Log Into My Account so that Upon Returning To The Site I Can Continue From Where I Left Off With The Same Details | Login Page and Profile App |
| [4](https://github.com/BenHowkins/nerd_box_pp5/issues/4) | As a User I can Have A Personalised Profile so that I Can Have An Individual Profile Containing My Past And Current Orders As Well As Saving My Card Details | Profile App |
| [5](https://github.com/BenHowkins/nerd_box_pp5/issues/5) | As a Shopper I can See A List Of Available Items so that I Can See What Items I Can Purchase | Boxes App and Products Page |
| [6](https://github.com/BenHowkins/nerd_box_pp5/issues/6) | As a Shopper I can Read A Description Of The Products so that I Know What I Am Buying And If It Is Right For Me | Boxes App and Product Details Page |
| [7](https://github.com/BenHowkins/nerd_box_pp5/issues/7) | As a Site User I can Log Out Of My Account so that Others Can Not Use It When I Am Not | Log Out Page |
| [8](https://github.com/BenHowkins/nerd_box_pp5/issues/8) | As a Shopper I can See Different Variations Of Each Product so that I Can Purchase The Correct One I Want | Boxes App and Product Details Page |
| [9](https://github.com/BenHowkins/nerd_box_pp5/issues/9) | As a User I can Sort Products By Categories so that I can find the product that I am looking for | Boxes App and Product Page |
| [10](https://github.com/BenHowkins/nerd_box_pp5/issues/10) | As a User I can Have A Way To Search And Find Products By Keywords so that I Can See Products That I Am Interested In | Search Bar In The Header and Product Page |
| [11](https://github.com/BenHowkins/nerd_box_pp5/issues/11) | As a User I can See A Detailed Description Of The Product so that I Can See If It Is Right For Me | Boxes App and Product Details Page |
| [12](https://github.com/BenHowkins/nerd_box_pp5/issues/12) | As a User I can See An Organised Grid Showing The Available Products so that I Can See What Is Available To Purchase | Boxes App and Products Page |
| [13](https://github.com/BenHowkins/nerd_box_pp5/issues/13) | As a User I can Select The Size Of A Product When Available so that I Can Get The Right Size Product For Me | Boxes App and Product Details Page |
| [14](https://github.com/BenHowkins/nerd_box_pp5/issues/14) | As a User I can Add Desired Products To My Bag so that I Can Purchase Them At Some Point | Boxes App and Product Details Page |
| [15](https://github.com/BenHowkins/nerd_box_pp5/issues/15) | As a User I can Select Different Quantities Of Products To Purchase so that I Get The Amount Of Each Product I Want | Boxes App, Product Details Page, Bag App and Bag Page |
| [16](https://github.com/BenHowkins/nerd_box_pp5/issues/16) | As a User I can Edit And Remove Products From My Bag so that I Only Purchase The Products And Amounts I Want | Bag App and Bag Page |
| [17](https://github.com/BenHowkins/nerd_box_pp5/issues/17) | As a User I can Input And Save My Data so that I Can Quickly Use It Again At Another Time When I May Need It | Profile App, Profile Page, Checkout App and Checkout Page |
| [18](https://github.com/BenHowkins/nerd_box_pp5/issues/18) | As a User I can Use My Card And Personal Details To Pay For Products so that I Can Purchase The Goods I Want | Checkout App and Checkout Page |
| [19](https://github.com/BenHowkins/nerd_box_pp5/issues/19) | As a User I can Recieve Confirmation AFfter I Have Completed My Order so that I Know Payment Was Successful | Checkout App and Checkout Page |
| [20](https://github.com/BenHowkins/nerd_box_pp5/issues/20) | As a User I can Have My Order Successfully Check Out Even When The Connection Is Lost Mid Payment so that I Am Not Charge Without Purchase Of Goods | Checkout App and Checkout Page |
| [21](https://github.com/BenHowkins/nerd_box_pp5/issues/21) | As a User I can Receive Messages Appear On The Screen Whenever Something Happens so that I Am Always Aware Of What Is Going On | Home App and Header Bar |
| [23](https://github.com/BenHowkins/nerd_box_pp5/issues/23) | As a User I can Click On A Link To The Store's Facebook Page so that I Can See What they Are Doing On And Keep Up To Date On Their Social Media | Home App and Footer Bar |
| [24](https://github.com/BenHowkins/nerd_box_pp5/issues/24) | As an Admin I can Add Products To The Store so that There Are Always New And Different Products Available | Boxes App and Products Mantainance Page |
| [25](https://github.com/BenHowkins/nerd_box_pp5/issues/25) | As an Admin I can Edit Existing Products so that I Can Update Products When Needed | Boxes App and Edit Products Page |
| [26](https://github.com/BenHowkins/nerd_box_pp5/issues/26) | As an Admin I can Remove Products From The Store so that I Can Take Products That Are Unavailable For Purchase Off The Store | Boxes App and Products Page |

#### User stories that are planned for future updates:

| ID | Content | 
| ------ | ------ |
| [27](https://github.com/BenHowkins/nerd_box_pp5/issues/27) | As an Admin I can Check Stock Levels so that I Know How Many Of Each Product Are In Stock |
| [28](https://github.com/BenHowkins/nerd_box_pp5/issues/28) | As a User I can Show Interest On Out Of Stock Products so that I Can Find Out When More Become Available |
| [29](https://github.com/BenHowkins/nerd_box_pp5/issues/29) | As an Admin I can Set Up Certain Products Behind An Age Barrier so that I Can Offer More Products To Older Users |
| [30](https://github.com/BenHowkins/nerd_box_pp5/issues/30) | As a User I can A Discount Off Product Purchased On My Birthday so that I Can Have A Gift On My Special Day |
| [31](https://github.com/BenHowkins/nerd_box_pp5/issues/31) | As an Admin I can Limit How Old Users Making Purchases Are so that Children Don't Make Purchases With Their Parents Card |
| [32](https://github.com/BenHowkins/nerd_box_pp5/issues/32) | As an Admin I can Implement Human Verification so that Only Real People And Not Bots Create Accounts |

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
<image src="assets/readme/framework/log_in_page.png" width="650px"></image>

### Logout Page
<br>
<image src="assets/readme/framework/log_out_page.png" width="650px"></image>

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

### Automated tests
Automated tests have not been created due to time constrains of the project.

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
| TEST       | DESIRED RESULT          | PASS/FAIL |
| ---------- | ----------------------- | --------- |
| Logo | When the logo is clicked, the user is brought back to the home page | PASS |
| Mobile Menu | On mobile devices, a burger menu is used to display three nav links: a link back to the home page and two dropdown menus to display the categories of the current and past boxes. There is also icons for the search bar, my account and bag links next to the burger menu | PASS |
| Search Bar | Inputting information into the search bar brings up a page with relivant search results | PASS |
| My Account Link | Brings up a mini drop menu with a number of links depending on if the user is signed in or out or is a superuser | PASS |
| Register Nav Link | Brings the user to the signup page | PASS |
| Login Nav Link | Brings the user to the login page | PASS |
| Logout Nav Link | Brings the user to the logout page | PASS |
| My Profile Link | Brings the user to their profile page | PASS |
| Product Management Nav Link | If the user is a SuperUser it brings user to the product management page | PASS |
| Bag Link | Brings the user to the bag page | PASS |
| All Current Boxes Dropdown Link | Brings up a dropdown menu containing links to each categories of the current box plus a link that displays all available current boxes | PASS |
| Anime Box Link | Brings the user to a page displaying all available boxes in the Anime Box category | PASS |
| Combo Box Link | Brings the user to a page displaying all available boxes in the Combo Box category | PASS |
| Gaming Box Link | Brings the user to a page displaying all available boxes in the Gaming Box category | PASS |
| Movie Box Link | Brings the user to a page displaying all available boxes in the Movie Box category | PASS |
| All Current Boxes Link | Brings the user to a page displaying all available current boxes | PASS |
| Past Boxes Dropdown Link | Brings up a dropdown menu containing links to each categories of the past box plus a link that displays all available past boxes | PASS |
| Past Anime Box Link | Brings the user to a page displaying all available boxes in the Past Anime Box category | PASS |
| Past Gaming Box Link | Brings the user to a page displaying all available boxes in the Past Gaming Box category | PASS |
| Past Movie Box Link | Brings the user to a page displaying all available boxes in the Past Movie Box category | PASS |
| All Past Boxes Link | Brings the user to a page displaying all available past boxes | PASS |
| Footer Link | When clicked, the facebook link in the footer opens to the facebook page in a new browser window | PASS |
| Mailchimp Link | When an email address is input and submitted in the link a message confirming the subscription to the news letter | PASS |

#### Home Page: index.html
| TEST       | DESIRED RESULT          | PASS/FAIL |
| ---------- | ----------------------- | --------- |
| Information Cards | A number of card each containing information about the store with key information such as categories and the store name highlighted in bold to emphasize them | PASS |
| Themes Title Box | A single page length white box containing text to state that the below text is the current available themes for each category | PASS |
| Themes Boxes | Three boxes should be at the base of the page above the footer stating the current themes of each box with a small 1-2 line hook for the boxes | PASS |

#### Products Page: products.html
| TEST       | DESIRED RESULT          | PASS/FAIL |
| ---------- | ----------------------- | --------- |
| Page Title | The user should see a title at the top of the page below the header stating that this is the Products page | PASS
| Category Boxes | There should be below the title boxes with the names of the caegories the user selected to see | PASS
| Individual Category Box Selection | If more than one was selected then clicking a box will change the product page to show just that category | PASS
| Item Cards | A card for each box is visible containing: feature image, name, price and category | PASS
| Superuser Extra Item Card Options | If the user is a superuser then there should be two extra option on the item card, one is a link to the edit product page labelled Edit and the other deletes the item labelled Delete | PASS
| Edit Link | Clicking the link will take the superuser to the edit poduct page | PASS
| Delete Link | Clicking the link will delete the product from the store | PASS
| Display Grid | The available item cards for the category/ categories selected should be displayed in the rows containing no more than four cards per row | PASS
| Site Direction | Upon clicking on the feature image of an item, the user should be directed to the product details page for that product | PASS
| Page Up | At the base of the page below the last row of item cards but above the footer is an arrow which when pushed returns the user to the top of the page | PASS |


#### Product Detail Page: product_detail.html
| TEST       | DESIRED RESULT          | PASS/FAIL |
| ---------- | ----------------------- | --------- |
| Product Image | On the left side of the screen there is an image of the current product that the user is looking at or a placeholder image of a box | PASS |
| Image Link | Clicking on the product image will open a new window with the image full size | PASS |
| Product Information | On the right of the image should be the current product's: name, price, category and a decription of the product | PASS |
| Superuser Extra Options | If the user is a superuser then uder the category should be two link, one is a link to the edit product page labelled Edit and the other deletes the item labelled Delete | PASS |
| Edit Link | Clicking the link will take the superuser to the edit poduct page | PASS |
| Delete Link | Clicking the link will delete the product from the store | PASS |
| Size Sector | If the product has the option of sizes then there should be a selector which allowing the user to select their desired size from: XS, S, M, L and XL | PASS |
| Quantity Selector | There should be a selector which allowing the user to select their desired quantity | PASS |
| Quantity Selector Input | The quantity can be changed/ input either by using the arrows at the right side of the input box or by manually inputting it into the box. The selector will also not allow the number to go above 99 and below 1 or anything other than a number | PASS |
| Add To Bag Button | At the base of the page is an 'Add To Bag' button which when clicked will add the current product and quantity selected to the bag. A message will appear at the top of the page stating the product has been added to the bag | PASS |
| Keep Shopping Button | At the base of the page next to the 'Add To Bag' button is a 'Keep Shopping' button which when clicked takes the user back to the Products page | PASS |

#### Register Page: signup.html
| TEST       | DESIRED RESULT          | PASS/FAIL |
| ---------- | ----------------------- | --------- |
| Register Message | The user should be welcomed with a message saying welcome back to the page and told if they already have an account to log in with a link to the log in page or sign up below if they don't have an account | PASS | |
| Input Details | There should be labeled boxes for the user to input an email address and another to confirm it, a box for a username and a password and another password field to confirm the password match. There is also a 'Submit' button to confirm entry of the details | PASS |
| Input Autherisation | After the 'Submit' button is pushed the site will check the data input against the database. If the passwords match and the username is unique the user will be redirected to another screen stating that an email has been sent to the provided address and they must click the link to confirm their account. If the username or email address is taken the user will be informed it has been taken and asked to pick another one. If the email addresses and/ or passwords don't match the user will be told they didn't match and asked to try again | PASS |
| Site Redirection | After pushing the 'Submit' button with correct details, the user should be redirected bto another screen stating that an email has been sent to the provided address and they must click the link to confirm their account | PASS |

#### Account Confirm Page: email_confirm.html
| TEST       | DESIRED RESULT          | PASS/FAIL |
| ---------- | ----------------------- | --------- |
| Conformation Message | The user should be welcomed with a message asking them to confirm that the email address provided is for the username provided | PASS |
| Conformation Button | The user should have a button labelled 'Confirm' which when clicked will confirm the details, create the account and redirect the user to the login page | PASS |
| Site Redirection | After pushing the button the user should be redirected back to the login page | PASS |

#### Login Page: login.html
| TEST       | DESIRED RESULT          | PASS/FAIL |
| ---------- | ----------------------- | --------- |
| Login Message | The user should be welcomed with a message saying if they don't have an account they need to sign up first with a link to the register page | PASS |
| Input Details | There should be labeled boxes for the user's username or email and password and a 'Submit' button to confirm entry of the details | PASS |
| Input Autherisation | After the 'Submit' button is pushed the site will check the data input against the database. If the data is correct the user is redirected back to the home page, if it is incorrect a message will appear stating that either the username and/ or password are incorrect and allow the user to try again | PASS |
| Site Redirection | After pushing the 'Submit' button with correct details, the user should be redirected back to the home page and a message should display stating they have signed in with their username | PASS |
| Home Button | Next to the 'Submit' button there is a 'Home' button which when clicked will return the user to the home page | PASS |

#### Logout Page: logout.html
| TEST       | DESIRED RESULT          | PASS/FAIL |
| ---------- | ----------------------- | --------- |
| Logout Message | The user should be welcomed with a message stating that they are logging out of their account and see if they are sure | PASS |
| Confirmation Button | A button should be visable below the message labelled 'Sign Out' which logs the user out of their account | PASS |
| Site Redirection | After pushing the button the user should be redirected back to the home page and a message should display stating they have signed out | PASS |
| Cancel Button | Next to the 'Sign Out' button there is a 'Cancel' button which when clicked will keep them signed in and return them to the home page | PASS |

#### Profile Page: profile.html
| TEST       | DESIRED RESULT          | PASS/FAIL |
| ---------- | ----------------------- | --------- |
| Page Title | At the top of the page is a title stating this is My Profile page | PASS |
| Delivery Information Title | At the top of the left hand side of the page below the title is a subheading stating that the below information is the Default Delivery Information | PASS |
| Delivery Information Input | Below the title there is seven input boxes labeled: Phone Number, Street Address 1, Street Address 2, Town or City, County State or Locality, Postal Code and Country | PASS |
| Update Information Button | Below the input boxes is an 'Update Information' button which when clicked will save the current information to the profile with a message stating that the information has been saved | PASS |
| Order History Title | At the top of the right hand side of the page below the title is a subheading stating that the below information is the Order History Information | PASS |
| Order History Headers | Below the Order History subtitle are four column with the headers: Order Number, Date, Items and Order Total | PASS |
| Order History | If there hasn't been any orders then this section will be blank, but if orders have been made then below each column header will be the relivant information for each of the orders | PASS |

#### Bag Page: bag.html
| TEST       | DESIRED RESULT          | PASS/FAIL |
| ---------- | ----------------------- | --------- |
| Page Title | At the top of the page is a title stating this is 'Shopping Bag' page | PASS |
| Empty Bag Message | If there is currently no items in the user's bag then there will be a message stating 'Your bag is empty' | PASS |
| Product Headers | Below the 'Shopping Bag' Title are four column with the headers: Product Info, Price, Quantity and Subtotal | PASS |
| Product Info | Under the 'Product Info' header should be the product image with the procucts: name, size selected (if applicable) and SKU number in a column next to the image | PASS |
| Price | Under the 'Price' header should be the price for the product per unit incase multiples are selected | PASS |
| Quantity | Under the 'Quantity' header should be an input box with the current selected quantity input | PASS |
| Quantity Input | The quantity can be changed/ input either by using the arrows at the right side of the input box or by manually inputting it into the box. The selector will also not allow the number to go above 99 and below 1 or anything other than a number | PASS |
| Update Button | On the left hand side below the quantity input box is a link/ button named 'Update' whch when clicked will update the quantity of the current item to what is currently in the quantity box | PASS |
| Remove Button | On the right hand side below the quantity input box is a link/ button named 'Remove' whch when clicked will remove this item from from shopping bag | PASS |
| Subtotal | Under the 'Subtotal' header should be the total price of the product by multiply price and quantity together | PASS |
| Items | If there is currently more than one different items in the users bag then they should be displayed with each item in it's own row | PASS |
| Bag Total | Below the last item on the right of the screen is a header labelled 'Bag Total:' with the current total of all the items in the shopping bag | PASS |
| Delivery | Below the 'Bag Total:' header is another header labelled 'Delivery:' with the current current charge for delivery | PASS |
| Grand Total | Below the 'Delivery:' header is another header labelled 'Grand Total:' with the current total of all the items in the shopping bag and delivery charge | PASS |
| Free Delivery Message | If a delivery charge is being applied a message will be seen under the grand total stating 'You could get free delivery by spending just $xx.xx more!' letting the user know how far they are from the free delivery threshold | PASS |
| Secure Checkout Button |At the base of the page is a 'Secure Checkout' button which when clicked will confirm the content of the bag and redirect the user to the 'Checkout' page to finish their purchase | PASS |
| Keep Shopping Button | At the base of the page next to the 'Secure Checkout' button is a 'Keep Shopping' button which when clicked takes the user back to the Products page | PASS |

#### Checkout Page: checkout.html

#### Product Management Page: add_product.html
| TEST       | DESIRED RESULT          | PASS/FAIL |
| ---------- | ----------------------- | --------- |
| Page Title | At the top of the page is a title stating this is 'Product Management' page | PASS |
| Page Subheader | Below the 'Product Management' title is a subheader stating 'Add a Product' which lets the superuser know that this page allows them to add a product | PASS |
| Product Information Input | Below the subheader there is six input boxes labeled: Category, SKU, Name, Description, Has Sizes and | Price and a 'Select Image' button below them | PASS |
| Category Selector Input | The Category selector has a dropdown menu of all the available categories allowing the superuser to select the desired category | PASS |
| Has Sizes Selector Input | The Has Sizes selector has a dropdown menu allowing the superuser to select if the item has sizes or not | PASS |
| Price Input | The Price should be an input box which allows the superuser to input the desired price. The price can be changed/ input either by using the arrows at the right side of the input box or by manually inputting it into the box. The selector will also not allow the number to go below 1 or anything other than a number | PASS |
| Select Image Button | The 'Select Image' button will open up the superuser's image folder to allow them to select the image for the product | PASS |
| Add Product Button | At the base of the page is a 'Add Product' button which when clicked will confirm the information added, add product to the store and redirect the superuser to the 'Product Detail' page for the added product | PASS |
| Required Fields | When clicking the 'Add Product' button and either the Name, Description or Price field is empty a message will appear stating 'Please fill in this field' | PASS |
| Cancel Button | At the base of the page next to the 'Add Product' button is a 'Cancel' button which when clicked takes the superuser back to the Products page | PASS |
 
#### Edit Product Page: edit_product.html
| TEST       | DESIRED RESULT          | PASS/FAIL |
| ---------- | ----------------------- | --------- |
| Page Title | At the top of the page is a title stating this is 'Product Management' page | PASS |
| Page Subheader | Below the 'Product Management' title is a subheader stating 'Edit a Product' which lets the superuser know that this page allows them to edit a product | PASS |
| Product Information Input | Below the subheader there is six input boxes labeled: Category, SKU, Name, Description, Has Sizes and Price each being prefilled with the current information for the product. There is also the current image for the product with a checkbox labelled 'Remove' as well as the 'Select Image' button below them. | PASS |
| Category Selector Input | The Category selector has a dropdown menu of all the available categories allowing the superuser to select the desired category | PASS |
| Has Sizes Selector Input | The Has Sizes selector has a dropdown menu allowing the superuser to select if the item has sizes or not | PASS |
| Price Input | The Price should be an input box which allows the superuser to input the desired price. The price can be changed/ input either by using the arrows at the right side of the input box or by manually inputting it into the box. The selector will also not allow the number to go below 1 or anything other than a number | PASS |
| Select Image Button | The 'Select Image' button will open up the superuser's image folder to allow them to select a new image for the product | PASS |
| Update Product Button | At the base of the page is a 'Update Product' button which when clicked will confirm the information added, edit product's details in the store and redirect the superuser to the 'Product Detail' page for the edited product | PASS |
| Required Fields | When clicking the 'Update Product' button and either the Name, Description or Price field is empty a message will appear stating 'Please fill in this field' | PASS |
| Remove Image Checkbox | If the 'Remove' checkbox is checked when the 'Update Product' button is clicked and a replacement image isn't selected then the placeholder image should be used for the product's image | PASS |
| Cancel Button | At the base of the page next to the 'Edit Product' button is a 'Cancel' button which when clicked takes the superuser back to the Products page | PASS |

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