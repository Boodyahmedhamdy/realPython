import geocoder
import folium

theIp = input('enter the ip address : ')

g = geocoder.ip(theIp)
myAddress = g.latlng
print(myAddress)

myMap = folium.Map(location=myAddress, zoom_start=12)
myMap.save("location.html")
