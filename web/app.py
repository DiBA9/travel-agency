import sys
import os

# Add the project root directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask, render_template, request, redirect, url_for, flash
from services.agent import create_agent_record, retrieve_agent_by_role, update_agent_record, delete_agent_record, retrieve_all_agents
from services.task import create_task_record, retrieve_task_by_id, retrieve_all_tasks, update_task_record, delete_task_record
from database.models import init_db

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a secure key

# Initialize the database
init_db()

@app.route('/')
def index():
    return render_template('index.html')

#### Task Management Routes
@app.route('/tasks')
def tasks():
    tasks = retrieve_all_tasks()
    return render_template('task_list.html', tasks=tasks)

@app.route('/task/<int:id>', methods=['GET'])
def task_details(id):
    task = retrieve_task_by_id(id)
    if not task:
        flash(f'Task with ID {id} not found', 'error')
        return redirect(url_for('tasks'))
    return render_template('task_details.html', task=task)

@app.route('/task/create', methods=['GET', 'POST'])
def create_task():
    if request.method == 'POST':
        task_data = {
            'name': request.form['name'],
            'description': request.form['description'],
            'agent': request.form['agent'],
            'expected_output': request.form['expected_output'],
            'tools': request.form['tools'],
            'async_execution': 'async_execution' in request.form,
            'context': request.form['context'],
            'config': request.form['config'],
            'output_json': 'output_json' in request.form,
            'output_pydantic': 'output_pydantic' in request.form,
            'output_file': request.form['output_file'],
            'callback': request.form['callback'],
            'human_input': 'human_input' in request.form
        }
        create_task_record(**task_data)
        flash('Task created successfully!', 'success')
        return redirect(url_for('tasks'))

    return render_template('task_create.html')

@app.route('/task/update/<int:id>', methods=['GET', 'POST'])
def update_task(id):
    task = retrieve_task_by_id(id)
    if request.method == 'POST':
        task_data = {
            'name': request.form['name'],
            'description': request.form['description'],
            'agent': request.form['agent'],
            'expected_output': request.form['expected_output'],
            'tools': request.form['tools'],
            'async_execution': 'async_execution' in request.form,
            'context': request.form['context'],
            'config': request.form['config'],
            'output_json': 'output_json' in request.form,
            'output_pydantic': 'output_pydantic' in request.form,
            'output_file': request.form['output_file'],
            'callback': request.form['callback'],
            'human_input': 'human_input' in request.form
        }
        update_task_record(id, task_data)
        flash('Task updated successfully!', 'success')
        return redirect(url_for('tasks'))

    return render_template('task_update.html', task=task)

@app.route('/task/delete/<int:id>', methods=['POST'])
def delete_task(id):
    delete_task_record(id)
    flash('Task deleted successfully!', 'success')
    return redirect(url_for('tasks'))

#### Agent Management Routes
@app.route('/agents', methods=['GET'])
def agents():
    agents = retrieve_all_agents()
    return render_template('agent_list.html', agents=agents)

@app.route('/agent/create', methods=['GET', 'POST'])
def create_agent():
    if request.method == 'POST':
        agent_data = {
            'role': request.form['role'],
            'backstory': request.form['backstory'],
            'goal': request.form['goal'],
            'tools': request.form['tools'],
            'llm_model_name': request.form['llm_model_name'],
            'llm_temperature': float(request.form['llm_temperature'])
        }
        create_agent_record(**agent_data)
        flash('Agent created successfully!', 'success')
        return redirect(url_for('agents'))

    return render_template('agent_create.html')

@app.route('/agent/update/<role>', methods=['GET', 'POST'])
def update_agent(role):
    agent = retrieve_agent_by_role(role)
    if not agent:
        flash(f'Agent with role {role} not found', 'error')
        return redirect(url_for('agents'))

    if request.method == 'POST':
        agent_data = {
            'backstory': request.form['backstory'],
            'goal': request.form['goal'],
            'tools': request.form['tools'],
            'llm_model_name': request.form['llm_model_name'],
            'llm_temperature': float(request.form['llm_temperature'])
        }
        update_agent_record(role, **agent_data)
        flash('Agent updated successfully!', 'success')
        return redirect(url_for('agents'))

    return render_template('agent_update.html', agent=agent)

@app.route('/agent/delete/<role>', methods=['POST'])
def delete_agent(role):
    delete_agent_record(role)
    flash('Agent deleted successfully!', 'success')
    return redirect(url_for('agents'))

@app.route('/agent/<role>', methods=['GET'])
def agent_details(role):
    agent = retrieve_agent_by_role(role)
    if not agent:
        flash(f'Agent with role {role} not found', 'error')
        return redirect(url_for('agents'))
    return render_template('agent_details.html', agent=agent)

@app.route('/test')
def test():
    return "Test page works!"


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
