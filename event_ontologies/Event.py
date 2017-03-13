"""High-level ontology for an event, and sub-classes relating to specific event types

Copyright (c) 2017 Arjun Tanguturi (tanarj)
License: BSD 3
"""

from dateutil.parser import parse
from dateutil.tz import gettz
from event_ontologies.Location import Location

class Event:
    def __init__(self, eventname):
        self.event_name = eventname

    def add_location(self, place_of_event):
        loc = Location(place_of_event)
        self.location = loc

    def add_eventtime(self, time_of_event, date_of_event):
        self.date_time = parse(date_of_event+" 2017 "+time_of_event,fuzzy=True).replace(tzinfo=gettz("America/Chicago"))
    
    def __str__(self):
        return "Event: " + self.event_name + "\nLocation: " +self.location.address + "\nDate+Time: " + self.date_time.strftime("%A, %B %d, %Y at %I:%M %p\n")
    
class PlannedEvent(Event):
    def __init__(self, eventname, location, time, date, description = None):
        super().__init__(eventname)
        self.add_location(location)
        self.add_eventtime(time,date)
        self.description = description