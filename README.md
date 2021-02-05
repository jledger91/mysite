# My Site

A test Django site for development purposes. Once set up, it can be found at:
`http://localhost`.

- [Features in Consideration](#features-in-consideration)
- [Overview](#overview)
  - [Admin Site](#admin-site)
  - [API](#api)
- [Development](#development)
  - [Dependencies](#dependencies)
  - [Installation](#installation)
  - [Creating Sample Data](#creating-sample-data)
  - [Tests](#tests)
  - [Django Shell](#django-shell)


## Features in Consideration

The site is now heading in the direction of a film review website, à la [Rotten
Tomatoes](https://www.rottentomatoes.com/). Here are some proposed plans for it:

- Separating the film and review functionality into separate apps? The idea for
  an app is to do one thing and one thing _well_, so perhaps having one app 
  to serve as a film catalogue and another to serve as a film review app makes
  sense.
- Models for cast and crew.
- An app for recommendations based on film tags? Could be cool to combine this
  with [Netflix](https://www.netflix.com) style machine learning in order to 
  recommend films to see (and review) to users.
- A React front-end is on the way, it just needs some designing. JavaScript or
  TypeScript? Functional or Class components? What toolkit? [Material Kit React](
    https://demos.creative-tim.com/material-kit-react/?_ga=2.65695594.538724389.1612323036-1959417379.1612323036#/
  ) is apparently regarded quite highly, so it's worth a look.


## Overview

### Admin Site

The admin site, for managing your data, can be found at `http://localhost/admin` 
and can be accessed using your superuser credentials.

### API

The API can be accessed at `http://localhost/api/`.


## Development

### Dependencies

- Docker
- docker-compose

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

To run the test suite, use:
```
make test
```

### Django Shell

To interact with your data via Django's shell, run:
```
make shell
```
