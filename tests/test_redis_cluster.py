import os

import pytest
from redis.cluster import RedisCluster, ClusterNode
from redis.exceptions import RedisClusterException


@pytest.fixture(scope="module")
def redis_client(request):
    startup_nodes = [
        ClusterNode("redis-node-1", 6379),
        ClusterNode("redis-node-2", 6379),
        ClusterNode("redis-node-3", 6379),
    ]
    client = None
    # username = request.param["username"]
    # password = request.param["password"]
    try:
        client = RedisCluster(startup_nodes=startup_nodes,
                              decode_responses=True,
                              # password=os.getenv("REDIS_CLUSTER_PASSWORD"))
                              username=os.getenv("REDIS_CLUSTER_TEST_USERNAME"),
                              password=os.getenv("REDIS_CLUSTER_TEST_PASSWORD"))
                              # username=username,
                              # password=password)
        client.ping()
        yield client
    except RedisClusterException as e:
        pytest.skip(f"Skipping tests: Redis Cluster unavailable - {e}")
    finally:
        if client is not None:
            # client.flushdb()
            client.close()


# @pytest.mark.parametrize("redis_client", [
#     {"username": os.getenv("REDIS_CLUSTER_APP_USERNAME"), "password": os.getenv("REDIS_CLUSTER_APP_PASSWORD")},
#     {"username": os.getenv("REDIS_CLUSTER_TEST_USERNAME"), "password": os.getenv("REDIS_CLUSTER_TEST_PASSWORD")},
# ], indirect=True)
def test_sample_key(redis_client):
    key = "test_key"
    value = "test_value"

    redis_client.set(key, value)
    assert redis_client.get(key) == value

    redis_client.delete(key)


# @pytest.mark.parametrize("redis_client", [
#     {"username": os.getenv("REDIS_CLUSTER_APP_USERNAME"), "password": os.getenv("REDIS_CLUSTER_APP_PASSWORD")},
#     {"username": os.getenv("REDIS_CLUSTER_TEST_USERNAME"), "password": os.getenv("REDIS_CLUSTER_TEST_PASSWORD")},
# ], indirect=True)
def test_key_deleted(redis_client):
    key = "test_key"
    assert redis_client.get(key) is None
