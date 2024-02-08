import requests
import json

url = "https://api.linkedin.com/v2/userinfo"

headers = {
    'Authorization': 'Bearer AQWcpte2Gv4lpQX_gXQ4oAgAvswQROIzeCEeZyXcHWYBS_aah40hdCjhxEcyH5hXkkyA8hbfbTFdW2R-GkBRkUOciMM85xREAIdWc5x3vFQyhxXdDmhn1MXVF0wzSo57vldkh_MEaYqeomk6fKkVZtW8Q069-gSCGgnIqfHMn7d0MDhD_ldNvwgAgMqZ74xtWQXq1K-qe6b4B-g4G9-uEXHR-xyoybivJc6iNbyPI4DlaHAMJ-q4fLjtwe5TgGXnEIHpUaInnM1zGV2-GyrHuYX74aGUyK8WAbe9-Is-JM96dvV-8vjPBwFgxF7JvUiliMuWEJokX8BFdzFuyPQvmTi9QQLLwg',
    'X-Restli-Protocol-Version': '2.0.0'
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    user_data = response.json()
    print(json.dumps(user_data, indent=2))
else:
    print(f"Error: {response.status_code} - {response.text}")
