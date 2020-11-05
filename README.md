# AirBnB

is an American vacation rental online marketplace company based in San Francisco-California, United States. Airbnb offers arrangement for lodging, primarily homestays, or tourism experiences. The company does not own any of the real estate listings, nor does it host events; it acts as a broker, receiving commissions from each booking.[more](https://en.wikipedia.org/wiki/Airbnb)

## AirBnB Clone


In the first phase of the AirBnB project we created a console to manipulate line commands

This is the first step towards building your first full web application: the AirBnB clone.

![](https://img.shields.io/badge/Linux-Bash-lightgrey) ![](https://img.shields.io/badge/Project-Shell-lightgrey) ![](https://img.shields.io/badge/Release-v1.0-blue) ![](https://img.shields.io/badge/Python-3.4.3-yellow)

## what this command interpreter do?

Create a new object (ex: a new User or a new Place)
Retrieve an object from a file, a database etc…
Do operations on objects (count, compute stats, etc…)
Update attributes of an object
Destroy an object

## Environment.

All code was proof with pep8 style guide checker \(V1.7\).
Environment develpment used was:

- Ubuntu 14.04 LTS
- Python 3.4.3
- Interpreter’s Python
- Json File
- OOP programming


## Content

This proyect has two branches and HEAD(main): one branch for each developer and branch main that contains the project.

This project allow you create User, City and State and save with unique ID, Datetime, as well as update them.

## Data hierarchy:

**Console.py** this is point enter command interpreter

**hierarchy**
<pre>
console.py
models<br \>
    base_model.py<br \>
    amenity.py<br \>
    city.py<br \>
    state.py<br \>
    place.py<br \>
    review.py<br \>
    user.py<br \>

engine<br \>
    file_storage.py<br \>

</pre>

# How to clone

You must have installed git.
if you need install it [click here](https://github.com/git-guides/install-git#:~:text=To%20install%20Git%2C%20navigate%20to,installation%20by%20typing%3A%20git%20version%20.).

Now, clone this repo:
 - first step
write: `git clone https://github.com/cristian-bedoya/AirBnB_clone.git`

 - Then you must enter into it, thus.
`cd AirBnB_clone`

Now, you current directory id **AirBnB_clone**

# How to use it

Execute the file called console:

`./console.py`

you can create User, City, State as mencioned above, thus.
Ex:
```Python
(hbnb) create User
db83e8f2-e3f1-4710-8e29-48ce638e423a
(hbnb) create City
54a4cff6-d271-412b-8236-ba534947e819
(hbnb) create State
e04290ed-5b95-49b2-8082-af4ddaafa23f
(hbnb) all
["[User] (db83e8f2-e3f1-4710-8e29-48ce638e423a) {'created_at': datetime.datetime(2020, 11, 5, 15, 22, 9, 83951), 'updated_at': datetime.datetime(2020, 11, 5, 15, 22, 9, 84173), 'id': 'db83e8f2-e3f1-4710-8e29-48ce638e423a'}", "[City] (54a4cff6-d271-412b-8236-ba534947e819) {'created_at': datetime.datetime(2020, 11, 5, 15, 22, 12, 639999), 'updated_at': datetime.datetime(2020, 11, 5, 15, 22, 12, 640148), 'id': '54a4cff6-d271-412b-8236-ba534947e819'}", "[State] (e04290ed-5b95-49b2-8082-af4ddaafa23f) {'created_at': datetime.datetime(2020, 11, 5, 15, 22, 18, 29407), 'updated_at': datetime.datetime(2020, 11, 5, 15, 22, 18, 29606), 'id': 'e04290ed-5b95-49b2-8082-af4ddaafa23f'}"]
```
**Note:**: once created it save a file with extension Json.

if you want to know what commands are accepted write help, thus.

```Python
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb) help create
Create attribute and save it in Json file

        Args:
            line ([type]): [description]
        
(hbnb) 
```

**Note**: write help <command> to know how to use that itself command.

# Copyright

> &copy; Holberton Students

