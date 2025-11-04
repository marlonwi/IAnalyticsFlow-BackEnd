import psycopg2
from domain.repositories.query_repository import QueryRepository
from infrastructure.config.settings import settings

class PostgresQueryRepository(QueryRepository):
    def __init__(self):
        self.config = {
            "host": settings.db_host,
            "database": settings.db_name,
            "user": settings.db_user,
            "password": settings.db_password,
            "port": settings.db_port
        }

    def run(self, sql: str):
        with psycopg2.connect(**self.config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql)
                print(sql)
                cols = [desc[0] for desc in cur.description]
                rows = [dict(zip(cols, row)) for row in cur.fetchall()]
                return {"columns": cols, "rows": rows}
