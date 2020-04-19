import requests
from bs4 import  BeautifulSoup

import movie_class as mv

movies_objects_list = []

def scrape(films):

	for film in films:
		url = "https://www.imdb.com/title/{}/".format(film)
		page = requests.get(url)
		soup = BeautifulSoup(page.content, 'html.parser')

		#The Basics)
		film_id = film
		film_url = url

		#Film Title
		title = soup.find_all("h1")
		try:
			only_title = str(title[0]).split(">")[1].split("<")[0].replace("\xa0", "")
		except IndexError:
			only_title = str(title[0]).split(">")[1].split("<")[0]

		#Year
		year = str(title[0]).split(">")[3].split("<")[0]

		#Main Info
		info = soup.find_all("div", class_="subtext")
		genre = str(info[0]).split(">")[8].split("<")[0]
		duration = str(info[0]).split(">")[4].split("\n")[1].strip(" ")

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

		movie_object = mv.Movie(
			"user",
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
		movies_objects_list.append(movie_object)
		print("Starting Film: "+movie_object.title+" / "+movie_object.year+" / "+"rating: "+str(movie_object.rating))

	return movies_objects_list






