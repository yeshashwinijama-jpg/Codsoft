print("🎬 Movie Recommendation System")
genre = input("Enter genre: ")
if genre == "action":
    print("Recommended Movies:")
    print("1. Avengers")
    print("2. John Wick")
    print("3. Batman")
elif genre == "comedy":
    print("Recommended Movies:")
    print("1. Mr Bean")
    print("2. Jumanji")
    print("3. Home Alone")
elif genre == "horror":
    print("Recommended Movies:")
    print("1. Conjuring")
    print("2. Annabelle")
    print("3. Nun")
elif genre == "thriller":
    print("Recommended Movies:")
    print("1. Inception")
    print("2. Shutter Island")
    print("3. Fight Club")
else:
    print("Genre not found")