import os
import requests
from dotenv import load_dotenv

load_dotenv()


def scrape_linkedin_profile(linkedin_profile_url: str, mock: bool = False):
    """Scrape information from LinkedIn,
    Manually scrap the information from the LinkdIn profile.
    """
    """
    :param linkedin_profile_url: Taking input parameter as string which will be linkedin profile 
    :param mock: Deafult is False to save the call the api call scrapin.io
    :return: 
    """
    if mock:
        linkedin_profile_url = "https://gist.githubusercontent.com/viplavdube/cd085f915b332a072690505aab86f5d9/raw/75b063a2b861e33720e97bde3c44671b1acc964c/viplav-dube-scrapping.json"
        response = requests.get(
            linkedin_profile_url,
            timeout=10,
        )
    else:
        url = "https://api.scrapin.io/v1/enrichment/profile"
        params = {
            "apikey": os.environ["SCRAPIN_API_KEY"],
        }
        payload = {"linkedInUrl": linkedin_profile_url, "includes": {}}
        headers = {"Content-Type": "application/json"}
        response = requests.post(url, json=payload, headers=headers, params=params)

    data = response.json().get("person")
    return data


if __name__ == "__main__":
    scrape_linkedin_profile(
        linkedin_profile_url="https://www.linkedin.com/in/viplav-dube-116043ba/",
        mock=False,
    )
