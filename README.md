# MyFamily

## Install the App for Development

### Requirements

- `python3.9`

```bash
brew install python@3.9
```

- `npm`

```bash
npm install -g npm
```

### Setting Up the app

1. Create a python3.9 virtual environment

```bash
python3.9 -m venv env
```

2. Activate the virtual envrionment

```bash
# For Linux/MAC Users
source env/bin/activate
# Windows users
env\Scripts\activate
```

3. Install Python packages in the virtual environment

```bash
pip install -r requirements.txt
```

4. Install frontend node_modules

```bash
cd frontend
npm install
```

5. Create a `.env` file with a Django SECRET_KEY and the DEBUG boolean. Here is [a Django SCRET_KEY generator](https://djecrety.ir/).

```
SECRET_KEY=<your_secret_key_generated>
DEBUG=<True (only for development)>
```

**Happy Coding !**

## During Development

- Backend server:

```bash
python manage.py runserver
```

- Frontend server:

```bash
cd frontend
npm start
```

## Link Django and React

In order to link Django and React (having react frontend on the django server), run `npm run build` to get all the files that will be used by Django to render React Views.
