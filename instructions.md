# Containerized App Exercise

Build a containerized app made up of multiple subsystems, each operating in a container.

## Concept

Containers are small-footprint, portable, isolated environments within which applications can run.

In this exercise, you will create a system consisting of three separate but internetworked [Docker](https://docker.com) containers.

## Requirements

The system you will build consists of three independent software sub-systems:

- a **machine learning client** - a program that performs one more more machine learning tasks on data collected from camera, microphone, or other sensor(s)
- a **web app** - an interface through which web visitors can see the activity and analytical results of the machine learning client
- a **database** - stores the data used by both other parts

A few notes:

- **What to include in this repository**: Code for the machine learning client and web app parts of this system must be stored in this "monorepo" - a single version control repository housing multiple independent subsystems of a single software project. The mongodb database will be run from mongodb's own container image, so will not be stored here, but any instructions for setting it up, running it, and populating it with starter data (if necessary) must be mentioned in the `README.md` file.
- **What not to include in this repository**: A starter `.gitignore` file has been provided for generic Python programming. However, this should be updated as necessary to make sure that any 3rd-party libraries, modules or other dependencies used by any part of this system are not included in version control. Use `pip` or `pipenv` to document and install any 3rd-party Python software dependencies for both parts independently.
- **How to start all your containers at once**: Eventually, you must start all your system's containers together using [docker-compose](https://docs.docker.com/compose/) - a tool for starting and configuring multiple docker containers that together are necessary to run a system. However, it recommended to start running each with its own `docker` commands at first until things are more-or-less working as expected, and then integrate `docker-compose` once all parts of your system are running as expected.

More details on each subsystem follow.

### Database

The other two parts of your application will depend upon a [MongoDB](https://mongodb.com) database, run within a Docker container. At a minimum, the machine learning client will store the data it collects in this database, and the web app will read from it. You are welcome to use this database for any other duties that befit your application.

See documentation for running [MongoDB within Docker](https://www.mongodb.com/compatibility/docker). Here is a simple example of how to run a MongoDB container with `docker`:

```bash
docker run --name mongodb -d -p 27017:27017 mongo
```

### Machine learning client

The machine learning client will be written in Python and will connect to the database using [pymongo](https://pymongo.readthedocs.io/en/stable/).

- The client device must collect data using one or more available hardware sensors, such as camera, microphone, gps, or any additional sensors the development team has access to.
- The client device must do some form of high-level analysis of the data, such as image recognition, speech recognition, classification, aggregation, etc, either using custom code, third-party APIs or code libraries designed for this purpose. In other words, the client device must not only collect raw data, but also must compute the results of some additional analysis of that data.
- Metadata about the collected data, including the results of any analysis performed, must be saved to the database. How frequently the client communicates with the database must make sense for your application.
- Unit tests using [pytest](https://docs.pytest.org/en/7.2.x/) must be written for the client device code that provide at least 50% code coverage of the client code.
- The client must have a Continuous Integration (CI) workflow using [GitHub Actions](https://github.com/features/actions) that automatically builds and tests the updated client subsystem every time a pull request is approved and code is merged into the `main` branch.
- Like the other parts, the machine learning client must run within its own Docker container.
- Put all code for this subsystem within the `machine-learning-client` subdirectory of this repository.

### Web app

The web app allows visitors on the web to view the activity of the machine learning client and the results of its analysis.

The web app must be built using the Python [flask](https://palletsprojects.com/p/flask/) framework and will connect to the database via `pymongo`, with any additional modules or libraries that you would like.

- The server must store the data received in a database and provide a web dashboard for users to visualize the data.
- Unit tests using `pytest`and [pytest-flask](https://pytest-flask.readthedocs.io/en/latest/) must be written for the web app code that provide at least 80% code coverage of the server code.
- The web app must have a Continuous Integration / **Continuous Deployment** (CI/**CD**) workflow using [GitHub Actions](https://github.com/features/actions) that automatically builds, tests, and deploys the updated server subsystem every time a pull request is approved and code is merged into the `main` branch.
- Like the other parts, the web app must run within its own Docker container.
- Put all code for this subsystem within the `web-app` subdirectory of this repository.

## Developer workflow

Teams are expected to follow a roughly "agile"-style development workflow, with the following specific requirements.

### Task boards

ALl teams must use task boards to provide insight into the status of all work.

- The task boards must have at least 4 columns: "To Do", "In Progress", "Awaiting Review", "Done".
- Teams must represent all work to be done as discrete tasks on the task board, where each task represents about one day's work for one team member.
- Each task must be assigned to the developer(s) responsible for implementing it.
- Each task must be positioned on the board in the appropriate column representing its status.

### Standup meetings

Each team must have at least 3 standup meetings per week. In these meetings, each developer must answer three questions:

- what have you done since last meeting?
- what are you working on now?
- is anything blocking your way?

One team member must collect the answers each team member gave to each of these questions and post a report of the standup to the team's communication channel. For example:

```
Standup Report - January 24 2023
--------------------------------

Flora Rosenkrist @florarose
- did: implemented upload selfie functionality
- doing: debugging the tensorflow model
- blockers: none

Chad Mugabe @chmug
- did: taking camera photos every 1 second using opencv
- doing: integrating pytorch with flask
- blockers: none

Trish McPerson @tmcfer
- did: finished user and edit profile
- doing: working on the background image issue
- blockers: just diagnosed with covid + midterm - out till Monday

Pat Sachin @patsach
- did: map page, merged trish's pull request. refactored audio recording stuff
- doing: selfie popup, map api integration
- blockers: none
```

### Individual contributions

All team members must have visibly contributed to the code using their own git & GitHub accounts in order to claim that they contributed to the project.

### Feature branch workflow

All code changes must be done in feature branches and not directly in the `main` branch.

To merge code from a feature branch into the `main` branch, do the following:

1. Create a pull request from the feature branch to the `main` branch.
1. Ask a fellow developer to review your code.
1. The reviewer must review the code and run unit tests to verify that the functions behave as expepcted.
1. If the reviewer has any concerns, discuss then and make any changes agreed upon.
1. Merge the pull request into the `main` branch.
1. Delete the feature branch.
1. Pull the latest changes from the remote `main` branch to your local `main` branch.

**Warning**: the longer you let code sit in a feature branch, the more likely your team is to end up in [merge hell](https://en.wikipedia.org/wiki/Merge_hell). . Merge feature branches into `main` often to avoid this fate.

## Documentation

Replace the contents of the [README.md](./README.md) file with a beautifully-formatted Markdown file including

- a plain-language **description** of your project, including:
- two [badges](https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/adding-a-workflow-status-badge) at the top of the `README.md` file showing the result of the latest build/test workflow of the server both the machine learning client and web app subsystems.
- the names of all teammates as links to their GitHub profiles in the `README.md` file.
- instructions for how to configure and run all parts of your project for any developer on any platform - these instructions must work!
- instructions for how to import any starter data into the database, if necessary for the system to operate correctly at first.
