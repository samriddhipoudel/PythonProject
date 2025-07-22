# Land Rental Management System – TechnoPropertyNepal

This repository contains a Python-based console application developed as part of the *CC4059NI: Fundamentals of Computing* coursework. The system is designed for managing land rental operations for a fictional real estate company, **TechnoPropertyNepal**, which oversees land listings in various locations across Nepal.

## Project Overview

The Land Rental Management System allows users to perform the following tasks:
- View available land listings
- Rent and return land
- Generate invoices for each transaction
- Track land availability status in real-time

The objective of this project is to demonstrate practical knowledge of:
- Python programming (with a focus on procedural and modular design)
- File handling and data persistence
- Input validation and error handling
- Functional decomposition using multiple modules

## Project Structure

The system is organized into the following Python modules:

- `main.py`: Entry point of the application; handles user interface and navigation  
- `operation.py`: Contains logic for renting and returning land  
- `read.py`: Responsible for reading land data from `land.txt`  
- `write.py`: Manages billing and writing updated land data and invoices to files  
- `land.txt`: Text file used to store and update land records (including location, cost, and availability)

## Features

- Console-based user interface with guided prompts  
- Modular code design for maintainability  
- Role-based user actions (renter and returner)  
- Rental duration and return tracking with fine calculation for late returns  
- Automatic invoice generation and saving to text files  
- Robust error handling and input validation

## How to Run

To run the application, ensure you have Python installed on your system and follow the steps below:

1. Clone or download this repository to your local machine  
2. Ensure all required files (`main.py`, `operation.py`, `read.py`, `write.py`, and `land.txt`) are in the same directory  
3. Open a terminal or command prompt and navigate to the project directory  
4. Execute the following command:

```bash
python main.py

Sample land.txt Format
Each line in land.txt represents a land listing and includes the following comma-separated values:

php-template
Copy
Edit
<Kitta Number>, <Location>, <Direction>, <Area (annas)>, <Rental Cost>, <Availability>
Example:

mathematica
Copy
Edit
101, Kathmandu, North, 4, 50000, Available
102, Pokhara, East, 5, 60000, Not Available
103, Lalitpur, South, 10, 100000, Available
Developed By
Samriddhi Poudel
Student ID: 23047345
Course: CC4059NI – Fundamentals of Computing
Affiliated with: London Metropolitan University
Academic Year: 2023/24

Disclaimer
This project was developed solely for educational purposes as part of a university coursework submission. It is not intended for production use or real-world deployment.
