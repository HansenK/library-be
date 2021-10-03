# library-be

## Getting Started

1. Clone the repo: `git clone git@github.com:HansenK/library-be.git`
2. Create a virtual environment: `virtualenv -p python3.8 venv`
3. Start the virtual environment: `source venv/bin/activate`
4. Installl the requirements: `pip install -r requirements.txt`
5. Applying migrations and sync database (creating tables): `python3 manage.py migrate --run-syncdb`
6. Run the app: `python3 manage.py runserver`

---

### Virtual environment

> Virtualenv creates new isolated environments to isolate your Python files on a per-project basis. This will ensure that any changes made to your website won’t affect other websites you’re developing.

- To create the virtual env: `virtualenv -p python3.8 venv`
- To activate the virtual env: `source ./bin/activate`
- To deactivate anytime, just run: `deactivate`
