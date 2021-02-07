# My Site

A test Django site for development purposes. Once set up, it can be found at:
`http://localhost`.

- [Features in Consideration](#features-in-consideration)
- [Overview](#overview)
  - [Frontend Site](#frontend-site)
  - [API](#api)
  - [Admin Site](#admin-site)
- [Development](#development)
  - [Dependencies](#dependencies)
  - [Installation](#installation)
    - [Backend](#backend)
    - [Frontend](#frontend)
  - [Creating Sample Data](#creating-sample-data)
  - [Tests](#tests)
  - [Django Shell](#django-shell)


## Features in Consideration

The site is now heading in the direction of a film review website, à la [Rotten
Tomatoes](https://www.rottentomatoes.com/). Here are some proposed plans for it:

- Models for cast and crew.
- Recommendations based on film tags? Could be cool to combine this with 
  [Netflix](https://www.netflix.com) style machine learning in order to
  recommend films to see (and review) to users.
- Weighting review search results based on user preferences, for both film tags
  and most-visited reviewers. An extension of the second point.
- Possibly considering changing to TypeScript for the front as I'm already
  seeing the benefits of typing. Also might switch from [Material-UI](https://material-ui.com/)
  to [React Bootstrap](https://react-bootstrap.github.io/). Still looking for
  viable toolkits as I'm not sure I get on with _Material-UI_'s styling choices.


## Overview

### Frontend Site

Currently, only the development version exists, so once the frontend server is
started, per the instructions below, the frontend site can be found at 
`http://localhost:3000`. This is automatically opened in a browser on the 
server startup.

### API

The API can be accessed at `http://localhost/api`, either in-browser or via
the console.

### Admin Site

The admin site, for managing your data, can be found at `http://localhost/admin` 
and can be accessed using your superuser credentials.


## Development

### Dependencies

- Docker (19.03.8)
- docker-compose (1.25.0)
- Nodejs (v10.19.0)

**Note: Any `make` commands involving _docker-compose_ may require `sudo` 
(assuming Linux or macOS), depending on your local setup.**

### Installation

First, set up the `.env` file with:
```
make env
```

To build the Docker images, run the following:
```
make build
```

To spin up the containers, run:
```
make up
```

#### Backend

To make migration files, run:
```
make make-migrations
```

To migrate the database, run:
```
make migrate
```

To collect static assets, run:
```
make collect-static
```

#### Frontend

To install necessary node modules, run:
```
make install-ui-modules
```

To start the React development server, run:
```
make start-ui-server
```

### Creating Sample Data

To create an admin account, run:
```
make create-super-user
```

To add sample data to your database, run:
```
make create-sample-data
```

To create a fresh selection of sample data (wiping your existing data, except 
any staff or superuser profiles), run:
```
make flush-and-create-sample-data
```

### Tests

To run the Django test suite, use:
```
make test
```

### Django Shell

To interact with your data via Django's shell, run:
```
make shell
```
