# get papere information by doi through crossref api
import requests
import pandas as pd
import time
import random
import json
import os



CROSSREF_API_URL = "https://api.crossref.org/works/"
def get_paper_info_by_doi(doi):
    headers = {
        "User-Agent": f"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36"
    }
    url = CROSSREF_API_URL + doi
    for attempt in range(5):
        try:
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                data = response.json()
                if 'message' in data:
                    return data['message']
                else:
                    print(f"No 'message' field in response for DOI: {doi}")
                    return None
            else:
                print(f"Failed to fetch data for DOI: {doi}, Status Code: {response.status_code}")
        except Exception as e:
            print(f"Error fetching data for DOI: {doi}, Error: {e}")
        time.sleep(5)
    return None

doi = "10.1109/ICACCTech61146.2023.00016"

paper_info = get_paper_info_by_doi(doi)
print(json.dumps(paper_info, indent=2))