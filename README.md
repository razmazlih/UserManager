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

4. Set up Firebase credentials as a single environment variable:
   - Open `credentials.json` and copy the entire contents.
   - Store it in an environment variable named `FIREBASE_CREDENTIALS_JSON` in your `.env` file:

      ```text
      FIREBASE_CREDENTIALS_JSON='{"type": "...", "project_id": "...", "private_key_id": "...", "private_key": "-----BEGIN PRIVATE KEY-----\\n...\\n-----END PRIVATE KEY-----\\n", ...}'
      ```

   - Ensure the private key includes `\\n` instead of actual newlines to store it properly in a single line within `.env`.

5. Configure additional environment variables in `.env`:

    ```text
    ADMIN_TOKEN="your_admin_token"
    CORS_ORIGINS="*"  # Allowed origins, e.g., "https://example.com"
    CORS_SUPPORTS_CREDENTIALS=True
    ```

## Firebase Initialization

In `app/utils/firebase.py`, Firebase is initialized by loading the JSON credentials directly from the `FIREBASE_CREDENTIALS_JSON` environment variable. The `private_key` is reformatted to include actual newlines before Firebase is initialized.

The code snippet used to initialize Firebase is as follows:

```python
import firebase_admin
from firebase_admin import credentials
import os
import json

def initialize_firebase():
    # Load JSON credentials from environment variable
    cred_data = json.loads(os.getenv('FIREBASE_CREDENTIALS_JSON'))

    # Replace \\n with actual newlines for the private key
    cred_data["private_key"] = cred_data["private_key"].replace('\\n', '\n')

    if not firebase_admin._apps:
        cred = credentials.Certificate(cred_data)
        firebase_admin.initialize_app(cred)