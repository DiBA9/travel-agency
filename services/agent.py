from sqlalchemy.orm import Session
from database.models import AgentDetails, SessionLocal
from database.crud import create_agent, get_agent_by_role, update_agent, delete_agent, get_all_agents

def create_agent_record(role: str, backstory: str, goal: str, tools: str, llm_model_name: str, llm_temperature: int) -> AgentDetails:
    db: Session = SessionLocal()
    try:
        agent_details = AgentDetails(
            role=role,
            backstory=backstory,
            goal=goal,
            tools=tools,
            llm_model_name=llm_model_name,
            llm_temperature=llm_temperature
        )
        created_agent = create_agent(db, agent_details)
        return created_agent
    finally:
        db.close()

def retrieve_agent_by_role(role: str) -> AgentDetails:
    db: Session = SessionLocal()
    try:
        retrieved_agent = get_agent_by_role(db, role)
        return retrieved_agent
    finally:
        db.close()

def update_agent_record(role: str, backstory: str, goal: str, tools: str, llm_model_name: str, llm_temperature: float) -> AgentDetails:
    db: Session = SessionLocal()
    try:
        updated_agent = update_agent(db, role, backstory, goal, tools, llm_model_name, llm_temperature)
        return updated_agent
    finally:
        db.close()

def update_agent_tools(role: str, tools: str) -> AgentDetails:
    db: Session = SessionLocal()
    try:
        agent = get_agent_by_role(db, role)
        if agent:
            agent.tools = tools
            db.commit()
            db.refresh(agent)
        return agent
    finally:
        db.close()

def delete_agent_record(role: str) -> None:
    db: Session = SessionLocal()
    try:
        delete_agent(db, role)
    finally:
        db.close()

def retrieve_all_agents() -> list[AgentDetails]:
    db: Session = SessionLocal()
    try:
        all_agents = get_all_agents(db)
        return all_agents
    finally:
        db.close()