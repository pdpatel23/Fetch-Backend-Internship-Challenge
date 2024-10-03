# Fetch-Backend-Internship-Challenge

## Overview


This is a simple REST API that tracks points for a single user across multiple payers. The API allows users to:
- Add points from a payer
- Spend points using the oldest points first
- Get the current balance of points per payer


The API follows RESTful principles and has been tested using the `cURL` command.


**Note**: We will be using Git and Git Bash: First to clone the repository and be able to use it. And then use Git Bash To test the API methods using cURL due to easier and readable outputs. If you don’t have Git installed (Git Bash comes with Git), please follow the instructions below to install it.


## Prerequisites


- **Python 3.7+** (I am using 3.12.1)
- **Flask** library


Make sure Python and Flask are installed on your machine before running the code.


### Installation Instructions


1. Install Python:
   - If Python isn't installed on your system, download it from https://www.python.org/downloads/.


2. Install Flask:
   - You can install Flask using `pip`:
     ```
     pip install Flask
     ```


#### Git and Git Bash Installation Instructions

1. Download Git from the official Git for Windows site: https://gitforwindows.org/.
2. Run the downloaded file and follow the installation instructions.
3. During the installation process, you can choose the default options by clicking "Next" through the prompts. Ensure that **Git Bash** is selected as one of the components to install in the **Select Components** step.
4. Once installed, you can open Git Bash from the Start menu and going into your directory, or by right-clicking in a folder and selecting **"Open Git Bash Here"**.




* This link provides more details for downloading Git if the steps above dont work: https://www.stanleyulili.com/git/how-to-install-git-bash-on-windows






## Running the API


1. In order to download the GitHub repository, use `git clone` in your desired directory in terminal.
   
2. Navigate to the directory containing the `app.py` file.


3. Run the Flask server in the terminal:
   ```
   python app.py
   ```


4. The server will start on port 8000, and the base URL will be `http://localhost:8000`.


5. Open a new terminal window while the server is running and use cURL commands to interact with the API.


## API Endpoints Information


### Add Points


- **URL**: `/add`
- **Method**: `POST`
- **Request Body**:
   ```json
   {
      "payer": "DANNON",
      "points": 300,
      "timestamp": "2022-10-31T10:00:00Z"
   }
   ```
- **Response**: Status code `200` when success.


### Spend Points


- **URL**: `/spend`
- **Method**: `POST`
- **Request Body**:
   ```json
   {
      "points": 5000
   }
   ```
- **Response**: A list of payers and the points spent from each, example:
   ```json
   [
      { "payer": "DANNON", "points": -100 },
      { "payer": "UNILEVER", "points": -200 },
      { "payer": "MILLER COORS", "points": -4700 }
   ]
   ```
   If there are not enough points, the server will return a `400` error with the message: `"The user doesn't have enough points"`.


### Get Balance


- **URL**: `/balance`
- **Method**: `GET`
- **Response**: The current balance for each payer, e.g.:
   ```json
   {
      "DANNON": 1000,
      "UNILEVER": 0,
      "MILLER COORS": 5300
   }
   ```


## Testing the code


To test the API, you can use `cURL` commands. Here’s how to test the functionalities:


Before running the commands, make sure you run a new "Git Bash" terminal and go into the directory where app.py is.


1. Add points from different payers:
   ```bash
   curl -X POST http://localhost:8000/add -H "Content-Type: application/json" -d '{"payer": "DANNON", "points": 300, "timestamp": "2022-10-31T10:00:00Z"}'
   ```


2. Spend points:
   ```bash
   curl -X POST http://localhost:8000/spend -H "Content-Type: application/json" -d '{"points": 5000}'
   ```


3. Check the balance:
   ```bash
   curl http://localhost:8000/balance
   ```




### Example Test to Check (Provided in the writeup)


After running the app, provide it with these specific commands


1. Add a couple payers:
    ```bash
    curl -X POST http://localhost:8000/add -H "Content-Type: application/json" -d '{"payer": "DANNON", "points": 300, "timestamp": "2022-10-31T10:00:00Z" }'


    curl -X POST http://localhost:8000/add -H "Content-Type: application/json" -d '{"payer": "UNILEVER", "points": 200, "timestamp": "2022-10-31T11:00:00Z" }'


    curl -X POST http://localhost:8000/add -H "Content-Type: application/json" -d '{"payer": "DANNON", "points":-200, "timestamp": "2022-10-31T15:00:00Z" }'


    curl -X POST http://localhost:8000/add -H "Content-Type: application/json" -d '{"payer": "MILLER COORS", "points": 10000, "timestamp": "2022-11-01T14:00:00Z" }'
   
    curl -X POST http://localhost:8000/add -H "Content-Type: application/json" -d '{"payer": "DANNON", "points": 1000, "timestamp": "2022-11-02T14:00:00Z" }'
    ```


2. Spend points:
    ```bash
    curl -X POST http://localhost:8000/spend -H "Content-Type: application/json" -d '{"points": 5000}'
    ```
    * Output from this should be:
        ```json
        {
            "DANNON": -100,
            "UNILEVER": -200,
            "MILLER COORS": -4700
        }
        ```


3. Lastly, check the balance:


    ```bash
    curl http://localhost:8000/balance
    ```


    * The output should be:
        ```json
            {
                "DANNON":1000,
                "UNILEVER":0,
                "MILLER COORS":5300
            }
        ```
        
### Note:


- Make sure you are in a new Git Bash terminal tab to run the cURL commands while keeping the Flask server running in the original terminal.
- If you need to stop the server at any point, go back to the terminal running `python app.py` and press `Ctrl+C` to stop it.


