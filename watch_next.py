import spacy
nlp = spacy.load("en_core_web_md")

# Create a function that returns which movies a user would watch next if they have watched Planet Hulk
# This function takes the description of Planet Hulk as a parameter and returns the title of the most similar movie
def movie_suggestion(description):
    
    # List of movies
    movies = ["Movie A :When Hiccup discovers Toothless isn't the only Night Fury, he must seek \"The Hidden World\", a secret Dragon Utopia before a hired tyrant named Grimmel finds it first.", 
    "Movie B :After the death of Superman, several new people present themselves as possible successors.",
    "Movie C :A darkness swirls at the center of a world-renowned dance company, one that will engulf the artistic director, an ambitious young dancer, and a grieving psychotherapist. Some will succumb to the nightmare. Others will finally wake up.",
    "Movie D :A humorous take on Sir Arthur Conan Doyle's classic mysteries featuring Sherlock Holmes and Doctor Watson.",
    "Movie E :A 16-year-old girl and her extended family are left reeling after her calculating grandmother unveils an array of secrets on her deathbed.",
    "Movie F :In the last moments of World War II, a young German soldier fighting for survival finds a Nazi captain's uniform. Impersonating an officer, the man quickly takes on the monstrous identity of the perpetrators he is trying to escape from.",
    "Movie G :The world at an end, a dying mother sends her young son on a quest to find the place that grants wishes.",
    "Movie H :A musician helps a young singer and actress find fame, even as age and alcoholism send his own career into a downward spiral.",
    "Movie I :Corporate analyst and single mom, Jen, tackles Christmas with a business-like approach until her uncle arrives with a handsome stranger in tow.",
    "Movie J :Adapted from the bestselling novel by Madeleine St John, Ladies in Black is an alluring and tender-hearted comedy drama about the lives of a group of department store employees in 1959 Sydney."]

    model_movie = nlp(description)

    # Empty list where the similarities will be stored
    similarities = []

    for movie in movies:
        similarity = nlp(movie).similarity(model_movie)
        similarities.append(similarity)
    
    # Find out the index of the movie with the highest similarity to Planet Hulk
    # Return the title of the movie with the highest similarity based on the shared index
    index = similarities.index(max(similarities))
    movie_to_recommend = movies[index]
    movie_to_recommend = movie_to_recommend.split(" :")[0]
    print(f"If you liked Planet Hulk, you will like {movie_to_recommend}.")



movie_suggestion("Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator.")