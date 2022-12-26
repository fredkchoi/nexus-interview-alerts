import requests

URL = "https://ttp.cbp.dhs.gov/schedulerapi/slots"
PARAMS = {
    "orderBy": "soonest",
    "limit": 20,
    "minimum": 1,
}

def poll_ttp_schedule(locationId):
    # print("Fetch API Request for: " + str(locationId))
    
    output = []
    request_params = PARAMS.copy()
    request_params["locationId"] = locationId

    results = requests.get(url = URL, params = request_params).json()

    for result in results:
        interview_date, interview_time = result["startTimestamp"].split("T")
        output.append({ "date": interview_date, "time": interview_time })

    return output

