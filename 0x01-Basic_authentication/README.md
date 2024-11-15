# Basic Authentication

## Project Overview

This project is part of the ALX Backend Software Engineering curriculum. The goal of this project is to implement a basic authentication system for an API using Python. We will create a class `BasicAuth` which implements various authentication features like extracting base64-encoded authorization headers, decoding them, and verifying user credentials.

## Project Directory Structure

```plaintext
alx-backend-user-data/
├── 0x01-Basic_authentication/
│   ├── api/
│   │   ├── v1/
│   │   │   ├── auth/
│   │   │   │   ├── basic_auth.py
│   │   │   ├── app.py
│   ├── models/
│   │   ├── user.py
├── README.md
```

### **Directory Overview**
- **api/v1/auth/basic_auth.py**: Contains the implementation for the `BasicAuth` class.
- **models/user.py**: Defines the `User` model with methods for saving, searching, and verifying user credentials.
- **api/v1/app.py**: Initializes and runs the API server.
- **README.md**: This file.

## **Requirements**

- Python 3.x
- Flask (for API server)
- UUID (for generating unique user IDs)
- Base64 (for encoding and decoding authorization headers)

## **Functionality Overview**

This project implements basic authentication for an API with the following functionalities:

1. **Extract Base64 Authorization Header**  
   Extracts the base64 part from the `Authorization` header.

2. **Decode Base64 Authorization Header**  
   Decodes the base64 authorization header into a plain text string.

3. **Extract User Credentials**  
   Extracts the user’s email and password from the decoded string.

4. **User Object from Credentials**  
   Retrieves a `User` instance from a database of users using the provided email and password.

5. **Require Authentication**  
   Determines if authentication is required for a given path.

6. **Wildcard Path Matching**  
   Allows wildcard matching for excluded paths in the `require_auth` method.

## **Features Implemented**

1. **Basic Authentication**  
   The API is protected by basic authentication, meaning users must send an HTTP `Authorization` header with the correct credentials to access certain endpoints.

2. **User Management**  
   Users can be created with an email and password. These credentials are then stored and used for authentication.

3. **API Access Control**  
   Different endpoints have varying levels of access control. Some paths are excluded from authentication (e.g., `/api/v1/status`), while others require valid credentials.

4. **Base64 Encoding/Decoding**  
   Base64 encoding and decoding is used to securely send and verify user credentials through HTTP headers.

## **Installation**

1. **Clone the Repository**

   First, clone the repository to your local machine:

   ```bash
   git clone https://github.com/harystyleseze/alx-backend-user-data.git
   cd alx-backend-user-data/0x01-Basic_authentication
   ```

2. **Set Up the Environment**

   Make sure you have Python 3 installed. You can install dependencies using `pip`:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```

3. **Run the API**

   After setting up the environment, you can start the API server:

   ```bash
   python3 -m api.v1.app
   ```

   The API will be available at `http://0.0.0.0:5000`.

## **Usage**

1. **Basic Authentication**

   To access protected routes, send the `Authorization` header with the `Basic` authentication scheme:

   ```bash
   curl -H "Authorization: Basic <base64-encoded-email:password>" http://0.0.0.0:5000/api/v1/protected_route
   ```

2. **Creating a New User**

   You can create a user by providing an email and password. This is done in the code using the `User` model.

3. **Testing the Authentication**

   The authentication system is tested using multiple scripts like `main_1.py`, `main_2.py`, etc., which test extracting and decoding base64 headers, as well as verifying credentials.

   Example usage for checking status:

   ```bash
   curl "http://0.0.0.0:5000/api/v1/status"
   ```

   Example usage for accessing users:

   ```bash
   curl "http://0.0.0.0:5000/api/v1/users" -H "Authorization: Basic <base64-encoded-email:password>"
   ```

4. **Path Matching and Wildcards**

   The `require_auth` method supports wildcard matching for excluded paths. For example:

   - `/api/v1/stat*` would exclude paths like `/api/v1/stats` or `/api/v1/status`.
   - Other paths like `/api/v1/users` will require authentication.

## **Contributions**

If you want to contribute to this project, feel free to fork the repository and create a pull request with your changes. All contributions are welcome!

Steps to contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to your branch (`git push origin feature/your-feature`).
6. Open a pull request.

## **License**

This project is licensed under the MIT License.

## **Contact Information**

- **GitHub Profile**: [Harrison Eze](https://github.com/harystyleseze)
- **Email**: [harry.eze@domain.com](mailto:harry.eze@domain.com)

## **Acknowledgments**

- ALX Software Engineering program
- [Flask Documentation](https://flask.palletsprojects.com/)
- [Base64 Encoding Documentation](https://en.wikipedia.org/wiki/Base64)
- All contributors to open-source projects used in this repository
