**Python CLI-based Student Management System**

This project is a simple command-line / console based Student Management System using Python and the file system. It allows you to add, delete, search for, and view all students in the system.

**Features:**

* Add students
* Delete students
* Search for students
* View all students

**Requirements:**

* Python 3.6 or higher
* The file system

**Usage:**

1. Clone the repository:

```
git clone https://github.com/OMKARGOPCHADE/python-project.git
```

2. Navigate to the project directory:

```
cd python-project
```

3. Install the requirements:

```
pip install -r requirements.txt
```

4. Run the program:

```
python main.py
```

**Commands:**

* **add <name> <roll_no> <branch> <year>:** Adds a new student to the system.
* **delete <roll_no>:** Deletes a student from the system.
* **search <name>:** Searches for a student by name.
* **view:** Views all students in the system.

**Example:**

```
# Add a new student
python main.py add John Doe 12345 CSE 2023

# Delete a student
python main.py delete 12345

# Search for a student by name
python main.py search John Doe

# View all students
python main.py view
```

**Contributing:**

Please feel free to contribute to this project by adding new features, fixing bugs, or suggesting improvements. To contribute, simply fork the repository, make your changes, and submit a pull request.
