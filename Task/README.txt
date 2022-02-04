"""
AMAZON DATA SCRAPING
"""

DOWNLOAD MODULES
pip install beautifulsoup, requests, pandas

1. The CSV data file is loaded using pandas
2. The urls are extracted from the csv and appened to the urls list to work with
3. Setting up BeautifulSoup4 to extract data from the working urls
4. There are 4 functions to extract each, title, price, image source, and description
5. If the url has a valid "Product Title" means it's a valid page else it's invalid url and data can't be extracted
6. Iterating through the urls list and checking if it's valid then performing the functions to extract data
7. Storing the data in a dictionary with key being serial numbers from 1 to n..
   Values = [url, title, price, image source, description]

   Format of dictionary -> 1 : [url, title, price, image source, description]	
		           2 : [url, title, price, image source, description]


8. Final dictionary is then dumped into a json file name "output.json"
9. Reading the final json file
10. Creating a list of tuples for storing the json values 
11. Dumping the list of tuples to the SQLite database name "output.db"