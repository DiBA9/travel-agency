from crewai import Crew
from controllers.agents import Agents
from controllers.tasks import TravelTasks

class TripCrew:
    def __init__(self, origin, cities, travel_dates, interests):
        self.origin = origin
        self.cities = cities
        self.travel_dates = travel_dates
        self.interests = interests

    def run(self):
        # Define your custom agents and tasks in agents.py and tasks.py
        agents = Agents()
        tasks = TravelTasks()

        # Define your custom agents and tasks here
        expert_travel_agent = agents.get_agent("Expert Travel Agent")
        city_selection_expert = agents.get_agent("City Selection Expert")
        local_tour_guide = agents.get_agent("Local Tour Guide")

        # Custom tasks include agent name and variables as input
        plan_itinerary = tasks.plan_itinerary(
            expert_travel_agent,
            self.cities,
            self.travel_dates,
            self.interests
        )

        identify_city = tasks.identify_city(
            city_selection_expert,
            self.origin,
            self.cities,
            self.travel_dates,
            self.interests
        )

        gather_city_info = tasks.gather_city_info(
            local_tour_guide,
            self.cities,
            self.travel_dates,
            self.interests
        )

        # Define your custom crew here
        crew = Crew(
            agents=[expert_travel_agent, city_selection_expert, local_tour_guide],
            tasks=[plan_itinerary, identify_city, gather_city_info],
            verbose=True,
        )

        result = crew.kickoff()
        return result