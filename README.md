#### Todo App

This app is to demonstrate the execution of SQL statements in an application. This is meant for the students of the Intro to Database course.

The app is built using Flask with the Psycopg2 library being used to connect to a Postgrsql database with the following data model.


```
CREATE TABLE todo (
    id serial not null,
    name varchar(100) not null,
    completed boolean not null default false,
    constraint todo_pkey primary key (id)
)
```

#### Environment variables

Set the DATABASE_URL environment variable on windows by using the following command.

```
set DATABASE_URL=postgresql://username:password@host:port/database
```