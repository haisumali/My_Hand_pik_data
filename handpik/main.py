import asyncio
import json
import logging.config
import os

from scrapers.zeenwomen.scraper import KhaddiScrapper  

def setup_logging():
    with open("utils/logging_config.json") as f:
        config = json.load(f)
    logging.config.dictConfig(config)

async def main():
    setup_logging()
    scraper = KhaddiScrapper()
    await scraper.scrape_data()

if __name__ == "__main__":
    asyncio.run(main())

if __name__ == "__main__":
    asyncio.run(main())
