import psycopg2
import logging
from itemadapter import ItemAdapter

class ScraperPipeline:
    def __init__(self):
        self.create_connection()

    def create_connection(self):
        self.connection = psycopg2.connect(
            host = 'localhost',
            user = 'postgres',
            password='scraperdatabase',
            database='scraper',
            port='5432'
        )
        self.curr = self.connection.cursor()

    def insertData(self, item):
        try:
            adapter = ItemAdapter(item)
            title = adapter.get('title')
            image_urls = adapter.get('image_urls')

            for image_url in image_urls:
                # Execute an INSERT query to insert the data into the table
                self.curr.execute("INSERT INTO scraped (title, image_url) VALUES (%s, %s)", (title, image_url))

                # Commit the transaction to persist the changes
                self.connection.commit()
        except Exception as e:
                logging.error("Error inserting data: %s", str(e))

    def process_item(self, item, spider):
        self.insertData(item)
        return item
