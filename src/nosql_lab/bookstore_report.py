#!/usr/bin/env python3

from pymongo import MongoClient
import os
import json
import logging

#start logger
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)

#getting environment variables
ATLASURL = os.getenv('MONGODB_ATLAS_URL')
ATLASUSER = os.getenv('MONGODB_ATLAS_USER')
ATLASPASS = os.getenv('MONGODB_ATLAS_PWD')

#defining a mongo clinet
client = MongoClient(ATLASURL, username=ATLASUSER, password=ATLASPASS, connectTimeoutMS=200, retryWrites = True)

#defining main function to meet specifications
def main():
	"""complete tasks as listed in github instructions"""
	try:
		db = client["bookstore"]
		authors_collection = db['authors']
		books_collection = db['books']
		
		### making list of ids
		author_ids_list = ['author_002', 'author_003', 'author_005']
		
		##log that connection was successful
		logger.info("Successfully connected to MongoDB Atlas")
		
		##print number of authors in list
		author_num = authors_collection.count_documents({ "_id": { "$in": author_ids_list } })
		print("Number of authors:",author_num)
		
		##print each author, along with their books
		for author_id in author_ids_list:
			auth_name = authors_collection.find_one({ "_id": author_id })
			print(f"{auth_name.get('name')}")
			
			##get books linked to author
			linked_books = books_collection.find( { "author_ids": auth_name["_id"] } )
			
			##print those linked books
			for book in linked_books:
				title = book.get("title")
				year = book.get("published_year")
				print(f"  {title} ({year})")
	except Exception as e:
		logger.error(f"Connection failed: {e}")
	finally:
		client.close()

##create the if main function to run
if __name__ == "__main__":
	main()
