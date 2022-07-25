# Gereedschapvoordetuin API

## Vereisten

- Docker
- Python 3.9
- PostgreSQL

## Tools

- Pycharm
- DataGrip

## Getting Started

1. Maak een virtual environment aan met Python 3.9
2. Install de benodigde packages: `pip install -r requirements.txt`
3. Maak een docker omgeving aan met een postgres database: `docker run --name gereedschapvoordetuin_db -e POSTGRES_PASSWORD=<password> -e POSTGRES_DB=gereedschapvoordetuin -e POSTGRES_USER=<username> -d -p 5433:5433 postgres`
4. Maak een .env bestand aan binnen de root van het project
5. Vul het .env bestand met het volgende:
```
DATABASE_NAME=gereedschapvoordetuin
DATABASE_HOST=localhost
DATABASE_PORT=5433
DATABASE_USER=<username>
DATABASE_PASSWORD=<password>
SECRET_KEY=<secret_key>
```
6. Maak de database tabellen aan: `python manage.py migrate`
7. Maak een admin account aan: `python manage.py createsuperuser --username <username> --email <email>`
   1. Maak een wachtwoord aan die je kan onthouden
8. Maak een authenticatie token aan: `python manage.py drf_create_token <username>`
9. Run de applicatie: `python manage.py runserver`
10. Database vullen (LET OP dit duurt een tijdje):
- `python manage.py update_products --all`
