# Chemistry Calculation Tool with SQLite Integration

This Python script serves as a chemistry calculation tool, allowing you to perform various chemical calculations and access information about chemical elements. It also integrates with an SQLite database containing chemical data.

## Prerequisites

- Python 3.x installed on your system.
- Libraries like `sqlite3`, `pandas`, and `requests` installed. You can typically install these using pip: `pip install sqlite3 pandas requests`.

## Features

### Chemical Calculations

1. **Molar Mass Calculation**: Calculate the molar mass of a given chemical compound.

2. **Mole Calculation**: Calculate the number of moles for a given chemical compound and mass.

3. **Chemical Reaction Analysis**: Analyze a chemical reaction, including balancing equations and stoichiometry.

### SQLite Database Integration

- Retrieve information about chemical elements from an SQLite database. The database includes data like atomic number, name, symbol, atomic mass, electronegativity, electron orbitals, and electron configuration.

### FastAPI Integration

- Utilizes FastAPI to create an API for performing chemical calculations and accessing chemical data.

## Usage

1. Run the script using Python: `python script.py`.
2. Choose the desired chemical calculation or SQLite database operation.
3. Follow the prompts to input relevant data.

## Database Integration

- The script connects to an SQLite database named `mendeleev.db`, which should be present in the same directory as the script. You can populate this database with chemical element data using the `fill_table.py` script.

## API Endpoints (FastAPI)

- The script also provides API endpoints for chemical calculations and data access. You can use tools like Postman to make POST requests to these endpoints.

### Example API Requests

- To calculate the molar mass of a compound:
POST /calculation_masse_molaire
{
  "Compose": "H2O"
}


- To calculate the number of moles:
POST /calculation_mol
{
  "Compose": "O2",
  "Masse": "32.0"
}

- For chemical reaction analysis:
POST /engima
{
  "Compose": "2H2 + O2 = 2H2O",
  "Masse": "",
  "Mole": "2",
  "Volume": ""
}

## Author
This script was created by Me.

Feel free to modify and use this script for various chemical calculations and to access chemical element data from the SQLite database.

If you intend to use the FastAPI endpoints, make sure to install FastAPI and Uvicorn, and you can customize the endpoints as needed.
