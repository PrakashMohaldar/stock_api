## 1. Make a `.env` file and add following details
### 1. Database used Neon postgres
   ```plaintext
   PGHOST=<Link>
   PGDATABASE=<db>
   PGUSER=<user>
   PGPASSWORD=<pgpuser>
   PGPORT=<portnumber>
   ```
### 2. Change 
 ```plaintext
  <Link> <db> <user> <pgpuser> <portnumber>
  ```

## 2. Running the server

### 1. installing the dependecies
    ```bash
        pip install -r requirements.txt
    ```
### 2. appling migrations
    ```bash
        python manage.py migrate
    ```
### 3. run the development server
    ```base
        python manage.py runserver
    ```

## 3. Api Endpoints

### 1. CRUD operations
```plaintext
GET http://127.0.0.1:8000/api/stocks/
POST http://127.0.0.1:8000/api/stocks/

GET http://127.0.0.1:8000/api/stocks/<id>/
PUT http://127.0.0.1:8000/api/stocks/<id>/
POST http://127.0.0.1:8000/api/stocks/<id>/
PATCH http://127.0.0.1:8000/api/stocks/<id>/
```

### 2. post, put, patch request input json format
```json
    {
        "name": "Apple Inc.",
        "ticker_symbol": "AAPL",
        "price": 175.00
    }
```

