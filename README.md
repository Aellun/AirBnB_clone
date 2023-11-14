AirBnB Clone Project
========================================================================================
Functionalities of HBNB command interpreter:

Create a new object
Retrieve an object from a file, a database
Do operations on objects (count,
Update attributes of an object
Destroy an object


==================Environment===============
This project is interpreted/tested on Ubuntu 14.04 LTS using python3 (version 3.4.3)

===========Installation==============
Clone this repository: git clone "git@github.com:Aellun/AirBnB_clone.git"
Access AirBnb directory: cd AirBnB_clone
Run hbnb(interactively): ./console and enter command
Run hbnb(non-interactively): echo "<command>" | ./console.py

==================File Descriptions==========
console.py - the console contains the entry point of the command interpreter.
================================================================================================================================
The following are the list of commands currently supported

EOF - exits console
>>quit - exits console
>><emptyline> - overwrites default emptyline method and does nothing
>>create - Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id
>>destroy - Deletes an instance based on the class name and id (save the change into the JSON file).
>>show - Prints the string representation of an instance based on the class name and id.
>>all - Prints all string representation of all instances based or not on the class name.
>>update - Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file).
>>count -  retrieves the number of instance of the class
>>models/ directory contains classes used for this project:
>>base_model.py - The BaseModel is the parent class from which all classes inherits their attributes
=======================================================================================================================================
def __init__(self, *args, **kwargs) - Initialization of the base model
def __str__(self) - String representation of the BaseModel class
def save(self) - Updates the attribute updated_at with the current datetime
def to_dict(self) - returns a dictionary containing all keys/values of the instance
=====================================================================================================================================
Classes inherited from Base Model:

>>amenity.py
>>city.py
>>place.py
>>review.py
>>state.py
>>user.py
/models/engine directory contains File Storage class that handles JASON serialization and deserialization :
file_storage.py - serializes instances to a JSON file & deserializes back to instances
