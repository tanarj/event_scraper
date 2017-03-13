"""Class used to call EventScrapers as we deem fit. Will be scheduled accordingly in the scheduler module.

Copyright (c) 2017 Arjun Tanguturi (tanarj)
License: BSD 3
"""

from web_scrapers.EventScraper import EventScraper


def main():
    uc = EventScraper("United Center")
    events = sorted(uc.scrape(), key=lambda x: x.date_time)
    for each in events:
        print(each)

if __name__ == "__main__":
    main()