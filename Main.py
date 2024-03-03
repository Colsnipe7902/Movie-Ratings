def view_all_movies():
    if not movies:
        print("No movies available.")
        return

    for name, rating in movies.items():
        print(f"{name}'s rating is {rating}")


def view_movie():
    movie_name = input("Enter the name of the movie you want to view: ")
    if movie_name not in movies:
        print(f"{movie_name} is not found in the watched movies.")
    else:
        print(f"{movie_name}'s rating is {movies[movie_name]}")


def add_movie():
    movie_name = input("Enter the name of the movie you want to add: ")
    rating = float(input(f"Enter the rating of {movie_name}: "))
    movies[movie_name] = rating
    print(f"{movie_name} was added to your watched movies.")


def update_movie():
    movie_name = input("Enter the name of the movie you want to update: ")
    if movie_name not in movies:
        print(f"{movie_name} is not found in the watched movies.")
    else:
        new_rating = float(input(f"Enter the new rating of {movie_name}: "))
        movies[movie_name] = new_rating
        print(f"{movie_name}'s rating has been updated to {new_rating}.")


def remove_movie():
    movie_name = input("Enter the name of the movie you want to remove: ")
    if movie_name not in movies:
        print(f"{movie_name} is not found in the watched movies.")
    else:
        del movies[movie_name]
        print(f"{movie_name} has been removed from your watched movies.")


options = """
    (1) View all watched movies
    (2) View movie rating 
    (3) Add movie               
    (4) Update movie rating 
    (5) Remove movie            
    (6) Exit
"""

movies = {
    "The Godfather": 0,
    'Lion King': 5.0,
}

while True:
    print(options)
    choice = input("Enter your choice: ")

    if choice == '1':
        view_all_movies()
    elif choice == '2':
        view_movie()
    elif choice == '3':
        add_movie()
    elif choice == '4':
        update_movie()
    elif choice == '5':
        remove_movie()
    elif choice == '6':
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 6.")
