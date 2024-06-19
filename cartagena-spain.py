import requests
import json
import time
import schedule

url = "https://api.aqi.in/api/v1/getMonitorsByCity"

headers = {
    'cityname': 'Cartagena',
    'Content-Type': 'application/json'
}

# Tiempo de espera para consultar los datos del API nuevamente
delay_time = 10

# Diccionario para almacenar el último timestamp de cada ubicación
last_timestamps = {}

def check_api_updates():
    response = requests.get(url, headers=headers)

    # Verificar si la solicitud fue exitosa
    if response.status_code == 200:
        # Parseamos la respuesta JSON
        data = response.json()

        # Extraemos los datos de interés de "Locations"
        locations = data.get('Locations', [])

        for location in locations:
            location_name = location.get('locationName')
            lat = location.get('lat')
            lon = location.get('lon')
            timestamp = location.get('timeStamp')
            locationId = location.get('locationId').replace('-', '')
            updated_at = location.get('updated_at')
            timeago = location.get('timeago')
            
            #air_components = location.get('airComponents', [])
            topic_mqtt = "scraping/cali/station/{}".format(locationId)
            
            # Si la ubicación no está en last_timestamps o el timestamp ha cambiado
            if locationId not in last_timestamps or last_timestamps[locationId] != timestamp:
                last_timestamps[locationId] = timestamp                
                # Imprimir datos
                print(f"Name: {location_name}")
                print(f"Latitude: {lat}")
                print(f"Longitude: {lon}")
                print(f"LocationId: {locationId}")
                print(f"TimeStamp: {timestamp}")
                print(f"Updated At: {updated_at}")
                print(f"Timeago: {timeago}")
                print(f"TOPIC: {topic_mqtt}")
                print(f"JSON: {location}")
                print()  
        print()                   
        print(f"Executed script at: {time.strftime('%Y-%m-%d %H:%M:%S')}")
        print() 
        print() 
    else:
        print(f"Error: {response.status_code} - {response.text}")

# Programar la tarea para que se ejecute cada N minutos
schedule.every(delay_time).minutes.do(check_api_updates)

print() 
print() 
print(f"START - Running script at {time.strftime('%Y-%m-%d %H:%M:%S')}")
print() 
print() 

check_api_updates() 

print(f"LOG - This script will run every {delay_time} minute(s)")
print() 

while True:
    schedule.run_pending()
    time.sleep(1)