from database.models import TaskDetails, SessionLocal, init_db
import datetime

def init_task_details():
    db = SessionLocal()
    task_details = [
        TaskDetails(
            name='plan_itinerary',
            description="""
                **Task**: Develop a 7-day Travel Itinerary
                **Description**: Expand the city guide into a full 7-day travel itinerary with detailed 
                per-day plans, including weather forecasts, places to eat, packing suggestions, 
                and a budget breakdown. You MUST suggest actual places to visit, actual hotels to stay,
                and actual restaurants to go to. This itinerary should cover all aspects of the trip,
                from arrival to departure, integrating the city guide information with practical travel logistics.

                **Parameters**:
                - Cities: {cities}
                - Trip Dates: {travel_dates}
                - Traveler Interests: {interests}

                **Note**: {tip_section}
            """,
            agent='TravelAgent',
            expected_output='A detailed 7-day travel itinerary',
            tools='SearchTools.search_internet,CalculatorTools.calculate',
            async_execution=False,
            context='',
            config=None,
            output_json=False,
            output_pydantic=False,
            output_file='',
            callback='',
            human_input=False,
            created_at=str(datetime.datetime.now()),
        ),
        TaskDetails(
            name='identify_city',
            description="""
                **Task**: Identify the Best City for the Trip
                **Description**: Analyze and select the best city for the trip based on specific
                criteria such as weather patterns, seasonal events, and travel costs. 
                This task involves comparing multiple cities, considering factors like current weather
                conditions, upcoming cultural or seasonal events, and overall travel expenses. 
                your final answer must be a detailed report on the chosen city, 
                including actual flight costs, weather forecast, and attractions. 

                **Parameters**:
                - Origin: {origin}
                - Cities: {cities}
                - Trip Dates: {travel_dates}
                - Traveler Interests: {interests}

                **Note**: {tip_section}
            """,
            agent='CitySelectionExpert',
            expected_output='A detailed report on the best city for the trip',
            tools='SearchTools.search_internet',
            async_execution=False,
            context='',
            config=None,
            output_json=False,
            output_pydantic=False,
            output_file='',
            callback='',
            human_input=False,
            created_at=str(datetime.datetime.now()),
        ),
        TaskDetails(
            name='gather_city_info',
            description="""
                **Task**: Gather In-depth City Guide Information
                **Description**: Compile an in-depth guide for the selected city, gathering information about
                key attractions, local customs, special events, and daily activity recommendations.
                This guide should provide a thorough overview of what the city has to offer, including
                hidden gems, cultural hotspots, must-visit landmarks, weather forecasts, and high-level cost 

                **Parameters**:
                - Cities: {cities}
                - Trip Dates: {travel_dates}
                - Traveler Interests: {interests}

                **Note**: {tip_section}
            """,
            agent='LocalTourGuide',
            expected_output='A comprehensive city guide',
            tools='SearchTools.search_internet',
            async_execution=False,
            context='',
            config=None,
            output_json=False,
            output_pydantic=False,
            output_file='',
            callback='',
            human_input=False,
            created_at=str(datetime.datetime.now()),
        ),
    ]

    db.bulk_save_objects(task_details)
    db.commit()
    db.close()

if __name__ == "__main__":
    init_db()  # Ensure this initializes the database if not already done
    init_task_details()
