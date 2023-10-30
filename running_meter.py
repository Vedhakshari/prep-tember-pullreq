import tkinter as tk
import time
import googlemaps


google_maps_api_key = 'YOUR_API_KEY_HERE'


gmaps = googlemaps.Client(key=google_maps_api_key)


def update_meter():
    global distance
   
    current_location = (your_latitude, your_longitude)
    if prev_location is not None:
        
        distance += calculate_distance(prev_location, current_location)

  
    meter_label.config(text=f"{distance:.2f} meters")
    
   
    prev_location = current_location
    
    
    root.after(100, update_meter)


def calculate_distance(coord1, coord2):
    directions = gmaps.directions(coord1, coord2, mode="walking")
    if directions:
        distance = directions[0]['legs'][0]['distance']['value']  
        return distance
    else:
        return 0


root = tk.Tk()
root.title("Running Meter")


distance = 0.0
prev_location = None


your_latitude = 0.0
your_longitude = 0.0


meter_label = tk.Label(root, text="0.0 meters", font=("Helvetica", 24))
meter_label.pack(pady=20)


update_meter()


root.mainloop()
