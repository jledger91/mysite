# My Site
A test Django site for development purposes. Once set up, it can be found at:
`http://localhost:8000`.

## Installation
First, set up the `.env` file with:
```
make env
```

To build the Docker images, run the following:
```
docker-compose build
```

To spin up the containers, run:
```
docker-compose up
```

To migrate the database, run:
```
make migrate
```

To create an admin account, run:
```
make createsuperuser
```
