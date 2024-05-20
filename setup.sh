#!/bin/sh

pip install -r requirements.txt
pip install crewai==0.28.8
composio-cli update
composio-cli login
composio-cli add googlecalendar