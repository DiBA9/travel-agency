import importlib
from crewai import Agent
from textwrap import dedent
from langchain_openai import ChatOpenAI
from tools.agent_tools import retrieve_agent_by_role

def load_tool(tool_path: str):
    """Load a tool dynamically given its class and method name."""
    print(f"Processing tool path: {tool_path}")  # Debugging statement
    try:
        module_name, class_method = tool_path.rsplit('.', 1)
        class_name, method_name = class_method.split('.', 1)
        module = importlib.import_module(module_name)
        cls = getattr(module, class_name)
        return getattr(cls, method_name)
    except ValueError as e:
        raise ValueError(f"Error processing tool path '{tool_path}': {e}")
    except ImportError as e:
        raise ImportError(f"Module '{module_name}' could not be imported: {e}")
    except AttributeError as e:
        raise AttributeError(f"Class or method not found in '{tool_path}': {e}")

class Agents:
    def __init__(self):
        self.OpenAIGPT35 = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)
        self.OpenAIGPT4 = ChatOpenAI(model_name="gpt-4", temperature=0.7)

    def get_agent(self, role: str) -> Agent:
        agent_details = retrieve_agent_by_role(role)
        if not agent_details:
            raise ValueError(f"Agent role '{role}' not found in the database.")

        tools = agent_details.tools.split(',')
        print(f"Tools to load: {tools}")  # Debugging statement
        llm = ChatOpenAI(model_name=agent_details.llm_model_name, temperature=agent_details.llm_temperature)

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
    agent = agents.get_agent("Expert Travel Agent")
    print(agent)