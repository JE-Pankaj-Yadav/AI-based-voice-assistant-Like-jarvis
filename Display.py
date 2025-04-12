import psutil
import speedtest
from requests import get
from bs4 import BeautifulSoup


# Weather forecast
@staticmethod
def temperature():
    try:
        IP_Address = get("https://api.ipify.org").text
        url = "https://get.geojs.io/v1/ip/geo/" + IP_Address + ".json"
        geo_reqeust = get(url)
        geo_data = geo_reqeust.json()
        city = geo_data["city"]
        search = f"temperature in {city}"
        url_1 = f"https://www.google.com/search?q={search}"
        r = get(url_1)
        data = BeautifulSoup(r.text, "html.parser")

        # Try multiple class names
        temp_element = data.find("div", class_="BNeawe iBp4i AP7Wnd") or data.find(
            "div", class_="BNeawe"
        )

        if temp_element:
            temp = temp_element.text
            return f"Current {search} is {temp}"
        return "Temperature data not available"
    except Exception as e:
        print(f"Error fetching temperature: {e}")
        return "Could not fetch temperature data"


# Internet speed
def InternetSpeed():
    try:
        import speedtest

        st = speedtest.Speedtest()
        dl = st.download()
        dl = dl / (1000000)  # converting bytes to megabytes
        up = st.upload()
        up = up / (1000000)
        return f"Download Speed: {round(dl,2)} MB/s \nUpload Speed: {round(up,2)} MB/s"
    except Exception as e:
        print(f"Error checking internet speed: {e}")
        return "Could not check internet speed at this time"


# System condition
def Battery_condition():
    battray = psutil.sensors_battery()
    percentage = battray.percent
    return percentage


def IP():
    ip = get("https://api.ipify.org").text
    return f"IP address is: {ip}"
