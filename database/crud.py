from sqlalchemy.orm import Session
from database.models import TripResult, AgentDetails, TaskDetails

#### Tasks
def create_task(db: Session, task: TaskDetails):
    db.add(task)
    db.commit()
    db.refresh(task)
    return task

def get_task_by_id(db: Session, task_id: int):
    return db.query(TaskDetails).filter(TaskDetails.id == task_id).first()

def get_task_by_name(db: Session, task_name: str):
    return db.query(TaskDetails).filter(TaskDetails.name == task_name).first()

def get_all_tasks(db: Session):
    return db.query(TaskDetails).all()

def update_task(db: Session, task_id: int, task_data: dict):
    task = db.query(TaskDetails).filter(TaskDetails.id == task_id).first()
    if task:
        for key, value in task_data.items():
            setattr(task, key, value)
        db.commit()
        db.refresh(task)
    return task

def delete_task(db: Session, task_id: int):
    task = db.query(TaskDetails).filter(TaskDetails.id == task_id).first()
    if task:
        db.delete(task)
        db.commit()
    return task

#### Trip

def get_latest_trip_result(db: Session):
    return db.query(TripResult).order_by(TripResult.id.desc()).first()

def create_trip_result(db: Session, origin: str, cities: str, travel_dates: str, interests: str, result: str):
    db_trip_result = TripResult(
        origin=origin,
        cities=cities,
        travel_dates=travel_dates,
        interests=interests,
        result=result
    )
    db.add(db_trip_result)
    db.commit()
    db.refresh(db_trip_result)
    return db_trip_result

#### Agent

def get_agent_by_role(db: Session, role: str) -> AgentDetails:
    return db.query(AgentDetails).filter(AgentDetails.role == role).first()

def create_agent(db: Session, agent: AgentDetails) -> AgentDetails:
    db.add(agent)
    db.commit()
    db.refresh(agent)
    return agent

def update_agent(db: Session, role: str, backstory: str, goal: str, tools: str, llm_model_name: str, llm_temperature: float) -> AgentDetails:
    agent = db.query(AgentDetails).filter(AgentDetails.role == role).first()
    if agent:
        agent.backstory = backstory
        agent.goal = goal
        agent.tools = tools
        agent.llm_model_name = llm_model_name
        agent.llm_temperature = llm_temperature
        db.commit()
        db.refresh(agent)
    return agent

def delete_agent(db: Session, role: str) -> None:
    agent = db.query(AgentDetails).filter(AgentDetails.role == role).first()
    if agent:
        db.delete(agent)
        db.commit()

def get_all_agents(db: Session):
    return db.query(AgentDetails).all()