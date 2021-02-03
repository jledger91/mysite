# My Site
A test Django site for development purposes. Once set up, it can be found at:
`http://localhost`.

- [Features in Consideration](#features-in-consideration)
- [Overview](#overview)
  - [Admin Site](#admin-site)
  - [API](#api)
- [Development](#development)
  - [Installation](#installation)
  - [Tests](#tests)
  - [Django Shell](#django-shell)


## Features in Consideration
The site is now heading in the direction of a film review website, à la _Rotten
Tomatoes_. Here are some proposed plans for it:

- Separating the film and review functionality into separate apps? The idea for
  an app is to do one thing and one thing _well_, so perhaps having one app 
  to serve as a film catalogue and another to serve as a film review app makes
  sense.
- An app for recommendations based on film tags? Could be cool to combine this
  with _Netflix_ style machine learning in order to recommend viewers films to
  see (and review).
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

### Installation
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

### Tests
To run the test suits, use:
```
make test
```

### Django Shell
To interact with your data via Django's shell, run:
```
make shell
```
