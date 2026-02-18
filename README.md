# RMOS Sprint 1 Prototype

## Prerequisites
- Docker and Docker Compose v2
- Copy `.env.example` to `.env` and set secure values

## Build and run
$ docker compose up --build

Services:
- Frontend: http://localhost (customer UI at /index.html, tablet at /tablet.html)
- Backend API: http://localhost:8000
- Postgres: internal service 'db'

## Verify end-to-end
1. Open http://localhost (customer UI). Add items and click "Place Order".
2. Open http://localhost/tablet.html (waiter UI). Pending order should appear within a few seconds.
3. Click "Accept" on the waiter UI. Backend audit table will record `order_created` and `order_accepted`.

## DB access (dev)
To inspect DB:
$ docker compose exec db psql -U ${POSTGRES_USER} -d ${POSTGRES_DB}
SELECT * FROM orders;
SELECT * FROM audit;

## Notes and next steps
- Authentication is a simple stub; replace with JWT/session in Sprint 2.
- Secrets must be rotated and stored securely (Docker secrets or vault) before production.
- Add TLS termination and production process manager (gunicorn) in next sprint.



#
### NOTAR ISA ajuste en requirements.txt

el original
```
fastapi==0.95.2
uvicorn[standard]==0.22.0
SQLAlchemy==2.0.19
psycopg2-binary==2.9.7
python-dotenv==1.0.0
passlib[bcrypt]==1.7.4
itsdangerous==2.1.2
```

Hubo que cambiar librerías añadiendo -- cambia dependencias
 
```
fastapi==0.95.2
uvicorn[standard]==0.22.0
SQLAlchemy==2.0.19
psycopg2-binary==2.9.7
python-dotenv==1.0.0
itsdangerous==2.1.2


bcrypt==3.1.7
passlib==1.7.4
```


http://localhost/

http://localhost/tablet.html.
