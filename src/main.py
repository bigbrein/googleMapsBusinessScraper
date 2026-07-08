from os import getenv

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
        included_types=["restaurant", "cafe", "hotel", "bar"],
        excluded_types=["university"],
        max_result_count=max_results
    )

    try:
        response = client.search_nearby(
            request=nearby_search_request, 
            metadata=(("x-goog-fieldmask", "places.id,places.displayName,places.shortFormattedAddress,places.formattedAddress,places.nationalPhoneNumber,places.internationalPhoneNumber,places.websiteUri,places.types,places.googleMapsUri"),)
        )
        print(response)
        return response.places
    except Exception as e:
        print(f"An error occurred while searching for places;\n{e}")
        return

def filter_places_with_website(places: Places.SearchTextResponse):
    return [place for place in places if not place.website_uri]

def display_place_info(places: list): 
    return [
f"""Name: {place.display_name.text}
ID: {place.id}
Address: {place.formatted_address}
Short Address: {place.short_formatted_address}
{place.national_phone_number and f"National Phone Number: {place.national_phone_number}" or "National Phone Number: none"}
{place.international_phone_number and f"International Phone Number: {place.international_phone_number}" or "International Phone Number: none"}
Types: {', '.join(place.types)}
Google Maps URI: {place.google_maps_uri}
{place.website_uri and f"Website URI: {place.website_uri}" or "Website URI: none"}
""" for place in places]


client = Places.PlacesClient(client_options=ClientOptions(api_key=PLACES_API_KEY))

res = nearby_search_places(client, 9.0204167, 7.3974722, 1000, 20)
# res = filter_places_with_website(res.places) if res else []

print("\n".join(display_place_info(res)))
