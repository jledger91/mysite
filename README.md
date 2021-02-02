# My Site
A test Django site for development purposes. Once set up, it can be found at:
`http://localhost`.

- [Installation](#installation)
- [Admin Site](#admin-site)

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

To collect static assets, run:
```
make collectstatic
```

## Admin Site
The admin site, for managing your data, can be found at `http://localhost/admin` 
and can be accessed using your superuser credentials.
