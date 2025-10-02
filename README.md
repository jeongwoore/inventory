# Burger King Inventory Management Program

A simple GUI-based inventory management program for managing Burger King menu items.  
Built with PyQt5 and MySQL, it allows adding, updating, deleting, and checking stock of menu items.


## Features (CRUD)
- Create menu items
- Read menu items
- Update menu items
- Delete menu items


## Tech Stack
- Python 3.13.x
- PyQt5
- MySQL Workbench
- pymysql library


## Installation and Running
1. Clone the project
''bash
git clone https://github.com/jeongwoore/inventory.git
cd inventory

2. Create and activate a virtual environment

python -m venv venv
venv\Scripts\activate


3. Install required library
pip install PyQt5
pip install pymysql


4. Set up MySQL database
- Create a database named burger
- Create the menu table

CREATE TABLE menu (
    category VARCHAR(20),
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    price INT,
    stock INT
);

5. Run the program
python app.py