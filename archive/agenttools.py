from sqlalchemy.orm import Session
from models import AgentDetails, SessionLocal
from crud import create_agent, get_agent_by_role, update_agent, delete_agent

def create_agent_record(role: str, backstory: str, goal: str, tools: str, llm_model_name: str, llm_temperature: int) -> AgentDetails:
    db: Session = SessionLocal()

    agent_details = AgentDetails(
        role=role,
        backstory=backstory,
        goal=goal,
        tools=tools,
        llm_model_name=llm_model_name,
        llm_temperature=llm_temperature
    )

    created_agent = create_agent(db, agent_details)
    db.close()
    return created_agent

def retrieve_agent_by_role(role: str) -> AgentDetails:
    db: Session = SessionLocal()
    retrieved_agent = get_agent_by_role(db, role)
    db.close()
    return retrieved_agent

def update_agent_record(role: str, backstory: str, goal: str, tools: str, llm_model_name: str, llm_temperature: float) -> AgentDetails:
    db: Session = SessionLocal()
    updated_agent = update_agent(db, role, backstory, goal, tools, llm_model_name, llm_temperature)
    db.close()
    return updated_agent

def update_agent_tools(role: str, tools: str) -> AgentDetails:
    db: Session = SessionLocal()
    agent = get_agent_by_role(db, role)
    if agent:
        agent.tools = tools
        db.commit()
        db.refresh(agent)
    db.close()
    return agent

def delete_agent_record(role: str) -> None:
    db: Session = SessionLocal()
    delete_agent(db, role)
    db.close()

# Example usage:
if __name__ == "__main__":
    created_agent = create_agent_record(
        role="Expert Travel Agent",
        backstory="""
            I am an expert in travel planning and logistics.
            I have decades of experience making travel itineraries.
        """,
        goal="""
            Create a 7-day travel itinerary with detailed per-day plans,
            including budget, packing suggestions, and safety tips.
        """,
        tools="search_internet,calculate",
        llm_model_name="gpt-3.5-turbo",
        llm_temperature=0.7
    )

    retrieved_agent = retrieve_agent_by_role("Expert Travel Agent")

    print("Created Agent:")
    print(f"Role: {created_agent.role}")
    print(f"Backstory: {created_agent.backstory}")
    print(f"Goal: {created_agent.goal}")
    print(f"Tools: {created_agent.tools}")
    print(f"LLM Model Name: {created_agent.llm_model_name}")
    print(f"LLM Temperature: {created_agent.llm_temperature}")

    print("\nRetrieved Agent:")
    print(f"Role: {retrieved_agent.role}")
    print(f"Backstory: {retrieved_agent.backstory}")
    print(f"Goal: {retrieved_agent.goal}")
    print(f"Tools: {retrieved_agent.tools}")
    print(f"LLM Model Name: {retrieved_agent.llm_model_name}")
    print(f"LLM Temperature: {retrieved_agent.llm_temperature}")