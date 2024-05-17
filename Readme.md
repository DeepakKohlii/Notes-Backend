# Note API

This is an API for creating and updating notes.

The backend is published on railway.

## Setup

1. Clone the repository:
    ```bash
    git clone <repository_url>
    ```

2. Navigate to the project directory:
    ```bash
    cd <project_directory>
    ```

3. Install the requirements:
    ```bash
    pip install -r requirements.txt
    ```

4. Run migrations:
    ```bash
    python manage.py migrate
    ```

5. Start the server:
    ```bash
    python manage.py runserver
    ```

## API Endpoints

- `POST /api/register/`: Register a new user.
    - Request body: `{ "username": "<username>", "password": "<password>" }`
    - Response: The created user object.

- `POST /api/token/`: Obtain a token for a registered user.
    - Request body: `{ "username": "<username>", "password": "<password>" }`
    - Response: `{ "token": "<token>" }`

- `POST /api/notes/`: Create a new note.
    - Request body: `{ "title": "<title>", "content": "<content>" }`
    - Response: The created note object.

- `PUT /api/notes/<note_id>/`: Update an existing note.
    - Request body: `{ "title": "<title>", "content": "<content>" }`
    - Response: The updated note object.

- `DELETE /api/notes/<note_id>/`: Delete a note.
    - Response: HTTP 204 No Content on success.

## Running Tests

To run the tests, use the following command:

```bash
python manage.py test
