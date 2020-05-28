from  geopy.geocoders import Nominatim
def weather():
    geolocator = Nominatim()
    city = input('Enter city: ')
    country =input('Enter country: ')
    loc = geolocator.geocode(city+','+ country)
    print("latitude is :-" ,loc.latitude,"\nlongtitude is:-" ,loc.longitude)

    import requests 
  
# api-endpoint 
    URL = "http://api.weatherunlocked.com/api/current/"
  
# location given here 
    location = "delhi technological university"
  
# defining a params dict for the parameters to be sent to the API 
    appID='f134de62'
    appKey='37ed7f8fb3d413880a6659c6240272d6'
    PARAMS = { 'app_id': appID, 'app_key': appKey} 
  
# sending get request and saving the response as response object 
    r = requests.get(url = URL+str(loc.latitude)+','+str(loc.longitude), params = PARAMS) 
  
# extracting data in json format 
    data = r.json()
    print(data)     
    URLf='http://api.weatherunlocked.com/api/forecast/'
    rf = requests.get(url = URLf+str(loc.latitude)+','+str(loc.longitude), params = PARAMS) 
    dataf=rf.json()
    print(dataf)
    return data,dataf