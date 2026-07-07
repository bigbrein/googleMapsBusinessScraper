import asyncio

from os import getenv

from google.maps import places_v1 as Places
from google.api_core.client_options import ClientOptions

# from google.api_core import retry

PLACES_API_KEY: str = getenv("PLACES_API_KEY") or "INVALID_ENVIRONMENT_VARIABLE"   

if __name__ == "__main__":
    pass