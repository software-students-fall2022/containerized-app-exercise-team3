![Machine Learning Client Build & Test](https://github.com/software-students-fall2022/containerized-app-exercise-team3/actions/workflows/ml-client.yaml/badge.svg)
[![Web App Build & Test](https://github.com/software-students-fall2022/containerized-app-exercise-team3/actions/workflows/web-app.yml/badge.svg)](https://github.com/software-students-fall2022/containerized-app-exercise-team3/actions/workflows/web-app.yml)

# Containerized App Exercise

## Team Members
[Yvonne Wu (Yiyi Wu)](https://github.com/Yvonne511)

[Larry Li](https://github.com/86larryli)

[Winston Zhang](https://github.com/Midas0231)

[Evan Huang](https://github.com/EV9H)

[Harvey Dong](https://github.com/junyid)

[Otis Lu](https://github.com/OtisL99)

[Lucy Kocharian](https://github.com/Lkochar19)

## Usage

### Create `.env` File

In `machine-learning-client/` and `web-app/`, create separate `.env` files as instructed.

### Machine Learning Client

For detailed instructions on running the machine-learning client, see [`machine-learning-client/README.md`](./machine-learning-client/README.md).

### Web App Without Using Containers

For detailed instructions on running the web app *without using containers*, see [`web-app/README.md`](./web-app/README.md).

### Web App Using Containers

In the project root directory, where `docker-compose.yaml` is, run:

    docker compose up

This will start 2 containers:

- web app container, on port 5001 on your machine

- mongodb container, on port ***37017*** on your machine (NOT default 27017)

You can verify that both containers are up and running using command:

    docker container ls

#### Insert Sample Data into Database

We highly recommand injecting sample data into the database by using [`mongoimport`](https://www.mongodb.com/docs/database-tools/mongoimport/).

Run `mongoimport` from the system command line, not the `mongosh` shell.

In the project root directory, **while the mongodb container is running**, run:

    mongoimport --uri "mongodb://localhost:37017/awstranscribe?retryWrites=true&w=majority" --collection=jobs --file=data/sample_data.json --jsonArray

Then you can see the web app with sample data running at http://localhost:5001/.

### Testing

### Machine Learning Client

In `machine-learning-client/`, while the mongodb container is running, run:
    
    python3 -m pytest

To see coverage report, run:

    coverage run -m pytest

    coverage report

### Web App

Stop the currently running web-app container while keeping the mongodb container by running command:

    docker container stop containerized-app-exercise-team3-webapp-1

Change `MONGO_URI` in `web-app/.env` to `MONGO_URI="mongodb://localhost:37017/awstranscribe?retryWrites=true&w=majority"`.

In `web-app/` run:
    
    python3 -m pytest

To see coverage report, run:

    coverage run -m pytest

    coverage report