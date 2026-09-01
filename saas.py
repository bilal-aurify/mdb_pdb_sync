import os
from common_sync import run_migration


def run():
    """Full sync: Mongo DB (SAAS) -> Postgres DB (SAAS)"""
    run_migration(
        name="saas",
        mongo_uri=os.getenv("MONGO_URI_SAAS"),
        mongo_db_name=os.getenv("MONGO_DB_SAAS"),
        pg_host=os.getenv("PG_HOST_SAAS", "localhost"),
        pg_port=int(os.getenv("PG_PORT_SAAS", 5432)),
        pg_database=os.getenv("PG_DATABASE_SAAS"),
        pg_user=os.getenv("PG_USER_SAAS", "postgres"),
        pg_password=os.getenv("PG_PASSWORD_SAAS"),
        initial_run=os.getenv("INITIAL_RUN_SAAS", "false").lower() == "true",
    )


if __name__ == "__main__":
    run()