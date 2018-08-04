
# #FIRST ITERATION
# import csv

# # Open and parse CSV file
# csvfile = open('/Users/thomasmulhern/new_desk/post_7:6:18/learning/add_learning/jonathan_dinu/\
# data-science-fundamentals/code/data/airbnb/seattle_reviews_01_04_2016.csv', newline='')
# csvreader = csv.reader(csvfile)
# header = next(csvreader)
# records = list(csvreader)

# # Set user for recommendations
# jonathan = '1465258'
# jonathan_reviews = []

# # Find listings of user
# for row in records:
#     if row[3] == jonathan:
#         jonathan_reviews.append(row)

# fellow_travelers = set()
# listings = set( [review[0] for review in jonathan_reviews])

# # Find fellow travellers
# for row in records:
#     if row[0] in listings:
#         fellow_travelers.add(row[3])

# fellow_listings = []

# # Find triangles users a part of
# for row in records:
#     if row[3] in fellow_travelers:
#         fellow_listings.append(row[0])

# print(len(fellow_listings)) 

#################################################################################################################

# SECOND ITERATION
# GENERALIZE INTO FUNCTIONS

# import csv
# import collections as col 

# # Open and parse CSV file
# csvfile = open('/Users/thomasmulhern/new_desk/post_7:6:18/learning/add_learning/jonathan_dinu/\
# data-science-fundamentals/code/data/airbnb/seattle_reviews_01_04_2016.csv', newline='')
# csvreader = csv.reader(csvfile)
# header = next(csvreader)
# records = list(csvreader)
# jonathan = '1465258'


# def find_listings(records, user_id):
#     listings = set()

#     # Find listings of user
#     for row in records:
#         if row[3] == user_id:
#             listings.add(row[0])

#     return listings


# def find_travellers(records, listings):
#     fellow_travelers = set()

#     # Find fellow travellers
#     for row in records:
#         if row[0] in listings:
#             fellow_travelers.add(row[3])
#     return fellow_travelers


# def count_triangles(records, fellow_travelers):
#     triangles = []

#     # Find triangles users a part of
#     for row in records:
#         if row[3] in fellow_travelers:
#             triangles.append(row[0])
#     return col.Counter(triangles)

# def recommend_listings(counts, user_listings, num=5):
#     for listing in user_listings:
#         if listing in counts:
#             counts.pop(listing)

#     return counts.most_common(num)

#################################################################################################################


# THIRD ITERATION
# ADD WEB CHECKS AND if __name__ == '__main__'

import csv, sys, webbrowser
import collections as col 


def find_listings(records, user_id):
    listings = set()

    # Find listings of user
    for row in records:
        if row[3] == user_id:
            listings.add(row[0])

    return listings


def find_travellers(records, listings):
    fellow_travelers = set()

    # Find fellow travellers
    for row in records:
        if row[0] in listings:
            fellow_travelers.add(row[3])
    return fellow_travelers


def count_triangles(records, fellow_travelers):
    triangles = []

    # Find triangles users a part of
    for row in records:
        if row[3] in fellow_travelers:
            triangles.append(row[0])
    return col.Counter(triangles)

def recommend_listings(counts, user_listings, num=10):
    for listing in user_listings:
        if listing in counts:
            counts.pop(listing)

    return counts.most_common(num)

if __name__ == '__main__':
    filename, user_id, want_web_pages_displayed = sys.argv[1:]

    # Open and parse CSV file
    csvfile = open(filename, newline='')
    csvreader = csv.reader(csvfile)
    header = next(csvreader)
    records = list(csvreader)

    # test user id :'1465258'
    user_listing = find_listings(records, user_id)
    user_fellows = find_travellers(records, user_listing)
    counts = count_triangles(records, user_fellows)
    recommendations = recommend_listings(counts, user_listing)

    # Present the results
    if want_web_pages_displayed == '1':
        [webbrowser.open('http://airbnb.com/rooms/' + rec[0]) for rec in recommendations]
    else: 
        pass    
    
    print(recommendations)
