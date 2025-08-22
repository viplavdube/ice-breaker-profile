import os
import requests
from dotenv import load_dotenv

load_dotenv()


def scrape_linkedin_profile(linkedin_profile_url: str, mock: bool = False):
    """Scrap information from LinkedIn profile,
    Manually scrap the information from the LinkedIn profile"""
