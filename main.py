from time import sleep
import urequests

x = 7

def connect():
    import network
 
    ssid = "GalaxyNoteS23" 
    password = "809655fr" 
 
    station = network.WLAN(network.STA_IF)
 
    if station.isconnected() == True:
        print("Already connected")
        return
 
    station.active(True)
    station.connect(ssid, password)
 
    while station.isconnected() == False:
        pass
 
    print("Connection successful")
    print(station.ifconfig())
    
connect()

while True:
    sleep(5)
    print(x)
    
    h = {'content-type' : 'application/x-www-form-urlencoded'}
    form_url = 'https://docs.google.com/forms/d/e/1FAIpQLScKkhyfqhDLriXd5GbB-7ig9-FEZPkwZoW0HfE7l6qnJ0O1cg/formResponse?usp=pp_url'
    form_data = 'entry.1481624375=' + str(x)
    r = urequests.post(form_url, data=form_data, headers=h)
    r.status_code
    r.close()
    print("check google form")
    
    
    
#https://docs.google.com/forms/d/e/1FAIpQLSfTfxMNKdGAepcyGISCoz6ynsDEdTJy9JiGha_HL5ypHgSg-g/formResponse?usp=pp_url&entry.1234193767={}&submit=Submit

