from flask import Flask, jsonify, request
from bson import ObjectId
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/arduinodb"
mongo = PyMongo(app)

@app.route('/arduinodata', methods=['GET'])
def get_all_data():
    data = []
    for d in mongo.db.arduinodata.find():
        data.append({'Microcontroller': d['microcontroller'], 'Operating Voltage': d['operatingVoltage'], 
                     'Supply Voltage recommended': d['supplyVoltageRecommended'],'Digital input Pins':d['digitalIoPins'],
                     'Analog Input Pins': str(d['analogInputPins']),'DC Current per I/O Pin':d['dcCurrentPerIoPin'],
                     'Flash Memory':d['flashMemory'],'SRAM':d['SRAM'],'EEPROM':d['EEPROM'],'Clock Speed':d['clockSpeed']})
    return jsonify({'data': data})

@app.route('/arduinodata/<id>', methods=['GET'])
def get_data(id):
    d = mongo.db.arduinodata.find_one({'_id': ObjectId(id)})
    if d:
        return jsonify({'Microcontroller': d['microcontroller'], 'Operating Voltage': d['operatingVoltage'], 
                        'Supply Voltage recommended': d['supplyVoltageRecommended'],'Digital input Pins':d['digitalIoPins'],
                        'Analog Input Pins': str(d['analogInputPins']),'DC Current per I/O Pin':d['dcCurrentPerIoPin'],
                        'Flash Memory':d['flashMemory'],'SRAM':d['SRAM'],'EEPROM':d['EEPROM'],'Clock Speed':d['clockSpeed']})
    else:
        return jsonify({'error': 'Data not found'})

@app.route('/arduinodata', methods=['POST'])
def add_data():
    #value = request.json['value']
    microcontroller = request.json['microcontroller']
    operatingVoltage = request.json['operatingVoltage']
    supplyVoltageRecommended = request.json['supplyVoltageRecommended']
    digitalIoPins = request.json['digitalIoPins']
    dcCurrentPerIoPin = request.json['dcCurrentPerIoPin']
    flashMemory = request.json['flashMemory']
    SRAM = request.json['SRAM']
    EEPROM = request.json['EEPROM']
    clockSpeed = request.json['clockSpeed']
    #analogInputPins =  request.json[int('analogInputPins')]
    #Microcontroller = request.json['Microcontroller']
    #id = mongo.db.arduinodata.insert_one({'value': value})
    id = mongo.db.arduinodata.insert_one({'microcontroller': microcontroller, 'Operating Voltage':operatingVoltage,'Supply Voltage recommended': supplyVoltageRecommended,
                                            'Digital input Pins':digitalIoPins,'DC Current per I/O Pin':dcCurrentPerIoPin,
                                            'Flash Memory':flashMemory,'SRAM':SRAM,'EEPROM':EEPROM,'Clock Speed':clockSpeed})
                                            #analogInputPins: 'analogInputPins'})
    return jsonify({'Microcontroller':microcontroller
                       ,'Operating Voltage':operatingVoltage,'Supply Voltage recommended': supplyVoltageRecommended,
                       'Digital input Pins':digitalIoPins,'DC Current per I/O Pin':dcCurrentPerIoPin,
                       'Flash Memory':flashMemory,'SRAM':SRAM,'EEPROM':EEPROM,'Clock Speed':clockSpeed,})
                       #'Analog Input Pins': str(analogInputPins)})

@app.route('/arduinodata/<id>', methods=['PUT'])
def update_data(id):
    #value = request.json['value']
    microcontroller = request.json['microcontroller']
    operatingVoltage = request.json['operatingVoltage']
    supplyVoltageRecommended = request.json['supplyVoltageRecommended']
    digitalIoPins = request.json['digitalIoPins']
    dcCurrentPerIoPin = request.json['dcCurrentPerIoPin']
    flashMemory = request.json['flashMemory']
    SRAM = request.json['SRAM']
    EEPROM = request.json['EEPROM']
    clockSpeed = request.json['clockSpeed']
    analogInputPins= int(request.json['analogInputPins'])
    #id = mongo.db.arduinodata.insert_one({'value': value})
    d = mongo.db.arduinodata.find_one_and_update(
        {'_id': ObjectId(id)}, {'$set': {'microcontroller': microcontroller, 'operatingVoltage': operatingVoltage, 
                                         'supplyVoltageRecommended': supplyVoltageRecommended,'digitalIoPins':digitalIoPins,
                                         'analogInputPins': analogInputPins,
                                         'dcCurrentPerIoPin':dcCurrentPerIoPin,
                                         'flashMemory':flashMemory,'SRAM':SRAM,'EEPROM':EEPROM,'clockSpeed':clockSpeed}}, return_document=True)
    if d:
        #return jsonify({'id': str(d['_id']), 'value': d['value']})
        return jsonify({'microcontroller': d['microcontroller'], 'operatingVoltage': d['operatingVoltage'], 
                        'supplyVoltageRecommended': d['supplyVoltageRecommended'],'digitalIoPins':d['digitalIoPins'],
                        'analogInputPins': d['analogInputPins'],
                        'dcCurrentPerIoPin':d['dcCurrentPerIoPin'],
                        'flashMemory':d['flashMemory'],'SRAM':d['SRAM'],'EEPROM':d['EEPROM'],'clockSpeed':d['clockSpeed']})
    else:
        return jsonify({'error': 'Data not found'})

@app.route('/arduinodata/<id>', methods=['DELETE'])
def delete_data(id):
    result = mongo.db.arduinodata.delete_one({'_id': ObjectId(id)})
    if result.deleted_count == 1:
        return jsonify({'message': 'Data deleted successfully'})
    else:
        return jsonify({'error': 'Data not found'})


if __name__ == '__main__':
    app.run(host="0.0.0.0")