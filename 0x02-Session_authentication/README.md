# ALX Backend User Data - 0x02-Session Authentication

This repository contains solutions to the ALX Backend program's task titled **"Session Authentication"**. It focuses on implementing various authentication mechanisms, including **Session Authentication**, **Session Expiration**, and **Session Persistence in a Database**.

## Table of Contents

- [Project Description](#project-description)
- [Technologies](#technologies)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Tests](#tests)
- [Contributing](#contributing)
- [Author](#author)
- [License](#license)

## Project Description

This project demonstrates the implementation of different session authentication methods for a backend API. It explores:
- **Basic Session Authentication**: where the session ID is stored temporarily in memory.
- **Session Expiration**: adding expiration time for session IDs.
- **Session Persistence in a Database**: ensuring session IDs are stored persistently in a database (or file), preventing loss when the application stops or restarts.

The goal of the project is to reinforce knowledge of authentication systems and handling user sessions securely.

## Technologies

- Python 3.7+
- Flask (for backend API)
- SQLAlchemy (for database interaction)
- HTTP cookies (for session management)
- Environment variables for configuration

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/harystyleseze/alx-backend-user-data.git
   cd alx-backend-user-data/0x02-Session_authentication
   ```

2. Install dependencies:
   - Create a virtual environment (optional but recommended):
     ```bash
     python3 -m venv venv
     source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
     ```
   - Install required packages:
     ```bash
     pip install -r requirements.txt
     ```

3. Set the necessary environment variables before running the application:
   ```bash
   export API_HOST=0.0.0.0
   export API_PORT=5000
   export AUTH_TYPE=session_db_auth  # or session_exp_auth based on your task
   export SESSION_NAME=_my_session_id
   export SESSION_DURATION=60  # Session expiration in seconds (optional)
   ```

4. Start the Flask application:
   ```bash
   python3 -m api.v1.app
   ```

The app should now be running at `http://0.0.0.0:5000/` (or whichever host and port you've configured).

## Usage

Once the application is running, you can test the API using `curl` or Postman:

1. **Login** (create a session):
   ```bash
   curl "http://0.0.0.0:5000/api/v1/auth_session/login" -XPOST -d "email=bobsession@hbtn.io" -d "password=fake_pwd"
   ```

   This should return a JSON response with user information and set a session cookie (`_my_session_id`).

2. **Access Protected Route** (using the session ID cookie):
   ```bash
   curl "http://0.0.0.0:5000/api/v1/users/me" --cookie "_my_session_id=your_session_id_here"
   ```

3. **Logout** (destroy the session):
   ```bash
   curl "http://0.0.0.0:5000/api/v1/auth_session/logout" --cookie "_my_session_id=your_session_id_here" -X DELETE
   ```

   This will destroy the session and the user will no longer be able to access protected routes.

## Project Structure

The directory structure of the project is as follows:

```
0x02-Session_authentication/
├── api/
│   └── v1/
│       └── auth/
│           ├── session_auth.py
│           ├── session_exp_auth.py
│           ├── session_db_auth.py
│       └── app.py
├── models/
│   ├── user.py
│   ├── user_session.py
├── requirements.txt
└── README.md
```

### Important Files:

- **api/v1/auth/session_auth.py**: Contains basic session authentication logic.
- **api/v1/auth/session_exp_auth.py**: Adds session expiration to the authentication system.
- **api/v1/auth/session_db_auth.py**: Stores session IDs in a database or file, persisting session data.
- **models/user.py**: Represents the User model in the application.
- **models/user_session.py**: Represents the UserSession model, used for session storage in the database.

## Tests

To run tests, ensure that you have a testing framework such as `pytest` or `unittest` set up in your environment. The project includes tests for session creation, expiration, and destruction.

1. **Run tests using `pytest`**:
   ```bash
   pytest
   ```

This will run all the tests and show results for each.

## Contributing

If you'd like to contribute to this project, feel free to fork the repository, make changes, and submit a pull request. Here's how you can contribute:

1. Fork the repository.
2. Create a new branch.
3. Implement your changes or fix bugs.
4. Run tests to ensure everything works as expected.
5. Submit a pull request.

## Author

- **Name**: Harrison Eze
- **Username**: harystyleseze
- **GitHub Profile**: [https://github.com/harystyleseze](https://github.com/harystyleseze)

## License

This project is licensed under the MIT License.
```
