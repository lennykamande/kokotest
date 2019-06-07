# koko networks test
This is a program to calculate and print a statement of a customer's charges at a book rental store.


## Getting Started
Clone the repo from GitHub:
    
    git clone :https://github.com/lennykamande/kokotest.git

Navigate to root folder
    `cd kokotest`

Create a virtual environment
    `virtualenv env`

Activate the virtual environment from the root folder
    `source .\env\Scripts\activate`

Install the required packages
    `pip install -r Requirements.txt`

## Starting the API

On the terminal type `export FLASK_APP=run.py` and type enter. Run `flask run`

## Use the following endpoints to perform the specified tasks
		 
| 	Endpoint                              | Functionality                                                  
| ----------------------------------------| -----------------------------------------------| 
| POST api/v1/signup                      | Create a user account                          |        
| POST /api/v1/signin                     | Sign in a user                                 |
| POST /api/v1/book                       | Request a booking                              |
| GET /api/v1/book                        | Retrieve all bookings                          | 
| GET /api/v1/book/<int:id>               | Retrieve a specific booking                    |
| PUT /api/v1/book/<int:id>/cancel	      | Cancel a specific booking                      |
| GET /api/v1/users/<int:id>/book         | Retrieve a specific user's bookings            |


## Application Features

1. Users can create an account and log in.
2. Users can request a book rental.
3. Users can cancel a book rental.
4. Users can see the details of a rental order.
5. Users can view all the rentals they have requested
6. Users can view a specific rental.

### Sample Data for testing the endpoints

#### Booking Data
            
        "title" 	     : "Song of ice and fire",
        "description" 	 : "Story based on the hit series game of thrones",
        "booking_days"   :  2 ,
        "books"          :  1   

#### User Data
            
        "user_name"   : "lennykamande",
        "user_email"  :  "lennymanyeki@gmail.com",
        "password"    :    "2019Koko"      
                                                
## Testing

To test run: `pytest`

## Built with...

* Python
* Flask
* Flask RESTful

### Credits
Coypright (c) [Lenny Kamande](https://github.com/lennykamande)