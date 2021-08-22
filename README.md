# Flask REST API Starter

A flexible Python Flask REST API starter kit with testing, postgreSQL integration and example data model.

## Getting started:

**Step 1:** Clone the repository and cd into the root directory

**Step 2:** Install and start PostgreSQL (I use [Postgres.app](https://postgresapp.com/) but any local PostgreSQL server should work)

**Step 3 - Option 1:**

Create a .env file with the following contents:

```
source venv/bin/activate
export FLASK_APP="run.py"
export SECRET="super-secret-long-security-phrase"
export FLASK_ENV="development"
export DATABASE_URL="postgresql://localhost/flask_db"
```

Then run the following on the command line to start the virtual environment and add the environment variables at the same time:

```
source .env
```

**Step 3 - Option 2:**

start the virtual environment by running the following in your terminal:

```
source venv/bin/activate
```

After the virtual environment has started you need to add some basic environment varables by running the following:

```
export FLASK_APP="run.py"
export SECRET="super-secret-long-security-phrase"
export FLASK_ENV="development"
export DATABASE_URL="postgresql://localhost/flask_db"
```

**Step 4:**

From inside the virtual environment run the following to install the packages you need to run the application:

```
pip install -r requirements.txt
```

**Step 5:**

Lastly, create two databases, one is for the app and the other is for unit testing (we are using postgres for the database)

```
createdb flask_db
createdb test_db
```

Then run: 

```
flask db upgrade
```

Note: check the [Flask-Migrate](https://flask-migrate.readthedocs.io/en/latest/) documentation to understand other commands used to manage database and schema migrations.

## Starting the application

Run `flask run` to start the application on your localhost.

## Running the tests

The tests reside in the tests folder and each test name should begin with a `test_` such as `test_post.py`

```
python -m unittest
```

The results should look like this:

```
.....
----------------------------------------------------------------------
Ran 5 tests in 0.197s

OK
```