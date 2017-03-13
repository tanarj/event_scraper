## Motivation

This project can be used to scrape **major events**(in terms of population) in Chicago from a variety of datasources. It can be extended to other cities/localities by changing the datasources used to scrape. Specifically, a website for scraping, an element along with an identifying id/class should be mentioned (EventScraper.py/web_elems), and finally the information required should be considered as well (how you define an event). In order to make this project generic, currently we are only looking at name, time, date, location, and description of events. 


## Code Example
```
scraper = EventScraper("http://xyz.com")#Datasource should have a corresponding element,id to scrape from in EventScraper.py.web_elems
event_list = sorted(scraper.scrape(), key = lambda x: x.date_time)#Return a list of sorted events by date_time
```

## Tests

Test will be here soon.
