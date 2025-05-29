# Ecom-Website
A minimalistic E-commerce website example using HTML / Jinja, CSS, JavaScript and Flask. 
Written for Mass Creations as requested by Sam Bishop.
Author: Tyler Brooker
Date: 29/05/2025
Location: UK

The main folder contains app.py, which runs the Flask server in Python, and two folders, static and templates, which is the required structure for Flask apps.
static contains image files loaded and cached by the page in an image subfolder, and all the .css and .js files.
template contains all html files to be rendered by the Flask engine.
The app.py file needs to be run, and the IP address http://127.0.0.1:5000/ is normally used to test the web page.


Info on each relevant file:

# app.py

Runs the server code using the Flask framework. Contains functions for returning and rendering the web pages, and for updating the user's shopping cart.
Loads in structured JSON data to create the products to be rendered.

# index.html

The landing page. Shows all products, and provides the ability to add any of the products to the user's cart without having to go onto the product page. This is done using an attribute in the Add to Cart button that provides the product key of that product as an argument. The user can also see their shopping cart at the bottom, which shows the number of items, each item and total. Each item can be removed individually using the bin icon, or the whole cart can be emptied. When removing an item, the page will stay looking at the cart info instead of scolling back to the top.

# product.html

When a product image is clicked on the index page, the user is taken to the specific product page using its ID, which displays more info about that product, such as more images, a description, a price, etc. The user can add the item to their cart, and can still see and update their cart at the bottom.

# script.js

The javascript functionality; creates a button for triggering light or dark mode and stores that when navigating pages. Updates the main image on the product page when a different image is clicked. Ensures each 'Add to Cart' button on the page has an event listener to handle which product is added to the cart.

# style.css

The css to style the page. Includes variables to control the light/dark mode colours.

