
class Movie:
	
	def __init__(self,
		seed,
		id,
		url,
		title,
		year,
		genre,
		duration,
		rating,
		n_votes,
		country,
		related_films,
		):
		self.seed = seed
		self.id = id
		self.url = url
		self.title = title
		self.year = year
		self.genre = genre
		self.duration = duration
		self.rating = rating
		self.n_votes = n_votes
		self.country = country
		self.related_films = related_films
