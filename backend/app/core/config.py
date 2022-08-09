from pydantic import BaseSettings


class Settings(BaseSettings):
    # project settings
    PROJECT_NAME: str = "IAM"
    API_V1_STR: str = "/api/v1"

    # neo4j server settings
    GRAPH_DB_USER: str
    GRAPH_DB_PASSWORD: str
    GRAPH_DB_HOST: str
    GRAPH_DB_PORT: int

    # cypher query settings
    LOG_NODE_NAME: str = "log"
    LOG_NODE_LABEL: str = "Log"


settings = Settings()
