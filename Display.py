import psutil
import speedtest
from requests import get
from bs4 import BeautifulSoup



#Weather forecast
def temperature():
    IP_Address = get('https://api.ipify.org').text
    url = 'https://get.geojs.io/v1/ip/geo/'+IP_Address+'.json'
    geo_reqeust = get(url)
    geo_data = geo_reqeust.json()
    city = geo_data['city']
    search = f"temperature in {city}"
    url_1 = f"https://www.google.com/search?q={search}"
    r = get(url_1)
    data = BeautifulSoup(r.text,"html.parser")
    temp = data.find("div",class_="BNeawe").text
    return f"Current {search} is {temp}"

#Internet speed
def InternetSpeed():
    st = speedtest.Speedtest()
    dl = st.download()
    dl = dl/(1000000) #converting bytes to megabytes
    up = st.upload()
    up = up/(1000000)
    return f'DS: {round(dl,2)}MB/s \n US: {round(up,2)}MB/s'
        
#System condition
def Battery_condition():
    battray = psutil.sensors_battery()
    percentage = battray.percent
    return percentage
    
    
    
def IP():
    ip = get('https://api.ipify.org').text
    return f"IP address is: {ip}"


    