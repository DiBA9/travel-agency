from crewai import Agent
from textwrap import dedent
from langchain_openai import ChatOpenAI

from tools.search_tools import SearchTools
from tools.calculator_tools import CalculatorTools

class TravelAgents:
    def __init__(self):
        self.OpenAIGPT35 = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)
        self.OpenAIGPT4 = ChatOpenAI(model_name="gpt-4", temperature=0.7)
        self.Ollama = Ollama(model="openhermes")

    def expert_travel_agent(self):
        return Agent(
            role="Expert Travel Agent",
            backstory=dedent(f"""
                            I am an expert in travel planning and logistics.
                            I have decades of experience making travel iteneraries.
                            """),
            goal=dedent(f"""
                        Create a 7-day travel itinerary with detailed per-day plans,
                        including budget, packing suggestions, and safety tips.
                        """),
            tools=[
                SearchTools.search_internet,
                CalculatorTools.calculate
            ],
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT35,
        )

    def city_selection_expert(self):
        return Agent(
            role="City Selection Expert",
            backstory=dedent(f"""
                            I am an expert at analyzing travel data to pick ideal destinations.
                            """),
            goal=dedent(f"""
                        Select the best cities based on weather, season, prices, and traveler interests.
                        """),
            tools=[SearchTools.search_internet],
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT35,
        )

    def local_tour_guide(self):
        return Agent(
            role="Local Tour Guide",
            backstory=dedent(f"""
                            I am a knowledgeable local guide with extensive information about the city, it's attractions and customs.
                            """),
            goal=dedent(f"""
                        Provide the best insights about a selected city.
                        """),
            tools=[SearchTools.search_internet],
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT35,
        )
