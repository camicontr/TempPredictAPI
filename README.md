# TempPredictAPI

## Introduction 
This is the repository for the Next Hour Temperature Prediction API using RNN with GRU units. The input is a list with the temperature values of the last 30 hours and the end date of these.

## Depedencies
Dependencies for Docker:
- [docker](https://www.docker.com/)
- [docker-compose](https://docs.docker.com/compose/install/)

## Installation
### Clone the repository
First you need to clone the repository.

```bash
git clone https://github.com/camicontr/TempPredictAPI.git
```

### Docker Installation
To install TempPredictAPI on a docker container, run the following command:

```bash
docker-compose up -d --build
```

## Usage
### Running the API
To run the API in the Docker container, run the following command:

```bash
docker start container_API
```

then go to

```bash
http://localhost:8000/predict
```
