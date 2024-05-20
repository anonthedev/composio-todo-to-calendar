# Todo to Calendar Converter

This Python script allows you to easily convert roughly written todo items into Google Calendar events. It leverages the power of Composio, an open-source command-line tool for developers, to automate the process of creating calendar events based on your todo descriptions.

## Installation

1. **Clone the repository:**

   ```
   git clone https://github.com/anonthedev/composio-todo-to-calendar.git
   ```

2. **Go to the cloned repo:**

   ```
   cd composio-todo-to-calendar
   ```

3. **Adding API keys**

   Create a `.env` file and add the API keys there.

   Composio API key can be found here - https://app.composio.dev/settings

   ```
   OPENAI_API_KEY=sk-
   COMPOSIO_API_KEY=
   ```

## Setup Project

1. **Setup Virtual env**
    ```
    python3.12 -m venv env
    ```
    ```
    source env/bin/activate
    ```

1. Give execute permission to `setup.sh` file

   ```
   chmod +x ./setup.sh
   ```

2. Run the setup.sh file
   ```
   ./setup.sh
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
