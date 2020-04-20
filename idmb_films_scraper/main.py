import films as f
import related_films as r
import dataframing as df

films = [""] #You Can place a single ID or a list of them
related = False

def main(films, related):

	movies_collection = []

	movies = f.scrape(films)
	movies_collection.extend(movies)

	related_movies = r.controller(movies, related)
	movies_collection.extend(related_movies)

	data = df.export(movies_collection)

if __name__ == "__main__":
	main(films, related)