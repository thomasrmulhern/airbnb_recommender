# airbnb_recommender
### INPUT: 

###### csv_filename_with_airbnb_user_reviews (csv), user_id_for_which_to_gather_recommendations (string of ints), do_you_want_the_web_pages_displayed (yes/no)

### OUTPUT: 

###### list of tuples(id of recommended listing , number of shared people with whom you share a common listing)

#### Description:

###### This is from Jonathan Dinu's "Cheaper Beds, Better Breakfasts' project from his "Data Science Fundamentals" series on Safaribooksonline.com.

#### Define the problem: 

###### Aid users in their discovery of relevant listings

#### Acquire data: 

###### Used open data from InsideAirBnB

#### Integration: 

###### Used Python standard library to parse csv files

#### Exploration: 

###### Initially looked at recommendations for Jonathan, and came back to look at other users

#### Analysis: 

###### Created social recommendations through triangle closing

#### Evaluation: 

###### Compared our results to a baseline we created, and to recommendations given by airbnb

#### Presentation:

###### Create the option to open recomended listings in web browser

#### Dissemination:

###### Packaged code into a module thats usuable by others

