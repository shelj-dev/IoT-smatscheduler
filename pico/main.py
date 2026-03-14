import network
import time
import urequests
from machine import Pin


WIFI_SSID = "iot kids"
WIFI_PASSWORD = "bright kidoos"

SERVER_IP_URL = "http://10.189.178.236:8000/"

wifi_status = False

relay1 = Pin(16, Pin.OUT)
relay2= Pin(17, Pin.OUT)
sensor_pin = Pin(26, Pin.IN)

timeout = False
timelim = 0


def connect_wifi():
    global wifi_status

    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)

    if wlan.isconnected():
        wifi_status = True
        print("WiFi connected:", wlan.ifconfig()[0])
        return

    if not wlan.isconnected():

        print("Connecting to WiFi...")
        wlan.connect(WIFI_SSID, WIFI_PASSWORD)

        timeout = 5
        while timeout > 0 and not wlan.isconnected():
            print("Waiting for connection...")
            time.sleep(1)
            timeout -= 1

    wifi_status = wlan.isconnected()

    if wifi_status:
        print("WiFi connected:", wlan.ifconfig()[0])
    else:
        print("WiFi failed")


def relay1_on():
    relay1.value(1)
    print("Relay ON")


def relay1_off():
    relay1.value(0)
    print("Relay OFF")
    
def relay2_on():
    relay2.value(1)
    print("Relay ON")


def relay2_off():
    relay2.value(0)
    print("Relay OFF")


def sensor_data():
    value = sensor_pin.value()
    print("Sensor value:", value)
    return value


def send_data(data):

    payload = {
        "sensor": data
    }

    url = SERVER_IP_URL + "api/get-sensor/"

    r = None

    try:
        r = urequests.post(url, json=payload)
        print("Server response:", r.text)

    except Exception as e:
        print("Send error:", e)

    finally:
        if r is not None:
            r.close()


def get_data():

    url = SERVER_IP_URL + "api/send-relay/"
    
    try:
        r = urequests.get(url)
        data = r.json()
        r.close()
        
        print(data)
        return data

    except Exception as e:
        print("Get error:", e)
        return None


def automode(motion, lim_val):
    global timeout, timelim

    if motion == 1:
        r1.value(0)
        r2.value(0)
        timelim = lim_val
        timeout = False

    else:
        if timelim > 0:
            timelim -= 1

        if timelim == 0:
            timeout = True

        if timeout:
            r1.value(1)
            r2.value(1)

def main():
    while True:
        connect_wifi()
        sensor = sensor_data()
        
        if wifi_status:
            send_data(sensor)
            
            data = get_data()

            schedule_automode = data.get("schedule_automode")
            schedule_on_time=data.get("schedule_on_time")
            schedule_off_time=data.get("schedule_off_time")
            sensor_automode=data.get("sensor_automode")
            sensor_threshold=data.get("sensor_threshold")
            sensor_off_delay=data.get("sensor_off_delay")
            light=data.get("light")
            fan=data.get("fan")


            if schedule_automode == True:
                if schedule_on_time:
                    ...

            elif sensor_automode == True:
                automode(sensor, sensor_off_delay)
            
            else:
                if light==True:
                    relay1_on()
                else:
                    relay1_off()
                if fan==True:
                    relay2_on()
                else:
                    relay2_off()


                

            
        time.sleep(1.5)

main()
