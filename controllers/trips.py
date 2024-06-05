from services.trip import (
    retrieve_all_trip_results,
    retrieve_trip_results_by_city,
    retrieve_trip_results_sorted_by_date,
    retrieve_trip_result_by_id,
    save_trip_result
)

def get_all_trip_results():
    return retrieve_all_trip_results()

def get_trip_results_by_city(city: str):
    return retrieve_trip_results_by_city(city)

def get_trip_results_sorted_by_date(descending: bool = True):
    return retrieve_trip_results_sorted_by_date(descending)

def get_trip_result_details(id: int):
    return retrieve_trip_result_by_id(id)

def create_trip_result(origin: str, cities: str, travel_dates: str, interests: str, result: str):
    formatted_result = result.replace('. ', '.\n')  # Add newline characters after periods for better formatting
    return save_trip_result(origin, cities, travel_dates, interests, formatted_result)
