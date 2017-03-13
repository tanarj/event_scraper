"""Event Scraper class that uses requests, as well as BeautifulSoup4 to scrape event information from websites
of interest

Copyright (c) 2017 Arjun Tanguturi (tanarj)
License: BSD 3
"""

import requests
from bs4 import BeautifulSoup
from event_ontologies.Event import PlannedEvent

web_elems = {
        "United Center" : ("http://www.unitedcenter.com/events/",["li","CT_Main_1"],["title","duration","dateIcon","description"])
    }


class EventScraper:
    """
    This class scrapes planned events based on the web elems. Web elems contains HTML class names, as well as the
    list names needed to scrape event information from a specific website.
    """
    def __init__(self, event_name):
        self.event_name = event_name

    def scrape(self):
        html_page = requests.get(web_elems[self.event_name][0])
        if(html_page.status_code==200):
            scraper = BeautifulSoup(html_page.content, "lxml")
            if isinstance(web_elems[self.event_name][1],list):
                events = scraper.find_all(web_elems[self.event_name][1][0],id = lambda x: x and x.startswith(web_elems[self.event_name][1][1]))
            else:
                events = scraper.find_all(id = lambda x: x and x.startswith(web_elems[self.event_name][1]))
            event_list = []
            print(len(events))
            for event in events:
                event_list.append(self.scrape_page(event))
            return event_list

    def scrape_page(self, event):
        name = event.find(class_=web_elems[self.event_name][2][0]).text
        location = self.event_name + ", Chicago"
        time = event.find(class_=web_elems[self.event_name][2][1]).text.strip()
        date = event.find(class_=web_elems[self.event_name][2][2]).text.strip().replace("\n"," ")
        description = event.find(class_=web_elems[self.event_name][2][3]).text.strip()
        return PlannedEvent(name,location,time,date,description)
