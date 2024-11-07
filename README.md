# User Management Service

This is a user management REST API service built with Flask and Firebase Firestore, designed to manage users and applications in a secure and isolated manner. Each application can store and access only the data it has saved, while the service admin can manage tokens for each application.

## Features

- **User Management**: Create, update, delete, and retrieve user data specific to each application.
- **Token-based Application Isolation**: Each application has its own token, and it can only access the data it has saved.
- **Admin Control**: Admin can add, update, and delete tokens for different applications.
- **Firestore Integration**: Uses Firebase Firestore to store user and application data.

## Requirements

- Python 3.12 or later
- Firebase credentials (`credentials.json`)
- Flask and additional libraries (see below)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/
    razmazlih/UserManager.git
    cd your-repo-name
    ```

2. Create and activate a virtual environment:

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Set up Firebase credentials:
    - Download the `credentials.json` file from the Firebase Console (in the Service Accounts section).
    - Place `credentials.json` in the root of the project folder.
    - Set the path to `credentials.json` in the `.env` file:

      ```text
      FIREBASE_CREDENTIALS_PATH="credentials.json"
      ```

5. Configure environment variables in a `.env` file:

    ```text
    ADMIN_TOKEN="your_admin_token"
    FIREBASE_CREDENTIALS_PATH="credentials.json"
    CORS_ORIGINS="*"  # Allowed origins, e.g., "https://example.com"
    CORS_SUPPORTS_CREDENTIALS=True
    ```

## Running the Service

To start the Flask development server, run:

```bash
python run.py