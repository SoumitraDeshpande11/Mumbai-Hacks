import os   
import requests
import streamlit as st
import json

# Ollama API configuration
# API_URL = 'http://localhost:8501'
API_URL = 'http://localhost:11434/api/generate'

# Define functions


def prioritize_tasks(tasks):
    prompt = "Here are some tasks:\n" + "\n".join(
        tasks) + "\nPlease prioritize these tasks based on urgency and importance."

    headers = {
        'Content-Type': 'application/json'
        # Add authorization header if needed
    }

    try:
        response = requests.post(API_URL, json={'model': 'llama2', 'prompt': prompt}, headers=headers)
        response.raise_for_status()

        # Print the raw response text for debugging
        print("Raw response:", response.text)

        # Split the response by new lines and decode each JSON object
        responses = response.text.strip().split('\n')
        results = []
        for resp in responses:
            try:
                json_response = json.loads(resp)  # Try to parse each line as JSON
                results.append(json_response.get('response', '').strip())
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON: {e} - Response: {resp}")

        return "\n".join(results)  # Join all responses into a single string
    except requests.exceptions.HTTPError as http_err:
        return f"HTTP error occurred: {http_err} - {response.text}"
    except Exception as err:
        return f"An error occurred: {err}"



def suggest_meeting_times(availability):
    prompt = "Given the following team availability, suggest common meeting times:\n" + availability

    headers = {
        'Content-Type': 'application/json'
        # Add authorization header if needed
    }

    try:
        response = requests.post(API_URL, json={'model': 'llama2', 'prompt': prompt}, headers=headers)
        response.raise_for_status()

        # Print the raw response text for debugging
        print("Raw response:", response.text)

        # Split the response by new lines and decode each JSON object
        responses = response.text.strip().split('\n')
        results = []
        for resp in responses:
            try:
                json_response = json.loads(resp)  # Try to parse each line as JSON
                results.append(json_response.get('response', '').strip())
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON: {e} - Response: {resp}")

        return "\n".join(results)  # Join all responses into a single string
    except requests.exceptions.HTTPError as http_err:
        return f"HTTP error occurred: {http_err} - {response.text}"
    except Exception as err:
        return f"An error occurred: {err}"


def analyze_feedback(feedback):
    prompt = f"Analyze the following feedback and provide insights:\n'{feedback}'"

    headers = {
        'Content-Type': 'application/json'
        # Add authorization header if needed
    }

    try:
        response = requests.post(API_URL, json={'model': 'llama2', 'prompt': prompt}, headers=headers)
        response.raise_for_status()

        # Print the raw response text for debugging
        print("Raw response:", response.text)

        # Split the response by new lines and decode each JSON object
        responses = response.text.strip().split('\n')
        results = []
        for resp in responses:
            try:
                json_response = json.loads(resp)  # Try to parse each line as JSON
                results.append(json_response.get('response', '').strip())
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON: {e} - Response: {resp}")

        return "\n".join(results)  # Join all responses into a single string
    except requests.exceptions.HTTPError as http_err:
        return f"HTTP error occurred: {http_err} - {response.text}"
    except Exception as err:
        return f"An error occurred: {err}"



def plan_timetable(goal):
    prompt = f"Break down the goal '{goal}' into weekly and daily sub-goals with estimated durations."

    headers = {
        'Content-Type': 'application/json'

    }

    try:
        response = requests.post(API_URL, json={'model': 'llama2', 'prompt': prompt}, headers=headers)
        response.raise_for_status()


        print("Raw response:", response.text)

        # Split the response by new lines and decode each JSON object
        responses = response.text.strip().split('\n')
        results = []
        for resp in responses:
            try:
                json_response = json.loads(resp)  # Try to parse each line as JSON
                results.append(json_response.get('response', '').strip())
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON: {e} - Response: {resp}")

        return "\n".join(results)  # Join all responses into a single string
    except requests.exceptions.HTTPError as http_err:
        return f"HTTP error occurred: {http_err} - {response.text}"
    except Exception as err:
        return f"An error occurred: {err}"


# Set up the Streamlit app
st.title("Work-from-Home AI Productivity Tool")

# Task Prioritization Section
st.header("Task Prioritization")
tasks_input = st.text_area("Enter Tasks for Prioritization (one per line):")
if st.button("Prioritize Tasks"):
    if tasks_input:
        tasks = tasks_input.splitlines()
        prioritized_output = prioritize_tasks(tasks)
        st.success(f"Prioritized Tasks:\n{prioritized_output}")
    else:
        st.warning("Please enter some tasks.")

# Meeting Suggestion Section
st.header("Meeting Suggestion")
availability_input = st.text_area("Enter Team Availability for Meeting Suggestion:")
if st.button("Suggest Meeting Times"):
    if availability_input:
        meeting_suggestion = suggest_meeting_times(availability_input)
        st.success(f"Suggested Meeting Times:\n{meeting_suggestion}")
    else:
        st.warning("Please enter team availability.")

# Feedback Analysis Section
st.header("Feedback Analysis")
feedback_input = st.text_area("Enter Feedback for Analysis:")
if st.button("Analyze Feedback"):
    if feedback_input:
        feedback_analysis = analyze_feedback(feedback_input)
        st.success(f"Feedback Analysis:\n{feedback_analysis}")
    else:
        st.warning("Please enter feedback.")

# Timetable Planner Section
st.header("Timetable Planner")
goal_input = st.text_area("Enter Your Goal for Timetable Planning:")
if st.button("Plan Timetable"):
    if goal_input:
        timetable_output = plan_timetable(goal_input)
        st.success(f"Timetable Plan:\n{timetable_output}")
    else:
        st.warning("Please enter a goal.")

