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
        # Define your custom agents in agents.py and tasks.py
        agents = Agents()
        tasks = TravelTasks()

        # Custom agents retrieved dynamically
        expert_travel_agent = agents.get_agent_by_role("Expert Travel Agent")
        city_selection_expert = agents.get_agent_by_role("City Selection Expert")
        local_tour_guide = agents.get_agent_by_role("Local Tour Guide")

        # Custom tasks retrieved dynamically
        plan_itinerary = tasks.get_task_by_name(
            "Plan 7-day Itinerary",
            agent=expert_travel_agent,
            cities=self.cities,
            travel_dates=self.travel_dates,
            interests=self.interests
        )

        identify_city = tasks.get_task_by_name(
            "Identify City",
            agent=city_selection_expert,
            origin=self.origin,
            cities=self.cities,
            travel_dates=self.travel_dates,
            interests=self.interests
        )

        gather_city_info = tasks.get_task_by_name(
            "Gather City Info",
            agent=local_tour_guide,
            cities=self.cities,
            travel_dates=self.travel_dates,
            interests=self.interests
        )

        # Define your custom crew here
        crew = Crew(
            agents=[expert_travel_agent, city_selection_expert, local_tour_guide],
            tasks=[plan_itinerary, identify_city, gather_city_info],
            verbose=True,
        )

        result = crew.kickoff()
        return result
