import phonenumbers
from phonenumbers import geocoder, carrier
import folium
from opencage.geocoder import OpenCageGeocode #+917232069038||+85252281109

# Taking input the phone number along with the country code
number = input("Enter the PhoneNumber with the country code: ")
phoneNumber = phonenumbers.parse(number)

# Storing the API Key in the Key variable (replace with your valid API key)
Key = "07ddafea180a49218413ac959eba8e57"

# Using the geocoder module of phonenumbers to get the location
yourLocation = geocoder.description_for_number(phoneNumber, "en")
print("Location: " + yourLocation)

# Using opencage to get the latitude and longitude of the location
geocoder = OpenCageGeocode(Key)
query = str(yourLocation)
results = geocoder.geocode(query)

if results:
    lat = results[0]['geometry']['lat']
    lng = results[0]['geometry']['lng']
    print(lat,lng)

    # Using the carrier module of phonenumbers to get the service provider name
    yourServiceProvider = carrier.name_for_number(phoneNumber, "en")
    print("Service provider: " + yourServiceProvider)

    # Getting the map for the given latitude and longitude
    myMap = folium.Map(location=[lat, lng], zoom_start=9)

    # Adding a Marker on the map to show the location name
    folium.Marker([lat, lng], popup=yourLocation).add_to(myMap)

    # Save map to HTML file to view the location
    myMap.save("Location.html")
else:
    print("No location found for the given phone number.")
