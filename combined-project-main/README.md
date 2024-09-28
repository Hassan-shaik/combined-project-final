
# Project Overview

This repository contains three distinct programs:

1. **FindIt**
2. **Laundry**
3. **Opt-out of Food Service**

Each program is designed to streamline different processes, and all are built using Python, Flask, and SQLite. This README provides the necessary steps to set up and run each application.

---

## Prerequisites

Before running any of the applications, ensure that the following software is installed on your machine:

- **Python** (Version 3.x or later)
- **pip** (Python package installer)
- **Node.js** (JavaScript runtime)
- **Flask** (Web framework for Python)
- **SQLite3** (Database engine)
- **SQLAlchemy** (SQL toolkit for Python)

### Installation Steps

1. **Install Python and pip**  
   - Download and install Python from [here](https://www.python.org/downloads/).  
   - Ensure `pip` is installed by running:  
     ```bash
     python -m ensurepip --upgrade
     ```

2. **Install Node.js**  
   - Download and install Node.js from [here](https://nodejs.org/).  
   
3. **Install Flask and SQLAlchemy**  
   - Install Flask by running:  
     ```bash
     pip install Flask
     ```  
   - Install SQLAlchemy by running:  
     ```bash
     pip install SQLAlchemy
     ```

---

## Program 1: FindIt

FindIt is a program designed to help users locate items.

### Running the Application:

1. Navigate to the `findit` folder:

2. Run the application:
   ```bash
   python app.py
   ```

3. Open a browser and navigate to the provided localhost address (typically `http://127.0.0.1:5000`).

---

## Program 2: Laundry

The Laundry program allows users to generate QR codes for managing laundry service details.

### QR Code Generation:

1. Use the `home.html` file located in the `qr generation` folder to generate QR codes.

### Running the Application:

1. Navigate to the `laundry` folder:

2. Run the application:
   ```bash
   python app.py
   ```

3. Open a browser and navigate to the provided localhost address (typically `http://127.0.0.1:5000`).

4. Scan your generated QR code to enter details.

---

## Program 3: Opt-out of Food Service

The Opt-out of Food Service application consists of two components: the **main app** and the **management app**. Each runs on different ports.

### Running the Application:

1. **Main App**
   - Navigate to the `main` directory:

   - Run the main application:
     ```bash
     python app.py
     ```

   - This will run on a designated port (e.g., `http://127.0.0.1:5000`).

2. **Management App**
   - Open a new terminal and navigate to the `management` directory:
     ```bash

   - Run the management application:
     ```bash
     python app.py
     ```

   - This will run on a different port (e.g., `http://127.0.0.1:5001`).

---

## Additional Notes

- Make sure the necessary dependencies are installed before running each application.
- Always ensure the appropriate directories are active when running the applications.
- If there are port conflicts, you can change the port number in the `app.py` file for each service.

---

## License

This project is licensed under the Creative Commons License. See the LICENSE file for more details.

---

