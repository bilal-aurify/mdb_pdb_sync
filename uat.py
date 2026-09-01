import os
from common_sync import run_migration


def run():
    """Full sync: Mongo DB (UAT) -> Postgres DB (UAT)"""
    run_migration(
        name="uat",
        mongo_uri=os.getenv("MONGO_URI_UAT"),
        mongo_db_name=os.getenv("MONGO_DB_UAT"),
        pg_host=os.getenv("PG_HOST_UAT", "localhost"),
        pg_port=int(os.getenv("PG_PORT_UAT", 5432)),
        pg_database=os.getenv("PG_DATABASE_UAT"),
        pg_user=os.getenv("PG_USER_UAT", "postgres"),
        pg_password=os.getenv("PG_PASSWORD_UAT"),
        initial_run=os.getenv("INITIAL_RUN_UAT", "false").lower() == "true",
    )


if __name__ == "__main__":
    run()