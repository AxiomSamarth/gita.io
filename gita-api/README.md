# gita.io
Gita.io is an API adhering to standards of OpenAPI v3.0, to leverage the Gita verses programmatically. The Gita.io API serves the verses in the native Devanagari script along with their transliteration and meaning.

## Prerequisites

Following are the prerequisites:

- Preferrably latest MS Windows/Linux/MacOS Platform
- Python >= 3.0
- MongoDB for the database

## Installation and setup

1.  The `requirements.txt` file specifies the required Python libraries and modules. They can be installed with the command `pip3 install -r requirements.txt`

2. Migrate/import the `gita.json` into your MongoDB database's collection.

3. Export the environment variables `DB_HOST`, `DB_PORT`, `SECRET_KEY`. You may need to modify the file `db.py` to authenticate to your db. The code doesn't do it.

4. Now, that everything is done. Run the gita.io API with the command - `python3 api.py`. The gita.io API will be served at `http://localhost:8080/`

## Documentation and usage

The official Swagger documentation of the gita.io API for the developers is available at [gita.io Documentation](https://app.swaggerhub.com/apis-docs/AxiomSamarth/gita.io/1.0.0)