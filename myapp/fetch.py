import requests
import fire

def get_status():
    res = requests.get('https://app.secclearance.com/clearance/api/halls/')
    return res.json()

if __name__ == "__main__":
    fire.Fire(get_status)