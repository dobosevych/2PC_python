# 2PC 
2PC python implementation
## DB initialization
```
docker pull postgres
docker run --name postgresql-container -p 5432:5432 -e POSTGRES_PASSWORD=somePassword -d postgres --max_prepared_transactions=100
PGPASSWORD=somePassword psql -U postgres -h localhost < init.sql
```
## Application
```
pip3 install -r requirements.txt
python3 app.py
```