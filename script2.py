import requests

# Tu token de la API
api_token = '6a16ab9d0f0cca630b6229c058f92ea393f70dda'
station_id = 'A370834'

# URL de la API
url = f'https://api.waqi.info/feed/@{station_id}/?token={api_token}'

# Realizar la solicitud GET a la API
response = requests.get(url)
data = response.json()

# Verificar si la solicitud fue exitosa
if data['status'] == 'ok':
    # Extraer los datos necesarios
    iaqi = data['data']['iaqi']
    pm10 = iaqi.get('pm10', {}).get('v', 'No data')
    pm25 = iaqi.get('pm25', {}).get('v', 'No data')
    no2 = iaqi.get('no2', {}).get('v', 'No data')
    so2 = iaqi.get('so2', {}).get('v', 'No data')
    co = iaqi.get('co', {}).get('v', 'No data')
    o3 = iaqi.get('o3', {}).get('v', 'No data')
    temperature = iaqi.get('t', {}).get('v', 'No data')

    # Imprimir los resultados
    print(f"PM10: {pm10}")
    print(f"PM2.5: {pm25}")
    print(f"NO2: {no2}")
    print(f"SO2: {so2}")
    print(f"CO: {co}")
    print(f"O3: {o3}")
    print(f"Temperatura: {temperature}°C")
else:
    print("Error al obtener los datos:", data['data'])
