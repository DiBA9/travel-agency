from typing import List
from sqlalchemy.orm import Session
from database.models import (
    AgentDetails, 
    CrewDetails, 
    TaskDetails, 
    TripResults
)

# AgentDetails CRUD operations
def create_agent(db: Session, agent_details: AgentDetails) -> AgentDetails:
    db.add(agent_details)
    db.commit()
    db.refresh(agent_details)
    return agent_details

def retrieve_agent_by_id(db: Session, agent_id: int) -> AgentDetails:
    return db.query(AgentDetails).filter(AgentDetails.id == agent_id).first()

def retrieve_agent_by_role(db: Session, role: str) -> AgentDetails:
    return db.query(AgentDetails).filter(AgentDetails.role == role).first()

def retrieve_all_agents(db: Session) -> List[AgentDetails]:
    return db.query(AgentDetails).all()

def update_agent(db: Session, agent_id: int, agent_data: dict) -> AgentDetails:
    agent_details = retrieve_agent_by_id(db, agent_id)
    if agent_details:
        for key, value in agent_data.items():
            setattr(agent_details, key, value)
        db.commit()
        db.refresh(agent_details)
    return agent_details

def delete_agent(db: Session, agent_id: int) -> None:
    agent_details = retrieve_agent_by_id(db, agent_id)
    if agent_details:
        db.delete(agent_details)
        db.commit()

# CrewDetails CRUD operations
def create_crew(db: Session, crew_details: CrewDetails) -> CrewDetails:
    db.add(crew_details)
    db.commit()
    db.refresh(crew_details)
    return crew_details

def retrieve_crew_by_id(db: Session, crew_id: int) -> CrewDetails:
    return db.query(CrewDetails).filter(CrewDetails.id == crew_id).first()

def retrieve_crew_by_name(db: Session, name: str) -> CrewDetails:
    return db.query(CrewDetails).filter(CrewDetails.name == name).first()

def retrieve_all_crews(db: Session) -> List[CrewDetails]:
    return db.query(CrewDetails).all()

def update_crew(db: Session, crew_id: int, crew_data: dict) -> CrewDetails:
    crew_details = retrieve_crew_by_id(db, crew_id)
    if crew_details:
        for key, value in crew_data.items():
            setattr(crew_details, key, value)
        db.commit()
        db.refresh(crew_details)
    return crew_details

def delete_crew(db: Session, crew_id: int) -> None:
    crew_details = retrieve_crew_by_id(db, crew_id)
    if crew_details:
        db.delete(crew_details)
        db.commit()

# TaskDetails CRUD operations
def create_task(db: Session, task_details: TaskDetails) -> TaskDetails:
    db.add(task_details)
    db.commit()
    db.refresh(task_details)
    return task_details

def retrieve_task_by_id(db: Session, task_id: int) -> TaskDetails:
    return db.query(TaskDetails).filter(TaskDetails.id == task_id).first()

def retrieve_task_by_name(db: Session, name: str) -> TaskDetails:
    return db.query(TaskDetails).filter(TaskDetails.name == name).first()

def retrieve_all_tasks(db: Session) -> List[TaskDetails]:
    return db.query(TaskDetails).all()

def update_task(db: Session, task_id: int, task_data: dict) -> TaskDetails:
    task_details = retrieve_task_by_id(db, task_id)
    if task_details:
        for key, value in task_data.items():
            setattr(task_details, key, value)
        db.commit()
        db.refresh(task_details)
    return task_details

def delete_task(db: Session, task_id: int) -> None:
    task_details = retrieve_task_by_id(db, task_id)
    if task_details:
        db.delete(task_details)
        db.commit()

# TripResults CRUD operations
def create_trip_result(db: Session, trip_result: TripResults) -> TripResults:
    db.add(trip_result)
    db.commit()
    db.refresh(trip_result)
    return trip_result

def retrieve_trip_result_by_id(db: Session, result_id: int) -> TripResults:
    return db.query(TripResults).filter(TripResults.id == result_id).first()

def retrieve_trip_result_by_origin(db: Session, origin: str) -> TripResults:
    return db.query(TripResults).filter(TripResults.origin == origin).first()

def retrieve_all_trip_results(db: Session) -> List[TripResults]:
    return db.query(TriptDetails).all()

def update_trip_result(db: Session, result_id: int, trip_result_data: dict) -> TripResults:
    trip_result = retrieve_trip_result(db, result_id)
    if trip_result:
        for key, value in trip_result_data.items():
            setattr(trip_result, key, value)
        db.commit()
        db.refresh(trip_result)
    return trip_result

def delete_trip_result(db: Session, result_id: int) -> None:
    trip_result = retrieve_trip_result(db, result_id)
    if trip_result:
        db.delete(trip_result)
        db.commit()
