# abbysangels

> My remarkable Nuxt.js project

## Specifications
> Python 3.6+ 
> NPM 6.14+
> Node 12.18+

## Backend Setup
```bash

# Creating a virtual environment
$ python -m venv myenv

# Navgiate to project/app and install dependencies
$ pip install -r requirements.txt

# Migrate data
$ python manage.py makemirations
$ python manage.py migrate

# Loading dump data
$ python manage.py loaddata mainapp.json

# Run the program
$ python manage.py runserver
```

## Build Setup

```bash
# install dependencies
$ npm install

# serve with hot reload at localhost:3000
$ npm run dev

# build for production and launch server
$ npm run build
$ npm run start

# generate static project
$ npm run generate
```

For detailed explanation on how things work, check out [Nuxt.js docs](https://nuxtjs.org).
