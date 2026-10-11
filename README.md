# GTM Reddit Intelligence

**Status: In progress**

A Python and PostgreSQL project exploring how Reddit-style post data can support business analysis. The goal is to clean text data and develop insights relevant to customer feedback, product positioning and go-to-market decisions.

## Current implementation

- **Text preprocessing with Pandas:** `src/cleaning.py` reads `raw_data.csv`, converts the `post` column to lowercase, removes leading and trailing whitespace, and exports `cleaned_data.csv`.
- **Initial PostgreSQL schema:** `sql/schema.sql.txt` defines tables for raw posts, cleaned posts, keywords and insights.
- **Database connection:** `src/db_connect.py` reads PostgreSQL settings from environment variables, checks connectivity with `SELECT 1`, and closes the connection.
- **Sample data:** the root CSV contains three example posts and their like counts. This sample supports development; it is too small to support general business conclusions.

## Tools

Python · Pandas · SQL · PostgreSQL · psycopg2 · Git · GitHub

## Repository structure

- `raw_data.csv` — sample input used by the cleaning script.
- `src/` — Python scripts for preprocessing and database connectivity.
- `sql/` — initial database schema.
- `data/` — data files.
- `reports/` — intended location for analytical outputs.

## Run the text-cleaning step

From the repository root, with Python and Pandas installed:

```bash
python src/cleaning.py
```

The script writes `cleaned_data.csv` to the repository root. This step runs independently of PostgreSQL.

## PostgreSQL connection

Set `PGPASSWORD` in your local environment before running `python src/db_connect.py`. Optional variables are `PGHOST`, `PGDATABASE`, `PGUSER` and `PGPORT`. Local `.env` files are ignored by Git but are not automatically loaded by this script. Never commit real credentials.

## Next development steps

- Expand and document the dataset, including its source and limitations.
- Connect preprocessing to database loading and add data-quality checks.
- Develop SQL analysis and visualisations of feedback themes and engagement.
- Document findings, limitations and potential business implications.

These are planned extensions. The current repository demonstrates preprocessing and an initial database structure; analytical findings are not yet reported.
