from typing import List
from sqlalchemy.orm import Session
from database.models import SessionLocal, AgentDetails
from database.crud import (
    create_agent,
    read_agent_by_id, 
    read_agent_by_role,
    read_all_agents,
    update_agent,
    delete_agent
)

def create_agent_record(role: str, backstory: str, goal: str, tools: str, llm_model_name: str, llm_temperature: float) -> AgentDetails:
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
        return create_agent(db, agent_details)
    finally:
        db.close()

def retrieve_agent_by_id(agent_id: int) -> AgentDetails:
    db: Session = SessionLocal()
    try:
        return read_agent_by_id(db, agent_id)
    finally:
        db.close()

def retrieve_agent_by_role(role: str) -> AgentDetails:
    db: Session = SessionLocal()
    try:
        return read_agent_by_role(db, role)
    finally:
        db.close()

def retrieve_all_agents() -> List[AgentDetails]:
    db: Session = SessionLocal()
    try:
        return read_all_agents(db)
    finally:
        db.close()

def update_agent_record(agent_id: int, role: str, backstory: str, goal: str, tools: str, llm_model_name: str, llm_temperature: float) -> AgentDetails:
    db: Session = SessionLocal()
    try:
        agent_data = {
            "backstory": backstory,
            "goal": goal,
            "tools": tools,
            "llm_model_name": llm_model_name,
            "llm_temperature": llm_temperature
        }
        return update_agent(db, agent_id, agent_data)
    finally:
        db.close()

def update_agent_tools(agent_id: int, tools: str) -> AgentDetails:
    db: Session = SessionLocal()
    try:
        agent = read_agent_by_id(db, agent_id)
        if agent:
            agent.tools = tools
            db.commit()
            db.refresh(agent)
        return agent
    finally:
        db.close()

def delete_agent_record(agent_id: int) -> None:
    db: Session = SessionLocal()
    try:
        delete_agent(db, agent_id)
    finally:
        db.close()