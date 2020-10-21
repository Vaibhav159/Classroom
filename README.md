# Classroom

## Usage

1. clone the repository using `git clone "ssh/https https://github.com/Vaibhav159/Classroom".`
2. create a virtual environment using `virtualenv -p python3.8 venv` in linux terminal, see 'Dependencies' for platform specific instructions.
3. activate virtual environment using `source venv/bin/activate` in linux terminal, see 'Dependencies' for platform specific instructions.
4. install dependencies using `pip install -r requirements.txt`.

## Setup

1. Download Postgres DB or use Online Insantce of Postgres DB.
2. Create .env file in main Classroom folder(outer).
3. Fill the .env parameters as per the values.
4. Run commands in Run section to get started.

## Run

```python
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

### Head to

1. http://127.0.0.1:8000/questions
2. http://127.0.0.1:8000/details/{replace with question id}
3. http://127.0.0.1:8000/modules
4. http://127.0.0.1:8000/module/{replace with module id}
