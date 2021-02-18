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
  - [Starting the Site](#starting-the-site)
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
- npm (6.14.4)

### Installation

___

**For a quick install, run:**
```
make quick-install
```
_(You can skip directly to [starting the site](#starting-the-site) after this.)_
___

First, set up the `.env` file with:
```
make env
```

To build the Docker images, run the following:
```
make build
```

#### Backend

___
**To install the backend in one go, run:**
```
make install-backend
```
_(You can skip directly to [installing the frontend](#frontend) after this.)_
___

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

___
**To install the frontend in one go, run:**
```
make install-frontend
```
_(You can skip directly to [creating sample data](#creating-sample-data) after this.)_
___

To install necessary node modules, run:
```
make install-frontend
```

To start the React development server, run:
```
make start-frontend
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

### Starting the Site

To start the backend and other containers, run:
```
make up
```

Then, to start React's development server, in a separate terminal, run:
```
make start-frontend
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
