
# AirBnB Imitation - The Command Interface

Welcome to the AirBnB Imitation project! This repository hosts a command-line interface (CLI) designed as part of the AirBnB project at Holberton School. The CLI is aimed at managing objects for a simplified version of the AirBnB website (HBnB).

## Functions of this command interpreter:

- Establish a new object (e.g., a new User or a new Place)
- Retrieve an object from a file, a database, etc...
- Perform operations on objects (count, compute stats, etc...)
- Modify attributes of an object
- Eradicate an object

## Table of Contents

- [Environment](#environment)
- [Installation](#installation)
- [File Descriptions](#file-descriptions)
- [Usage](#usage)
- [Examples of Usage](#examples-of-usage)
- [Testing](#testing)
- [Issues](#issues)
- [Authors](#authors)
- [License](#license)

## Environment

This project is interpreted and tested on Ubuntu 14.04 LTS using Python 3 (version 3.4.3).

## Installation

To get started with this project, follow these steps:

1. Clone this repository:
   ```
   git clone https://github.com/alexaorrico/AirBnB_clone.git
   ```

2. Navigate into the AirBnB directory:
   ```
   cd AirBnB_clone
   ```

3. Launch the console interactively:
   ```
   ./console
   ```

4. Alternatively, execute commands non-interactively:
   ```
   echo "<command>" | ./console.py
   ```

## File Descriptions

### [console.py](console.py)

The `console.py` file serves as the entry point for the command interpreter.

Supported commands:

- `EOF` or `quit`: Exits the console
- `<emptyline>`: Supersedes the default empty line method
- `create`: Creates a new instance of `BaseModel` and saves it to the JSON file
- `destroy`: Deletes an instance based on class name and id (saves changes to JSON)
- `show`: Prints the string representation of an instance based on class name and id
- `all`: Prints string representations of all instances based on class name
- `update`: Updates an instance based on class name and id by adding/updating attributes (saves changes to JSON)

### `/models/` Directory

This directory contains Python class definitions used in the project:

- [base_model.py](/models/base_model.py): Defines the `BaseModel` class, with methods for initialization, string representation, saving, and conversion to dictionary format. Other classes inherit from `BaseModel`.

  Classes inherited from `BaseModel`:
  - [amenity.py](/models/amenity.py)
  - [city.py](/models/city.py)
  - [place.py](/models/place.py)
  - [review.py](/models/review.py)
  - [state.py](/models/state.py)
  - [user.py](/models/user.py)

### `/models/engine/` Directory

This directory contains utility classes for JSON serialization and deserialization:

- [file_storage.py](/models/engine/file_storage.py): Implements the `FileStorage` class, which handles serialization of instances to JSON and deserialization back to instances.

  Methods include:
  - `all()`: Returns the dictionary of objects
  - `new(obj)`: Adds an object to the dictionary
  - `save()`: Saves the objects to the JSON file
  - `reload()`: Reloads objects from the JSON file

### `/tests/` Directory

Contains unit test cases for the project:

- [/test_models/test_base_model.py](/tests/test_models/test_base_model.py): Tests for `BaseModel` and related classes.

  Test classes:
  - `TestBaseModelDocs`: Tests documentation and PEP8 conformity for `base_model.py` and its test file.
  - `TestBaseModel`: Tests instantiation, attribute handling, and methods of `BaseModel`.

- [/test_models/test_amenity.py](/tests/test_models/test_amenity.py): Tests for `Amenity` class.

- [/test_models/test_city.py](/tests/test_models/test_city.py): Tests for `City` class.

- [/test_models/test_file_storage.py](/tests/test_models/test_file_storage.py): Tests for `FileStorage` class.

## Usage

Start the console by running `./console` and use the supported commands to interact with the AirBnB database.

## Examples of Usage

Create a new instance:
```
(hbnb) create User
2f5614b1-3ef2-4bfa-b8d6-85f3c6be1491
```

Show an instance:
```
(hbnb) show User 2f5614b1-3ef2-4bfa-b8d6-85f3c6be1491
[User] (2f5614b1-3ef2-4bfa-b8d6-85f3c6be1491) {'id': '2f5614b1-3ef2-4bfa-b8d6-85f3c6be1491', 'created_at': datetime.datetime(2024, 6, 22, 14, 30, 0, 0), 'updated_at': datetime.datetime(2024, 6, 22, 14, 30, 0, 0)}
```

Update an instance:
```
(hbnb) update User 2f5614b1-3ef2-4bfa-b8d6-85f3c6be1491 first_name "John"
(hbnb) show User 2f5614b1-3ef2-4bfa-b8d6-85f3c6be1491
[User] (2f5614b1-3ef2-4bfa-b8d6-85f3c6be1491) {'id': '2f5614b1-3ef2-4bfa-b8d6-85f3c6be1491', 'created_at': datetime.datetime(2024, 6, 22, 14, 30, 0, 0), 'updated_at': datetime.datetime(2024, 6, 22, 14, 35, 0, 0), 'first_name': 'John'}
```

For more examples and detailed command usage, refer to the [Usage](#usage) section.

## Testing

Run tests using:
```
python3 -m unittest discover tests
```

