# AirBnB Clone - The Console

## Description

This project is the first step in building a full web application: the AirBnB clone. In this stage, we will implement a command-line interpreter (CLI) to manage AirBnB objects like users, places, and other entities. The console is the backbone for all interactions, helping users create, update, delete, and retrieve instances of the different objects in a structured way.

## Key Features:

- Manage AirBnB objects: create, retrieve, update, and destroy.
- Serialization and deserialization of objects using JSON format.
- Abstracted storage engine using file storage.
- Classes like User, Place, City, etc., inherit from a base class (BaseModel).
- Fully equipped with unit tests to validate functionality.

## Command Interpreter

The command interpreter is similar to a shell, where users can issue commands to manage the objects of our project.

### How to Start It

**Interactive Mode:** To start the console in interactive mode, simply run:

		$ ./console.py
		(hbnb)
Non-Interactive Mode: You can also run commands without entering the shell:
		$ echo "command" | ./console.py
		(hbnb)

### How to Use It

**Available Commands:**

- **quit** - Exits the program.
- **EOF** - Exits the program (end-of-file).
- **create <class>** - Creates a new instance of a class (e.g., User, Place).
- **show <class> <id>** - Retrieves the string representation of an instance based on class and ID.
- **destroy <class> <id>** - Deletes an instance based on class and ID.
- **all** - Shows all instances (optionally, you can specify a class).
- **update <class> <id>** <attribute_name> <attribute_value> - Updates an instance by adding or modifying an attribute.

### Examples
**Interactive Mode:**

		$ ./console.py
		(hbnb) create User
		(hbnb) show User 1234-1234-1234
		(hbnb) update User 1234-1234-1234 email "example@domain.com"
		(hbnb) all
		(hbnb) destroy User 1234-1234-1234
		(hbnb) quit

**Non-Interactive Mode:**

		$ echo "create User" | ./console.py
		$ echo "all" | ./console.py
