# RPG Rest API

This repository is an example of using Django and Django Rest Framework to set up and Rest API for tracking RPG characters. The code here is used as an example through a series of posts on my blog [jimbarnes.dev](https://jimbarnes.dev/).

If you want a more in-depth discussion of the setup process, you can read through the first post here: [https://jimbarnes.dev/posts/django-rpg-api-part-1/](https://jimbarnes.dev/posts/django-rpg-api-part-1/). However, more succinct instructions are provided below.

## Setup

1. Clone this repository down into your machine: `git clone https://github.com/jmbarne3/rpgapi.git` and cd into the directory.
2. Create a virtual environment: `python -m venv .venv --prompt=rpgapi`. The `--prompt` flag is optional, but I like to name my virtual environments for easy reference.
3. Activate the virtual environment and install the dependencies: `source .venv/bin/activate && pip install .`.
4. If not using `sqlite`, set up your database and create your user account on PostgreSQL or MySQL.
5. Copy the `.env-template` file and name it `.env` and configure it accordingly.
6. Run the initial migrations: `python manage.py migrate`.
7. Run the server: `python manage.py runserver`.

### Configuration

The configuration items for the project need to be stored in a `.env` file when developing locally. The variables that need to be set are as follows:

| Variable Name | Description |
| --- | --- |
| SECRET_KEY | The key used to salt password hashes and other cryptographic information within your database. |
| DB_NAME | The name of the database file (if using SQLite) or the name of the database if using MySQL or PostgreSQL. |
| DB_USER | The user name to use when connecting to MySQL or PostgreSQL. Not needed if using SQLite. |
| DB_PASS | The password to use when connecting to MySQL or PostgreSQL. Not needed if using SQLite. |
| DB_HOST | The hostname to use when connecting to MySQL or PostgreSQL. Not needed if using SQLite. |
| DB_PORT | The port to use when connecting to MySQL or PostgreSQL. Not needed if using SQLite. |
