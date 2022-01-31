import os

import dotenv

dotenv.load_dotenv()


class Config:
    google_api_key = os.getenv('GOOGLE_API_KEY')
    mapbox_token = os.getenv("MAPBOX_TOKEN")
