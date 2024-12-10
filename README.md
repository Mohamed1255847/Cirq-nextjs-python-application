# Cirq Next.js Python Application

This project combines a **Python backend** with a **Next.js front-end** to create a quantum simulator built on Cirq. Follow the steps below to set up and run the application.

---

## Backend: Running the API


```bash
# Step 1: Navigate to the root folder, then into the backend directory
cd backend
# Step 2: install flask_cors 
pip install flask_cors
or using docs https://flask-cors.readthedocs.io/en/v1.1/
# Step 3: install flask
pip install flask
or using docs https://flask.palletsprojects.com/en/stable/installation/#install-flask 
cd backend
# Step 4: Run the API
python3 app.py
# OR
python app.py

# Step 3: You should see output like this:
# Example Output:
# [API is now running on http://localhost:5000]
```
![image](https://github.com/user-attachments/assets/1f2b1024-0e6b-4262-951a-efcc0a4528ea)

## Frontend: Running the NextJS Application 

### Step 1: Navigate to the root folder, then into the front-end directory
cd quantum-simulator-on-cirq

### Step 2: Open the folder in a terminal (e.g., PowerShell, CMD, or your terminal of choice)

### Step 3: Ensure you have Node.js installed
### If not, follow the installation guide:
### https://nodejs.org/en/download/package-manager

### Step 4: Ensure you have Yarn installed
### If not, follow the installation guide:
### https://yarnpkg.com/getting-started/install

### Step 5: Install dependencies

```bash
yarn
```
### Step 6: Start the development server

```bash
yarn dev
```
### then open http://localhost:3000/
![image](https://github.com/user-attachments/assets/6117ae4e-24dc-495e-b281-3cd58be7850c)
