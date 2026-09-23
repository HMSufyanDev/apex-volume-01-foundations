# JavaScript Object Notation (JSON)
# JSON is simply a text-based data format commonly used for storing and exchanging structured data
# Note: JSON is text. A Python dictionary is a Python object in memory.

# python boolean -> True/False, JSON -> true/false. Python -> None, JSON -> null. In python ""/'' both allowed for strings, in JSON only "" allowed

# Nested Data Works Too
[
    {
        "name": "Sarah Connor",
        "country": "United States",
        "email": "sarah@example.com",
        "status": "New",
        "estimated_value": 4500
    },
    {
        "name": "Alexandre Dubois",
        "country": "France",
        "email": "alex@example.com",
        "status": "Contacted",
        "estimated_value": 12000.5
    }
]

# json Module
import json

# json.dump()
# Take Python data and write it as JSON into a file.
import json

lead = {
    "name": "Sarah",
    "country": "United States",
    "estimated_value": 4500
}

with open("lead.json", "w", encoding="utf-8") as file:
    json.dump(lead, file, indent=4)

# json.dump(data, file, indent=4)
# data: The Python data you want to save:
# file: The open file:
# indent=4: Makes the JSON nicely formatted. Without indentation, you might get: {"name": "Sarah", "country": "United States", "estimated_value": 4500}

# Serialization
# Converting data in memory into a format that can be stored or transmitted.
import json
data = {"name": "Alice", "role": "Developer", "active": True}
# Serialize: Convert Python dict to JSON string
json_string = json.dumps(data)


# json.load()
import json
with open("lead.json", "r", encoding="utf-8") as file:
    data = json.load(file)

print(data)
# This Is Deserialization

# dump() vs dumps()
json.dump()
# Writes JSON directly to a file:
json.dumps()
# Converts Python data into a JSON string:
data = {"name": "Sarah"}
json_text = json.dumps(data)
print(json_text) # {"name": "Sarah"}

# json.loads()
# it takes JSON text and converts it to Python data.


# What Happens If the JSON Is Invalid?
json.load(file)
# Python's JSON parser will raise: json.decoder.JSONDecodeError


