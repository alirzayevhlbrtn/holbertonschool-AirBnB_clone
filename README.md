<h1 align="center">AirBnB Clone Command Interpreter</h1>

This project is a command-line interpreter (CLI) for managing AirBnB objects.


<h2 align="center">AirBnB Clone Command Interpreter</h2>

To start the AirBnB Clone Command Interpreter, follow these steps:
1. Clone the  our repository from GitHub:
```
git clone https://github.com/alirzayevhlbrtn/holbertonschool-AirBnB_clone.git
```
2. Navigate to the project directory:
```
cd holbertonschool-AirBnB_clone
```
3. Give file execute permission:
```
chmod +x console.py
```
4. Run the command interpreter:
```
./console.py
```


<h2 align="center">Storage</h2>

The command interpreter uses a storage engine to manage AirBnB objects. The storage engine is implemented using a JSON file to store and retrieve objects. The storage engine is defined in the [file_storage.py]. The storage engine supports the following methods:

- `all`: Retrieve all objects from the storage.
- `new`: Add a new object to the storage.
- `save`: Save changes to the storage.
- `reload`: Reload objects from the storage.

The storage engine is used by the command interpreter to manage AirBnB objects.


<h2 align="center">the Command Interpreter</h2>

The command interpreter supports the following commands:

- `EOF`: Exit the command interpreter.
- `all`: Retrieve all objects from the storage.
- `create`: Create a new object.
- `destroy`: Delete an object.
- `help`: Display help information.
- `quit`: Exit the command interpreter.
- `show`: Display information about an object.
- `update`: Update an object.

The command interpreter supports the following objects:

- `Amenity`
- `BaseModel`
- `City`
- `Place`
- `Review`
- `State`
- `User`

To run the command interpreter in non-interactive mode, echo the command and pipe it into the command interpreter. For example:
```
echo "help" | ./console.py
```


<h2 align="center">Testing</h2>

Unit tests for the command interpreter are located in the [tests](./tests/) directory. To run the tests, navigate to the project directory and run the following command:

```
python3 -m unittest discover tests
```


<h2 align="center">Authors</h2>

- [Saleh Shahverdiyev](https://github.com/vasifvortex)
- [Uzeyir Alirzayev](https://github.com/alirzayevhlbrtn)


<h2 align="center">License</h2>
This project is licensed under the GNU GENERAL PUBLIC LICENSE - see the [LICENSE](./LICENSE) file for details.
