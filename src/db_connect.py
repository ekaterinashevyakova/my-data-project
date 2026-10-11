import os
from contextlib import closing

import psycopg2


def main():
    password = os.environ.get("PGPASSWORD")
    if not password:
        raise SystemExit("Set PGPASSWORD before running this script.")

    try:
        with closing(psycopg2.connect(
            host=os.environ.get("PGHOST", "localhost"),
            database=os.environ.get("PGDATABASE", "gtm_intelligence"),
            user=os.environ.get("PGUSER", "postgres"),
            password=password,
            port=os.environ.get("PGPORT", "5432"),
            connect_timeout=10,
        )) as conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT 1")
                if cursor.fetchone() != (1,):
                    raise SystemExit("Database connection check failed.")
        print("Connected successfully!")
    except psycopg2.Error:
        raise SystemExit(
            "Database connection failed. Check your PostgreSQL service "
            "and PG environment variables."
        ) from None


if __name__ == "__main__":
    main()
