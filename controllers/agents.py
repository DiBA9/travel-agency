from crewai import Agent
from textwrap import dedent
from langchain_openai import ChatOpenAI
from controllers.tools import load_tool
from services.agents import (
    create_agent_record,
    retrieve_agent_by_id,
    retrieve_agent_by_role,
    retrieve_all_agents,
    update_agent_record,
    delete_agent_record
)

class Agents:
    def __init__(self):
        self.OpenAIGPT35 = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)
        self.OpenAIGPT4 = ChatOpenAI(model_name="gpt-4", temperature=0.7)

    def get_agent_by_role(self, role: str) -> Agent:
        agent_details = retrieve_agent_by_role(role)
        if not agent_details:
            raise ValueError(f"Agent role '{role}' not found in the database.")

        tools = agent_details.tools.split(',')
        print(f"Tools to load: {tools}")  # Debugging statement

        tool_instances = []
        for tool in tools:
            tool_instances.append(load_tool(tool.strip()))

        return Agent(
            role=agent_details.role,
            backstory=dedent(agent_details.backstory),
            goal=dedent(agent_details.goal),
            tools=tool_instances,
            allow_delegation=False,
            verbose=True,
            llm=llm,
        )

# Example usage:
if __name__ == "__main__":
    agents = Agents()
    agent = agents.get_agent_by_role("Expert Travel Agent")
    print(agent)