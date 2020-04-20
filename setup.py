import setuptools


setuptools.setup(name='imdb_films_scraper',
      version="1.0.1",
      url = "https://github.com/AdriaPadilla/imdb_films_scraper/", 
      description='Scrape Film data from IMDB',
      author='Adrian Padilla',
      author_email='adrian.padilla.m@gmail.com',
      packages=setuptools.find_packages(),
      install_requires=["numpy", "pandas", "requests", "beautifulsoup4", "openpyxl", "tqdm"],
      classifiers=[
       "Programming Language :: Python :: 3",
       "License :: OSI Approved :: MIT License",
       "Operating System :: OS Independent",
       ],
     )
