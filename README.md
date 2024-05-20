# Todo to Calendar Converter

This Python script allows you to easily convert roughly written todo items into Google Calendar events. It leverages the power of Composio, an open-source command-line tool for developers, to automate the process of creating calendar events based on your todo descriptions.

## Prerequisites

Before you begin, ensure that you have the following installed:

- Python 3.12 or later
- Git

## Installation

1. **Clone the repository:**
    ```
    git clone https://github.com/anonthedev/composio-todo-to-calendar.git
    ```
2. **Create a virtual env**

	We've used python 3.12

	``` 
    python3 -m venv env
    ```
	```
    source env/bin/activate
    ```

3. **Install required dependencies**
	 
	```
	pip install -r requirements.txt
	```
4. **Adding API keys**

	Create a ```.env``` file and add the API keys there.
    
    Composio API key can be found here - https://app.composio.dev/settings
	```
    OPENAI_API_KEY=sk-
    COMPOSIO_API_KEY=
    ```

## Authenticate
1. **Authenticate composio:**
	```
    composio-cli login
    ```
2. **Authenticate Google:**
	
    Authenticate with the account in which events will be created
	```
    composio-cli add googlecalendar
    ```

## Usage

1. **Edit your todos:**

    Open the `main.py` file and edit the `todos` list with your desired todo items in the format `start_time - end_time -> description`. For example:

	```python
	todos = '''
	    9AM - 11AM -> Work on project X,
	    1PM - 3PM -> Gaming,
	    # Add more todos here
	'''
	```
2. **Run the file:**
	```
	python main.py
	```
