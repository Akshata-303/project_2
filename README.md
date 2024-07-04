Arduino Data API:
This project is a RESTful API built with Flask and Flask-PyMongo to interact with a MongoDB database. The API allows you to perform CRUD operations on Arduino data.

Prerequisites
1.Python 3.x
2.MongoDB
3.Flask
4.Flask-PyMongo
5.bson (comes with PyMongo)

Setup
1. Clone the Repository
   git clone <repository-url>
   cd <repository-directory>
2. Install Dependencies
   pip install Flask Flask-PyMongo
3. MongoDB Setup
   Ensure you have MongoDB installed and running on your local machine. The default MongoDB URI is set to mongodb://localhost:27017/arduinodb. You can change this in the Flask app configuration if needed.
4. Run the Flask Application
   python app.py

API Endpoints
Get All Arduino Data
URL: /arduinodata
Method: GET
Description: Fetches all Arduino data entries from the database.
Response: JSON object containing an array of Arduino data.

Get Arduino Data by ID
URL: /arduinodata/<id>
Method: GET
Description: Fetches a single Arduino data entry by its ID.
Response: JSON object containing the Arduino data or an error message if not found.

Add New Arduino Data
URL: /arduinodata
Method: POST
Description: Adds a new Arduino data entry to the database.
Body Parameters:
microcontroller: string
operatingVoltage: string
supplyVoltageRecommended: string
digitalIoPins: integer
analogInputPins: integer
dcCurrentPerIoPin: string
flashMemory: string
SRAM: string
EEPROM: string
clockSpeed: string
Response: JSON object containing the added Arduino data.

Update Arduino Data by ID
URL: /arduinodata/<id>
Method: PUT
Description: Updates an existing Arduino data entry by its ID.
Body Parameters:
microcontroller: string
operatingVoltage: string
supplyVoltageRecommended: string
digitalIoPins: integer
analogInputPins: integer
dcCurrentPerIoPin: string
flashMemory: string
SRAM: string
EEPROM: string
clockSpeed: string
Response: JSON object containing the updated Arduino data or an error message if not found.

Delete Arduino Data by ID
URL: /arduinodata/<id>
Method: DELETE
Description: Deletes an Arduino data entry by its ID.
Response: JSON object containing a success message or an error message if not found.

Example Requests
Get All Data:
curl -X GET http://0.0.0.0:5000/arduinodata

Get Data by ID:
curl -X GET http://0.0.0.0:5000/arduinodata/<id>

Add New Data:
curl -X POST http://0.0.0.0:5000/arduinodata -H "Content-Type: application/json" -d '{
  "microcontroller": "ATmega328",
  "operatingVoltage": "5V",
  "supplyVoltageRecommended": "7-12V",
  "digitalIoPins": 14,
  "analogInputPins": 6,
  "dcCurrentPerIoPin": "40mA",
  "flashMemory": "32KB",
  "SRAM": "2KB",
  "EEPROM": "1KB",
  "clockSpeed": "16MHz"
}'

Update Data by ID:
curl -X PUT http://0.0.0.0:5000/arduinodata/<id> -H "Content-Type: application/json" -d '{
  "microcontroller": "ATmega328",
  "operatingVoltage": "5V",
  "supplyVoltageRecommended": "7-12V",
  "digitalIoPins": 14,
  "analogInputPins": 6,
  "dcCurrentPerIoPin": "40mA",
  "flashMemory": "32KB",
  "SRAM": "2KB",
  "EEPROM": "1KB",
  "clockSpeed": "16MHz"
}'

Delete Data by ID:
curl -X DELETE http://0.0.0.0:5000/arduinodata/<id>

Notes:
-Ensure MongoDB is running on your local machine.
-The Flask server listens on all available IP addresses (0.0.0.0) and port 5000.
