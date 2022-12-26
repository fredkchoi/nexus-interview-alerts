import time
import json

from poll import poll_ttp_schedule 

# Adjust the frequency that the program checks for available appointments, in seconds
FREQUENCY = 600

# From locationId.json, add the names of the locations that you want to check
LOCATION_NAMES = [
    "Niagara Falls (Niagara Falls EC)",
    "Detroit (Detroit Enrollment Center)",
    "Fort Erie (Buffalo-Ft. Erie EC)"
]

# TODO: Add filters for state, country etc. and function to filter results before a
# specific date

# TODO: Mailgun API integration to send emails directly to email inbox

def main():
    while True:
        location_name_dict = {}
        
        with open('locations.json') as locations_json:
            locations_content = locations_json.read()
        
        locations = json.loads(locations_content)
        
        for location in locations:
            location_name_dict[location["label"]] = location["locationId"]
        
        for location_name in LOCATION_NAMES:
            print("Querying for " + location_name + ":")
            result = poll_ttp_schedule(location_name_dict[location_name])
            print(result)
        
        time.sleep(FREQUENCY)

if __name__ == "__main__":
    main()
    
    
    
    