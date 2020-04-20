import pandas as pd

def export(movies_collection):

	output_name = "output.xlsx"

	all_data = []

	for movie in movies_collection:
		movie_frame = pd.DataFrame({
			"seed": movie.seed,
			"id": movie.id,
			"url": movie.url,
			"title": movie.title,
			"year": movie.year,
			"genre": movie.genre,
			"duration": movie.duration,
			"rating": movie.rating,
			"n_votes": movie.n_votes,
			"country": movie.country,
			}, index=[0])
		all_data.append(movie_frame)

	all_data = pd.concat(all_data, ignore_index=True)
	all_data.to_excel(output_name)
	print("Job Done!")
	return all_data