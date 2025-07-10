import requests
import datetime
from ics import Calendar

def get_events_from_ical(url, year, month):
    response = requests.get(url)
    c = Calendar(response.text)
    print(f"Fetched {len(c.events)} events from the calendar.")
    # with open('calendar.ics', 'wb') as f:
    #     f.write(response.text.encode('utf-8'))
    events_list = []
    
    for event in c.events:
        start = event.begin.datetime

        if start.year == year:
            events_list.append({
                "date": start.isoformat(),
                "title": event.name,
                "location": event.location or ""
            })

    return events_list

# Example
ical_url = "https://calendar.google.com/calendar/ical/hhlp4gcgvdmifq5lcbk7e27om4@group.calendar.google.com/public/basic.ics"
events = get_events_from_ical(ical_url, 2025, 7)
print(events)
import json
with open('santa_calendar.json', 'w') as f:
    json.dump(events, f, indent=2)

