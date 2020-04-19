import films as f
import related_films as r
import dataframing as df

films = ["items_list"] #You Can place a single ID or a list of them

def main(films):

	movies_collection = []

	movies = f.scrape(films)
	movies_collection.extend(movies)

	related_movies = r.controller(movies)
	movies_collection.extend(related_movies)

	data = df.export(movies_collection)

if __name__ == "__main__":
	main(films)