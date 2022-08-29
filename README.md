# TempPredictAPI

## Introduction 
This is the repository for the Next Hour Temperature Prediction API using RNN with GRU units. With the last 30 temperature values, the temperature for the next hour is predicted with a root mean square error of 0.4 °C.

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
http://localhost:8000/docs
```
