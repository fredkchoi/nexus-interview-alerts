# nexus-interview-alerts

I had a NEXUS (https://www.cbp.gov/travel/trusted-traveler-programs/nexus) scheduled for 12/24, however it was cancelled due to the winter storm :(

NEXUS interviews are notoriously hard to schedule due to a lack of available timeslots, and the backlog has grown to over 300,000. I realized that by running a script to call the API used by the scheduler webpage (https://ttp.cbp.dhs.gov/schedulerui/schedule-interview/location?lang=en&vo=true&returnUrl=ttp-external&service=nh), I could potentially set up a system to alert myself when an interview time becomes available. I currently have the frequency set to every 10 mins, as I plan to integrate this script with the Mailgun Free tier, which allows for 5000 emails/month.
