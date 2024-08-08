import pandas as pd
import os
from geopy.geocoders import Nominatim
from gmplot import gmplot

# Function to read CSV file and return dataframe
def read_csv(file_path):
    df = pd.read_csv(file_path)
    return df

# Function to get latitude and longitude for an address
def geocode_address(address):
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.geocode(address)
    if location:
        return location.latitude, location.longitude
    else:
        return None, None

# Function to plot locations on Google Map
def plot_locations(df, poc_df, api_key):
    # Initialize the map to the center of Germany
    gmap = gmplot.GoogleMapPlotter(51.1657, 10.4515, 6, apikey=api_key)
    
    # Plot main locations
    for index, row in df.iterrows():
        address = f"{row['Straße']}, {row['Ort']}, {row['PLZ']}, Germany"
        lat, lon = geocode_address(address)
        if lat and lon:
            gmap.marker(lat, lon, title=row['Ort'], color='red')

    # Plot POC locations
    for index, row in poc_df.iterrows():
        address = f"{row['Ort']}, Germany"
        lat, lon = geocode_address(address)
        if lat and lon:
            info = f"{row['poc_name']}, {row['contact_number']}, {row['Ort']}"
            gmap.marker(lat, lon, title=info, color='blue')
    
    # Draw the map
    gmap.draw("index.html")

# Main execution
if __name__ == "__main__":
    main_file_path = "data/location_data.csv"  # Path to the main locations CSV file
    poc_file_path = "data/poc_details.csv"  # Path to the POC data CSV file
    api_key = "AIzaSyBVii0lHnauDP5wSoiEoqDdf8tatWKYnPk"  # Replace with your actual Google Maps API key
    #api_key = os.getenv("GOOGLE_MAPS_API_KEY")  # Read API key from environment variable
    
    df = read_csv(main_file_path)
    poc_df = read_csv(poc_file_path)
    plot_locations(df, poc_df, api_key)
    print("Map has been created and saved as index.html")
