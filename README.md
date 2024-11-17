# AirBnB Clone - Command Interpreter

This project is part of the AirBnB clone series and implements a command-line interface (CLI) that interacts with a simple object-oriented storage engine. The goal is to create a system where we can manage users, places, states, cities, amenities, reviews, and more, all from the terminal.

## Project Overview

This repository contains:
1. A **command-line interpreter** that allows users to create, read, update, and delete instances of various classes (such as `User`, `State`, `City`, `Place`, etc.).
2. A **serialization engine** that converts instances to and from JSON, enabling persistent storage of objects.
3. Unit tests to ensure the CLI commands work as expected.

### Project Structure

Here is the expected project structure based on your description:

```
AirBnB_clone/
│
├── console.py
│
├── models/
│   ├── __init__.py
│   ├── base_models.py
|   ├── amenity.py
│   ├── city.py
│   ├── place.py
│   ├── review.py
│   ├── state.py
│   └── user.py
│   └── engine/
│       ├── __init__.py
│       └── file_storage.py
│
└── test/
    ├── __init__.py
    ├── test_base_model.py
    ├── test_file_storage.py
    ├── test_console.py
    └── test_models.py
```

## Features

- **Command Interpreter**: Interacts with the AirBnB object models through commands like `create`, `show`, `destroy`, `update`, `all`, and `count`.
- **Persistence**: Uses a JSON file to store instances between program runs.
- **Object Serialization/Deserialization**: Automatically converts objects to and from JSON format.
- **Dynamic Class Management**: You can add or remove models, and they will be automatically integrated into the system.

## Requirements

- Python 3.x
- `unittest` for testing
- `cmd` for building the command-line interface

## Models

The project includes the following classes (models), which inherit from the `BaseModel` class:

- **BaseModel**: The parent class for all models. Manages common attributes like `id`, `created_at`, `updated_at`, and provides methods for serialization and deserialization.
- **User**: A user of the AirBnB service.
- **State**: A geographical state.
- **City**: A city within a state.
- **Amenity**: An amenity available at a place.
- **Place**: A place listing, such as a house or apartment.
- **Review**: A review written by a user for a specific place.

## Installation

Clone the repository to your local machine:
   ```bash
   git clone https://github.com/makauj/AirBnB_clone.git
   cd AirBnB_clone
   ```

## Usage

### Starting the Command-Line Interface (CLI)

To start the command-line interface, simply run:

```bash
python3 console.py
or
./console.py
```

This will drop you into the interactive prompt `(hbnb)` where you can execute commands.

### Available Commands

The CLI supports the following commands:

#### `create <class name>`
Creates a new instance of the specified class, saves it, and prints its unique ID.  
Example:
```bash
(hbnb) create User
```

#### `show <class name> <id>`
Prints the string representation of an instance based on the class name and its ID.  
Example:
```bash
(hbnb) show User 1234-1234-1234
```

#### `destroy <class name> <id>`
Deletes an instance based on the class name and ID.  
Example:
```bash
(hbnb) destroy User 1234-1234-1234
```

#### `update <class name> <id> <attribute name> <attribute value>`
Updates an attribute of an instance. Only one attribute can be updated at a time.  
Example:
```bash
(hbnb) update User 1234-1234-1234 email "new_email@example.com"
```

#### `update <class name> <id> <dictionary>`
Updates an instance based on a dictionary of attributes.  
Example:
```bash
(hbnb) update User 1234-1234-1234 {'email': 'new_email@example.com', 'first_name': 'John'}
```

#### `all [<class name>]`
Prints all instances of the specified class, or all instances of all classes if no class is specified.  
Example:
```bash
(hbnb) all User
```

#### `count <class name>`
Prints the number of instances of the specified class.  
Example:
```bash
(hbnb) count User
```

#### `quit` or `EOF`
Exits the command-line interface.  
Example:
```bash
(hbnb) quit
```

### Error Handling

The command interpreter includes basic error handling for invalid inputs, including:

- **Missing class name**: If no class name is provided, it will print `** class name missing **`.
- **Non-existent class**: If the class does not exist, it will print `** class doesn't exist **`.
- **Missing instance ID**: If no instance ID is provided, it will print `** instance id missing **`.
- **Instance not found**: If the instance with the given ID does not exist, it will print `** no instance found **`.
- **Attribute name or value missing**: If the attribute name or value is missing for an update, it will print the relevant error message.

## File Storage

The `FileStorage` engine is used for serializing and deserializing instances of classes to a JSON file, enabling data persistence across runs. The file is stored in `file.json` and contains all instances of the models.

## Testing

Unit tests are provided to ensure the correctness of the program. They can be run with:

```bash
python3 -m unittest discover tests
```

This will run all tests in the `tests/` directory, which includes tests for all available commands and error handling.

### Testing the Console with Mocking

To test the console without actually running it interactively, you can use the `patch` method from the `unittest.mock` module to intercept the `stdout` and test the output. This is useful for automated testing of command-line interactions.

## Contributing

If you'd like to contribute to this project, feel free to fork the repository, make your changes, and submit a pull request. All contributions are welcome!