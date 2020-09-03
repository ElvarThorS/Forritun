no_of_days = int(input("Number of days after 9/25/09: "))
no_of_hours = no_of_days * 24
no_of_minutes = no_of_hours * 60
no_of_seconds = no_of_minutes * 60

distance_miles = int(16637000000)
velocity = int(38241)
miles_to_km = float(1.609344)
miles_to_AU = float(92955887.6)
speed_of_light = int(299792458)
km_to_m = 1000

round_trip_time = ((distance_miles * miles_to_km * km_to_m) + (no_of_hours * velocity * miles_to_km * km_to_m))/speed_of_light

print('Miles from the sun: ',distance_miles + no_of_hours * velocity)
print('Kilometers from the sun: ',round(distance_miles * miles_to_km + no_of_hours * velocity * miles_to_km))
print('AU from the sun: ', round(distance_miles / miles_to_AU + no_of_hours * velocity / miles_to_AU))
#print('Radio round trip time: ',round(round_trip_time/3600,1))

