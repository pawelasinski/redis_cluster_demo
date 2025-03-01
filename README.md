# Redis Cluster Demo

This mini-project showcases how to set up, configure, and use **Redis Cluster** for distributed data storage and high availability. It includes examples of managing a cluster, connecting to it, and performing basic operations with Python, along with testing and logging.

## Features

- Setup of Redis Cluster with 6 nodes (3 masters and 3 replicas) using Docker and Docker Compose.
- Authentication using ACL (Access Control List) for secure access.
- Connection and operations using the `redis-py` Python client.
- Testing with `pytest` for verifying cluster functionality.

## Prerequisites

- Docker
- Docker Compose

## Installation and Execution

1. **Clone the repository**:
   ```bash
   git clone git@github.com:pawelasinski/redis_cluster_demo.git
   cd redis_cluster_demo
   ```

2. **Create and populate the `.env` and `conf/acl.conf` files**:
   ```env
   REDIS_CLUSTER_PASSWORD=<password1>

   REDIS_CLUSTER_DEFAULT_USERNAME=<username2>
   REDIS_CLUSTER_APP_USERNAME=<username3>
   REDIS_CLUSTER_APP_PASSWORD=<password3>
   REDIS_CLUSTER_TEST_USERNAME=<username4>
   REDIS_CLUSTER_TEST_PASSWORD=<password4>
   ```
   ```text
   user <username2> on nopass ~* +@all
   user <username3> on ><password3> ~* +@all
   user <username4> on ><password4> ~* +@read +@write +@keyspace +@dangerous +@connection +cluster
   ```
   Adjust the usernames and passwords as needed.

3. **Run the project**:
   ```bash
   docker compose up --build
   ```
   - The application (`redis-cluster-app`) will connect to the cluster and perform some trivial operations.
   - Tests (`redis-cluster-test`) will verify cluster functionality.

4. **Check the results**:
   - The `data/` folder will contain:
     - `node_1`, `node_2`, ..., `node_6` — directories with Redis Cluster data files (`appendonly.aof`, `dump.rdb`, `nodes.conf`, `acl.conf`).
   - The `logs/` folder will contain:
     - `redis_cluster_app.log` — logs from the application.
   - The `test_results/` folder will contain:
     - `pytest_results.txt` — results of the tests.

5. **Stop the containers**:
   ```bash
   docker compose down
   ```
   - To remove volumes as well, add the flag `--volumes`: `docker compose down --volumes`.

## Project File Structure

```text
redis_cluster_demo/
├── conf/                            # Configuration files
│   └── acl.conf                        # ACL configuration for Redis Cluster
├── data/                            # Data storage for Redis nodes (mounted as volumes)
│   ├── node_1/                         # Data for redis-node-1
│   ├── node_2/                         # Data for redis-node-2
│   ├── node_3/                         # Data for redis-node-3
│   ├── node_4/                         # Data for redis-node-4
│   ├── node_5/                         # Data for redis-node-5
│   └── node_6/                         # Data for redis-node-6
├── logs/                            # Logs (created automatically)
│   └── redis_cluster_app.log           # Application logs (created automatically)
├── src/                             # Application code
│   ├── Dockerfile                      # Dockerfile for the application
│   └── redis_cluster_app.py            # Python script to connect and operate on Redis Cluster
├── tests/                           # Test code
│   ├── Dockerfile                      # Dockerfile for tests
│   ├── pytest_results.txt              # Test results (created automatically)
│   └── test_redis_cluster.py           # Pytest tests for Redis Cluster
├── .env                             # Environment variables for credentials
├── .gitignore                       # Git ignore file
├── docker-compose.yml               # File for managing all services
├── LICENSE                          # Project license
├── README.md                        # Project description
└── requirements.txt                 # Python dependencies
```

## Example Logs

```
...
redis-cluster-app   | 2025-03-01 11:56:09,978 - INFO - Connecting to Redis Cluster...
redis-cluster-app   | 2025-03-01 11:56:10,021 - INFO - Successfully connected to Redis Cluster.
redis-cluster-app   | 2025-03-01 11:56:10,021 - INFO - Setting key...
redis-cluster-app   | 2025-03-01 11:56:10,023 - INFO - Retrieving value for key...
redis-cluster-app   | 2025-03-01 11:56:10,024 - INFO - Retrieved value: `greeting` = `Hello from Redis Cluster!`
redis-cluster-app   | 2025-03-01 11:56:10,024 - INFO - Application finished.
...
```

## Possible Project Extensions

- Add real-time monitoring of cluster health and metrics.
- Implement failover and recovery scenarios.
- Integrate with a web interface for cluster management.
- ...

## License

[MIT License](./LICENSE)

## Author

Pawel Asinski (pawel.asinski@gmail.com)
