#Movie type preference

action = input("Do you like to watch action movies?(yes/no)").lower() == "yes"
comedy = input("Do you like to watch comedy?(yes/no)").lower() == "yes"
drama = input("Do you like to watch drama?(yes/no)").lower() == "yes"

#boolean using logical operator

if action and comedy and not drama:
    genre = "Action-Comedy"
elif action and drama and comedy:
    genre = "Action-Drama"
elif comedy and drama and not action:
    genre = "Comedy-Drama"
elif action:
    genre = "action"
elif comedy:
    genre = "comedy"
elif drama:
    genre = "drama"
else:
    genre = "other"

# Movies recommendation based on choice

if genre == "Action-Comedy":
    print("Recommended movies: 'Rush Hour','Bad Boys','The nice guys'")
elif genre == "Action-Drama":
    print("Recommended movies: 'The Dark Knight','Inception','John Wick'")
elif genre == "Comedy-Drama":
    print("Recommended movies: 'The Big Sick','Littel Miss Sunshine','The Intouchables'")
elif genre == "Action":
    print("Recommended movie: 'Die Hard','The Matrix','Mission: Impossible'")
elif genre == "Comedy":
    print("Recommended movie: 'The Hangover','Superbad','Bridesmaids'")
elif genre == "drama":
    print("Recommended movies: 'The Shawshank Redemption','Forrest Gump',''The Green Mile")
else:
    print("Sorry, we couldn't recognize your movie preference")