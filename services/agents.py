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

def create_agent_record(role: str, goal: str, backstory: str, llm: str, tools: str, function_calling_llm: str, 
        max_iter: int, max_rpm: int, max_execution_time: int, verbose: bool, allow_delegation: bool, 
        step_callback: str, cache: bool, created_at: str, updated_at: str
    ) -> AgentDetails:
    db: Session = SessionLocal()
    try:
        agent_details = AgentDetails(
            role=role,
            goal=goal,
            backstory=backstory,
            llm=llm,
            tools=tools,
            function_calling_llm=function_calling_llm,
            max_iter=max_iter,
            max_rpm=max_rpm,
            max_execution_time=max_execution_time,
            verbose=verbose,
            allow_delegation=allow_delegation,
            step_callback=step_callback,
            cache=cache,
            created_at=created_at,
            updated_at=updated_at
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

def update_agent_record(agent_id: int, agent_data: dict) -> AgentDetails:
    db: Session = SessionLocal()
    try:
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