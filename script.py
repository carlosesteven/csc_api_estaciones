import requests
import json

url = "https://api.aqi.in/api/v1/getMonitorsByCity"

headers = {
    'cityname': 'Cali',
    'Content-Type': 'application/json'
}

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
        air_components = location.get('airComponents', [])
        
        print(f"Location Name: {location_name}")
        print(f"Latitude: {lat}")
        print(f"Longitude: {lon}")
        print("Air Components:")
        for component in air_components:
            sensor_name = component.get('sensorName')
            sensor_data = component.get('sensorData')
            sensor_unit = component.get('sensorUnit')
            print(f"  - {sensor_name}: {sensor_data} {sensor_unit}")
        print()  # Línea en blanco para separar las ubicaciones
else:
    print(f"Error: {response.status_code} - {response.text}")
