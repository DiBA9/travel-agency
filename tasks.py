from crewai import Task
from textwrap import dedent


# This is an example of how to define custom tasks.
# You can define as many tasks as you want.
# You can also define custom agents in agents.py
class CustomTasks:
    def __tip_section(self):
        return "If you do your BEST WORK, I'll give you a $10,000 commission!"

    def plan_itinerary(self, agent, city, travel_dates, interests):
        return Task(
            description=dedent(
                f"""
            **Task**: Develop a 7-day Travel Itinerary
	        **Description**: Expand the city guide into a full 7-day travel itinerary wit detailed 
                per-day plans, including weather forecasts, places to eat, packing suggestions, 
                and a budget breakdown. You MUST suggest actual places to visit, actual hotes to stay,
                and actual restaurants to go to. THis itinerary should cover all aspects of the trip,
                from arrival to departure, integrating the city guide information with practical travel logistics.

            **Parameters**:
            - City: {city}
            - Trip Date: {travel_date}
            - Traveler Interest: {interests}

            **Note**: {self.__tip_section()}

        """
            ),
            agent=agent,
        )

    def identify_city(self, agent, origin, cities, interests, travel_dates):
        return Task(
            description=dedent(
                f"""
            **Task**: Identify the Gest City for the Trip
	        **Description**: Analyze and select the best city for the trip based on specific
            criteria such as weather patterns, seasonal events, and travel costs. 
            This task involves comparing multiple cities, considering factors like current weather
            conditions, upcoming cultural or seasonal events, and overall travel expenses. 
            your final answer must be a detailed report on the chosen city, 
            including actual flight costs, weather forecast, and attractions. 

            **Parameters**:
            - Origin: {origin}
            - City: {city}
            - Trip Date: {travel_date}
            - Traveler Interest: {interests}

            **Note**: {self.__tip_section()}
        """
            ),
            agent=agent,
        )
