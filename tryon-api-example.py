import json
import base64
import requests
from pprint import pprint
import time
from dotenv import dotenv_values
import os

CURRENT_URL = 'https://app.alphabake.io/'
url = CURRENT_URL + 'api/tryon/'
fetch_url = CURRENT_URL + 'api/tryon_state/'

API_KEY = dotenv_values('.env')['API_KEY'] #add a .env file in the same directory as this file and add the API_KEY as an environment variable

def download_image(url, download_path):
    response = requests.get(url)
    if response.status_code == 200:
        with open(download_path, 'wb') as file:
            file.write(response.content)
        print(f"Image downloaded to {download_path}")
        return True
    else:
        print(f"Failed to download image from {url}")
        return None

# Define headers with authorization token
headers = {
    'Authorization': 'Bearer ' + API_KEY,
    'Content-Type': 'application/json',
}

human_image_path = 'inputs/human.jpg'
garment_image_path = 'inputs/garment.jpg'
output_tryon_path = 'outputs/tryon.png'

if os.path.exists(output_tryon_path):
    os.remove(output_tryon_path)

output_dir = os.path.dirname(output_tryon_path)
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

human_image_data = open(human_image_path, 'rb').read()
garment_image_data = open(garment_image_path, 'rb').read()

human_base64_image = base64.b64encode(human_image_data).decode('utf-8')
garment_base64_image = base64.b64encode(garment_image_data).decode('utf-8')

data = {
    'human_image_base64': human_base64_image,  
    'garment_image_base64': garment_base64_image,
    'garment_name': 'garment-123456',
    'tryon_name': 'tryon-123456',
    'mode': 'balanced'  # Optional: 'fast', 'balanced', or 'quality'. Default is 'balanced'
}

response = requests.post(url, headers=headers, data=json.dumps(data))

if response.status_code == 200:
    json_response = response.json()
    pprint(json_response)
    tryon_pk = json_response['tryon_pk']
    found = False
    time_elapsed = 0
    while not found:
        response = requests.post(fetch_url, headers=headers, data=json.dumps({
            'tryon_pk': tryon_pk,
        }))
        if response.status_code == 200:
            json_response = response.json()
            if json_response['message'] != 'success':
                found = True
            else:
                if json_response['status'] == 'done':
                    print(json_response['s3_url'])
                    download_image(json_response['s3_url'], output_tryon_path)
                    found = True
                else:
                    time.sleep(2)
                    time_elapsed += 2
                    print(f"Time elapsed: {time_elapsed} seconds")
            if time_elapsed > 60:
                found = True
                print("Tryon not found after 60 seconds")
        else:
            found = True
            print(f"Failed to get tryon. Status code: {response.status_code}")
else:
    print(f"Failed to create tryon. Status code: {response.status_code}")
    print(f"Response: {response.text}")