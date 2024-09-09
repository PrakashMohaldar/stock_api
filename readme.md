## 1. Adding Database URL and Password to `.env`

To configure your PostgreSQL database, you need to set up the necessary environment variables in a `.env` file. Follow these steps to add the database connection details:

### 1.1. Create a `.env` File

1. In the root directory of your Django project (the same directory where `manage.py` is located), create a file named `.env` if it does not already exist.

2. Open the `.env` file in a text editor and add the following lines. Replace the placeholders with your actual database credentials:

3. Database used Neon postgres

   ```plaintext
   PGHOST=<Link>
   PGDATABASE=<db>
   PGUSER=<user>
   PGPASSWORD=<pgpuser>
   PGPORT=<portnumber>```

4. Change <Link> <db> <user> <pgpuser> <portnumber>

