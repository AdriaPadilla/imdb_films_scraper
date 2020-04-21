import requests
from bs4 import  BeautifulSoup
import movie_class as mv

from tqdm import tqdm
from time import sleep

def get_related(movies_objects_list, ammount, message):

	related_movies_objects_list = []

	pbar = tqdm(total=ammount, bar_format='{l_bar}{bar:20}{r_bar}{bar:-20b}', desc=message)

	for movie_object in movies_objects_list:

		seed = movie_object.id

		related_films = movie_object.related_films

		for related_film in related_films:

			url = "https://www.imdb.com/title/{}/".format(related_film)
			page = requests.get(url)
			soup = BeautifulSoup(page.content, 'html.parser')

			#The Basics)
			film_id = related_film
			film_url = url

			#Film Title
			title = soup.find_all("h1")
			try:
				only_title = str(title[0]).split(">")[1].split("<")[0].replace("\xa0", "")
			except IndexError:
				only_title = str(title[0]).split(">")[1].split("<")[0]

			#Year
			try:
				year = str(title[0]).split(">")[3].split("<")[0]
			except IndexError:
				year = "Nan"

			#Main Info
			info = soup.find_all("div", class_="subtext")
			genre = str(info[0]).split(">")[8].split("<")[0]
			try:
				duration = str(info[0]).split(">")[4].split("\n")[1].strip(" ")
			except IndexError:
				duration = "Nan"

			#rating
			rating = soup.find_all("span", itemprop="ratingValue")
			clean_rating = str(rating[0]).split(">")[1].split("<")[0]
			float_rating = float(clean_rating)

			#votes
			votes = soup.find_all("span", itemprop="ratingCount")
			only_votes = str(votes[0]).split(">")[1].split("<")[0]
			only_votes_clean = only_votes.replace(",", "")
			only_votes = int(only_votes_clean)

			#Country
			country = soup.find_all("div", class_="txt-block")
			only_country = str(country).split("/search/title?country_of_origin")[1].split(">")[1].split("<")[0]

			#Related
			related_films = soup.find_all("div", class_="rec_item")
			transactional_related_films = []
			for related_film in related_films:
				only_film = str(related_film).split("data-tconst=")[1].split(">")[0].split('"')[1]
				transactional_related_films.append(only_film)

			related_movie_object = mv.Movie(
				seed,
				film_id,
				film_url,
				only_title,
				year,
				genre,
				duration,
				float_rating,
				only_votes,
				only_country,
				transactional_related_films,
				)
			
			related_movies_objects_list.append(related_movie_object)

			pbar.update()

	return related_movies_objects_list

def controller(movies_objects_list, related):

	ammount = len(movies_objects_list)*12
	print("Total access points: "+str(len(movies_objects_list)))
	print("Total Related Movies: "+str(ammount))
	print("Please remember: Runtime depends on website response speed, be patient :)")
	print("Starting the job...")

	movies = []

	message = "1st Iteration -->"
	related_movies = get_related(movies_objects_list, ammount, message)
	movies.extend(related_movies)

	if related == True:
		new_ammount = len(movies)*12
		second_message = "2nd Iteration -->"
		more_related_movies = get_related(related_movies, new_ammount, second_message)
		movies.extend(more_related_movies)

	tqdm._instances.pop().close() # This close all tqdm instances and prevent from re-print
	
	return movies

