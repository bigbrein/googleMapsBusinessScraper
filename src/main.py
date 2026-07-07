import asyncio

from os import getenv
from asyncio import run

from google.maps import places_v1 as Places
from google.type import latlng_pb2 as LatLng
from google.api_core.client_options import ClientOptions

PLACES_API_KEY: str = getenv("PLACES_API_KEY") or "INVALID_ENVIRONMENT_VARIABLE"

def search_places_by_name(client: Places.PlacesClient, query: str, max_results: int = 20) -> Places.SearchTextResponse:
    searchRequest = Places.SearchTextRequest(
        text_query=query,
        rank_preference=Places.SearchTextRequest.RankPreference.DISTANCE,
        max_result_count=max_results
    )
    print(searchRequest)

    try:
        response: Places.SearchTextResponse = client.search_text(
            request=searchRequest,
            metadata=(("x-goog-fieldmask", "places.id,places.displayName,places.formattedAddress,places.websiteUri"),)
        )
        return response
    except Exception as e:
        print(f"An error occurred while searching for places;\n{e}")
        return

def nearby_search_places(client: Places.PlacesClient, lat: float, lng: float, radius: float = 1000, max_results: int = 20):
    center_point = LatLng.LatLng(latitude=lat, longitude=lng)
    search_area = Places.Circle(center=center_point, radius=radius)

    location_restriction = Places.SearchNearbyRequest.LocationRestriction(circle=search_area)
    
    nearby_search_request = Places.SearchNearbyRequest(
        location_restriction=location_restriction,
        included_types=["restaurant", "school", "corporate_office", "university", "bar", "cafe", "hotel"]
    )

    try:
        response = client.search_nearby(
            request=nearby_search_request, 
            metadata=(("x-goog-fieldmask", "places.id,places.displayName,places.formattedAddress,places.websiteUri"),)
        )
        return response
    except Exception as e:
        print(f"An error occurred while searching for places;\n{e}")
        return

def filter_places_with_website(places: Places.SearchTextResponse):
    return [place for place in places if not place.website_uri]

if __name__ == "__main__":
    client = Places.PlacesClient(client_options=ClientOptions(api_key=PLACES_API_KEY))

    res = nearby_search_places(client, 9.0204167, 7.3974722, 1000, 200)
    res = filter_places_with_website(res.places) if res else []

    print(res or "No results found")
