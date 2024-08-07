import pandas as pd
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
def plot_locations(df, api_key):
    # Initialize the map to the center of Germany
    gmap = gmplot.GoogleMapPlotter(51.1657, 10.4515, 6, apikey=api_key)
    
    latitudes = []
    longitudes = []

    for index, row in df.iterrows():
        address = f"{row['Straße']}, {row['Ort']}, {row['PLZ']}, Germany"
        lat, lon = geocode_address(address)
        if lat and lon:
            latitudes.append(lat)
            longitudes.append(lon)
            gmap.marker(lat, lon, title=row['Ort'])
    
    # save the map as image
    gmap.draw("index.html")

# Main execution
if __name__ == "__main__":
    file_path = "data/location_data.csv"  # Update this path if necessary
    api_key = "AIzaSyBVii0lHnauDP5wSoiEoqDdf8tatWKYnPk"  # Replace with your Google Maps API key
    
    df = read_csv(file_path)
    plot_locations(df, api_key)
    print("Map has been created and saved as germany_map.html")
