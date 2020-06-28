# gita.io website

Gita.io is an API adhering to standards of OpenAPI v3.0, to leverage the Gita verses programmatically. The Gita.io API serves the verses in the native Devanagari script along with their transliteration and meaning.

This is a Python Flask website built leveraging the gita.io API for an easy access to the verses of the holy Hindu book of Bhagavad Gita that translates to the song of God.

## Prerequisites

Following are the prerequisites:

- Preferrably latest MS Windows/Linux/MacOS Platform
- Python >= 3.0

## Installation and setup

1.  The `requirements.txt` file specifies the required Python libraries and modules. They can be installed with the command `pip3 install -r requirements.txt`

2. Export the environment variables `SECRET_KEY`

3. Ensure the gita.io is up and running at `http://localhost:8080` or accordingly as per your setup following the instructions provided at [Setting up gita.io](/gita-api/README.md)

4. Run the flask web application with the command - `python3 api.py`. The gita.io API website will be served at `http://localhost:8000/`

5. Login/Signup and be blessed with the knowledge and realization from the verses of Gita quoted by Lord Sri Krishna himself. Bolo Radhe Radhe.