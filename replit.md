# Careers Website

## Overview
A Flask-based careers website application built with Python.

## Recent Changes (October 30, 2025)
- Configured Flask app to run on Replit environment
- Changed port from 5001 to 5000 for web preview
- Set host to 0.0.0.0 to allow proxy access
- Added Flask dependency to pyproject.toml
- Configured workflow for automatic startup

## Project Structure
- `app.py` - Main Flask application with routes
- `main.py` - Standalone Python script (unused)
- `pyproject.toml` - Python project configuration and dependencies

## Running the App
The app automatically runs when you click the Run button. It starts a Flask development server on port 5000.

## Routes
- `/home` - Returns "Hello, World!" message

## Dependencies
- Flask 3.1.2
- Python 3.11

## Development Notes
- Flask debug mode is enabled for development
- Server binds to 0.0.0.0:5000 for Replit preview compatibility
