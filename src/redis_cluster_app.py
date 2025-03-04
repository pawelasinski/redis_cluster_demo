import logging
import time
import os

from redis.cluster import ClusterNode, RedisCluster
from redis.exceptions import RedisClusterException

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("logs/redis_cluster_app.log", mode="w"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


def main():
    startup_nodes = [
        ClusterNode("redis-node-1", 6379),
        ClusterNode("redis-node-2", 6379),
        ClusterNode("redis-node-3", 6379),
    ]

    try:
        logger.info("Connecting to Redis Cluster...")
        r = RedisCluster(startup_nodes=startup_nodes,
                         decode_responses=True,
                         # password=os.getenv("REDIS_CLUSTER_PASSWORD"))
                         username=os.getenv("REDIS_CLUSTER_APP_USERNAME"),
                         password=os.getenv("REDIS_CLUSTER_APP_PASSWORD"))
        logger.info("Successfully connected to Redis Cluster.")

        logger.info("Setting key...")
        r.set("greeting", "Hello from Redis Cluster!")

        logger.info("Retrieving value for key...")
        value = r.get("greeting")
        logger.info(f"Retrieved value: `greeting` = `{value}`")

    except RedisClusterException as rds_clstr_e:
        logger.error(f"Redis Cluster error: %s", rds_clstr_e)
    except Exception as e:
        logger.error("Unexpected error: %s", e)

if __name__ == "__main__":
    logger.info("Starting application...")
    time.sleep(10)
    main()
    logger.info("Application finished.")
