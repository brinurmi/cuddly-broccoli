# Description: Create a movie storage application, that will allow users
# to manage their movie collection and find any movie they want.

# Three main features:
# 1. Must allow adding new movies to the collection
# 2. Must allow users to view all movies in their collection
# 3. Allow user to find any movie by its attribute

# Conditions:
# Movies will be dictionaries, but can define the dictionary to be anything
#   Example: a dictionary with only 3 keys
#        {'name': 'The Matrix,
#         'director': 'Wachowskis',
#         'year': '1994}
#   Or you could have more than 3 keys:
#       -name
#       -director
#       -year
#       -location
#       -shelf
#
# Movies can be stored any way, as long as they can be printed, retrieved, and found.
#
# Finding Movies: user will give a property to search for
# Example: "Find all movies released in 1999" (i.e. search via year)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

MENU_PROMPT = """
~Movie Menu~
Choose from the following..
 'a' to add a movie
 'l' to see your movies
 'f' to find a movie by title
 'q' to quit
Enter option: """

movies = []


# Add new movie to the list
def add_movie(movies):
    # Get movie from user
    title = input("Enter the movie title: ")
    director = input("Enter the movie director: ")
    year = input("Enter the movie release year: ")
    rating = input("Enter the movie rating: ")

    # add to list
    movies.append({
        'title': title,
        'director': director,
        'year': year,
        'rating': rating,
    })



#   - listing movies
def list_movies(movie):
    title = movie["title"]
    director = movie["director"]
    year = movie["year"]
    rating = movie["rating"]

    print(f"Title: {title}\nDirector: {director}\nYear: {year}\nRating: {rating}\n")

    # for movie in movies:
    #     title = movie["title"]
    #     director = movie["director"]
    #     year = movie["year"]
    #     rating = movie["rating"]
    #
    #     print(f"Title: {title}\nDirector: {director}\nYear: {year}\nRating: {rating}\n")



#   - finding movies
def find_movie(movies):
    SEARCH_PROMPT = """
    ~Movie Search~
    Choose a criteria to search by..
     't' to search via movie title
     'd' to search via movie director
     'y' to search via movie release year
     'r' to search via movie rating
     'q' to cancel search and return to main menu
    Enter option: """

    selection = input(SEARCH_PROMPT)
    while selection != 'q':
        if selection == 't':
            search = input("Enter movie title: ")
            print(f"List of movies titled {search}:")
            for movie in movies:
                if search == movie["title"]:
                    list_movies(movie)

        elif selection == 'd':
            search = input("Enter movie director: ")
            print(f"List of movies directed by {search}:")
            for movie in movies:
                if search == movie["director"]:
                    list_movies(movie)

        elif selection == 'y':
            search = input("Enter movie year: ")
            print(f"List of movies released in {search}:")
            for movie in movies:
                if search == movie["year"]:
                    list_movies(movie)

        elif selection == 'r':
            search = input("Enter movie rating: ")
            print(f"List of movies rated {search}:")
            for movie in movies:
                if search == movie["rating"]:
                    list_movies(movie)
        else:
            print('Unknown command. Please try again.')

        selection = input(SEARCH_PROMPT)


# And another function here for the user menu
def user_menu(MENU_PROMPT):
    selection = input(MENU_PROMPT)
    while selection != 'q':
        if selection == "a":
            add_movie(movies)
        elif selection == "l":
            print("\nList of movies in your inventory:")
            for movie in movies:
                list_movies(movie)
        elif selection == "f":
            find_movie(movies)
        else:
            print('Unknown command. Please try again.')

        selection = input(MENU_PROMPT)

user_menu(MENU_PROMPT)

# Remember to run the user menu function at the end!
