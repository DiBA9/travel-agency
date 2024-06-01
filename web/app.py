import sys
import os

# Add the project root directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask, render_template, request, redirect, url_for, flash
from services.agent import create_agent_record, retrieve_agent_by_role, update_agent_record, delete_agent_record, retrieve_all_agents
from database.models import init_db

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a secure key

# Initialize the database
init_db()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/agents', methods=['GET'])
def agents():
    agents = retrieve_all_agents()
    return render_template('agent_list.html', agents=agents)

@app.route('/agent/create', methods=['GET', 'POST'])
def create_agent():
    if request.method == 'POST':
        role = request.form['role']
        backstory = request.form['backstory']
        goal = request.form['goal']
        tools = request.form['tools']
        llm_model_name = request.form['llm_model_name']
        llm_temperature = int(request.form['llm_temperature'])

        create_agent_record(role, backstory, goal, tools, llm_model_name, llm_temperature)
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
        backstory = request.form['backstory']
        goal = request.form['goal']
        tools = request.form['tools']
        llm_model_name = request.form['llm_model_name']
        llm_temperature = int(request.form['llm_temperature'])

        update_agent_record(role, backstory, goal, tools, llm_model_name, llm_temperature)
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

if __name__ == '__main__':
    app.run(debug=True)