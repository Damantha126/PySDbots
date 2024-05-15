#Copyright © 2024 Damantha Jasinghe
#For the repository at https://github.com/Damantha126/PySDbots

import sys
import requests
from datetime import date
from .__version__ import __version__

# HTTP request headers
headers = {
    'Content-Type': 'application/json',
    'User-Agent': 'pysdbots'
}

# URL for fetching configurations
CONFIGS="https://gist.githubusercontent.com/Damantha126/b18e14d0d04f25327773e0ab54cc090a/raw/config.json"
# Fetch configurations from the URL
req = requests.get(CONFIGS).json()

# Main class for interacting with SD API
class SDAPI:
    notice_displayed = False
    """Main class for interacting with SD API."""
    def __init__(self) -> None:
        # Initialize notice_displayed flag
        self.notice_displayed = False
        # Base URL and version information
        self.BASE = req["BASE_URL"]
        self.VERSION = __version__
        self.client = requests
        self.api_error = "Failed to retrieve data from the SD API. Please ensure that the API is operational and that your request parameters are correct. If the issue persists, contact support for assistance."


        # Display notice only once
        if not self.notice_displayed:
            self._start()
    
    def _start(self):
        """Display version information and update notice.

        Prints information about the current version of PySDBots and displays a notification if a newer version is available.

        This method checks the latest available version of PySDBots by querying a remote configuration source.
        """
        # Set notice_displayed flag to True
        self.notice_displayed = True
        year = date.today().year
        # Print version information
        print(
            f'PySDBots v{__version__}, Copyright (C) '
            f'2022-{year} Damantha Jasinghe <https://github.com/Damantha126>\n'
            'Licensed under the terms of the MIT License, '
            'Massachusetts Institute of Technology (MIT)\n',
        )
        # Check for newer version and print update notice
        if req["LAST_VERSION"] != __version__:
            text = f'Update Available!\n' \
                    f'New PySDBots v{req["LAST_VERSION"]} ' \
                    f'is now available!\n'
            if not sys.platform.startswith('win'):
                    print(f'\033[93m{text}\033[0m')
            else:
                print(text)

    def version(self):
        return(self.VERSION)

    def _fetch_data(self, method, url, data=None):
        """
        Make a request with the specified method.

        Args:
            method (str): The HTTP method ('GET' or 'POST').
            url (str): The URL to send the request to.
            data (dict, optional): The JSON data to send in the request body (for 'POST' requests).

        Returns:
            dict: The JSON response from the API.

        Raises:
            requests.exceptions.RequestException: If the request encounters an error (e.g., network issues, server errors).
        """
        try:
            if method == "GET":
                # Send a GET request with the specified URL and headers
                response = self.client.get(url, headers=headers)
            elif method == "POST":
                # Send a POST request with the specified URL, headers, and JSON data
                response = self.client.post(url=url, headers=headers, json=data)

            # Check for errors in the response (e.g., 4xx or 5xx status codes)
            response.raise_for_status()
            # Parse the JSON response and return it
            return response.json()
        
        except requests.exceptions.RequestException as e:
            # Re-raise the request exception if an error occurs
            print(f"Error occurred: {e}\n", self.api_error)
            return None
        
    def anime_logo(self, name):
        """Generate images with anime characters.

        Args:
            name (str): The name to include in the generated image.

        Returns:
            str: URL of the generated image hosted on telegra.ph.
        
        This method generates an image with anime characters based on the provided name and returns the URL of the generated image hosted on telegra.ph.
        """
        try:
            return self._fetch_data("GET", f"{self.BASE}/anime-logo?name={name}")
        except:
            raise Exception(self.api_error)
    
    def tiktok(self, url):
        """Get TikTok video information from a URL.

        Args:
            url (str): The URL of the TikTok video.

        Returns:
            dict: JSON object containing information about the TikTok video.
        
        This method retrieves information about a TikTok video from the provided URL and returns it as a JSON object.
        """
        try:
            return self._fetch_data("GET", f"{self.BASE}/tiktok?url={url}")
        except:
            raise Exception(self.api_error)

    def apod(self):
        """Retrieve Astronomy Picture of the Day (APOD) from NASA.

        Returns:
            dict: JSON object with information about the APOD, including date, explanation, image URL, and title.
        """            
        try:
            return self._fetch_data("GET", f"{self.BASE}/apod")
        except:
            raise Exception(self.api_error)

    def detect_lang(self, text):
        """Detect the language of a given text.

        Args:
            text (str): The text to analyze for language detection.

        Returns:
            dict: JSON object with the detected language.
        """
        try:
            return self._fetch_data("GET", f"{self.BASE}/detect?text={text}")
        except:
            raise Exception(self.api_error)

    def write(self, text):
        """Generate a note from the provided text.

        Args:
            text (str): The text content of the note.

        Returns:
            str: URL of the generated note.
        """
        try:
            body = {"text": f"{text}"}
            return self._fetch_data("POST", f"{self.BASE}/write", data=body)            
        except:
            raise Exception(self.api_error)
        
    def chk(self, cc):
        """Check information related to a given credit card.

        Args:
            cc (str): The credit card to check.

        Returns:
            dict: JSON object with information related to the credit card.
        """        
        try:
            return self._fetch_data("GET", f"{self.BASE}/chk?cc={cc}")
        except:
            raise Exception(self.api_error) 

    def sk_checker(self, key):
        """Check information related to a Stripe API Keys.

        Args:
            key (str): The sk key to check.

        Returns:
            dict: JSON object with information related to the Stripe API Keys.
        """        
        try:
            return self._fetch_data("GET", f"{self.BASE}/sk?key={key}")
        except:
            raise Exception(self.api_error) 

    def lyrics(self, song):
        """Retrieve lyrics for a given song.

        Args:
            song (str): The name of the song.

        Returns:
            dict: JSON object with the lyrics of the song.
        """        
        try:
            return self._fetch_data("GET", f"{self.BASE}/lyrics?song={song}")
        except:
            raise Exception(self.api_error) 

    def ipinfo(self, ip):
        """Retrieve information about a given IP address.

        Args:
            ip (str): The IP address to retrieve information for.

        Returns:
            dict: JSON object with information about the IP address.
        """        
        try:        
            return self._fetch_data("GET", f"{self.BASE}/ipinfo?ip={ip}")
        except:
            raise Exception(self.api_error) 

    def hirunews(self):
        """Retrieve news from Hiru News.

        Returns:
            dict: JSON object with news information.
        """        
        try:
            return self._fetch_data("GET", f"{self.BASE}/hirunews")
        except:
            raise Exception(self.api_error) 

    def logohq(self, text):
        """Generate a high-quality logo from the provided text.

        Args:
            text (str): The text content of the logo.

        Returns:
            str: URL of the generated logo.
        """        
        try:
            return self._fetch_data("GET", f"{self.BASE}/logohq?text={text}")
        except:
            raise Exception(self.api_error) 

    def fakeinfo(self):
        """Retrieve fake information.

        Returns:
            dict: JSON object with fake information.
        """        
        try:
            return self._fetch_data("GET", f"{self.BASE}/fakeinfo")    
        except:
            raise Exception(self.api_error) 
    
