# labelbox

Object Relational Mapper example Martyn

## Rationale

Build an entire python package from scratch. Focus on Object Relational Mapper: basically a software wrapper for connecting to relational (SQL-like) databases.

## Steps

    git log master..labelbox --pretty=format:'%s' --reverse
    README: initial checkin
    README: small explanation
    README: repo navigating
    LICENSE: checking BSD style license
    CHANGELOG: checkin
    labelbox: adds __init__.py file
    demo: call package constants from external file
    .gitignore: ignore pyc files
    models: adds a recording class
    demo: make a recording object
    models: read method on recording
    labelbox: minimal working ORM demo recording
    label box: adds event type
    labelbox: adds label type + database interactions
    requirements: scipy, sqlalchemy, tabulate
    setup.py: package setup script

## Repo navigating

Next: to child commit (towards `labelbox` branch pointer):

    git reset --hard `git log --reverse --ancestry-path HEAD..labelbox | head -n 1 | cut -d \  -f 2`

Previous: to parent commit

    git reset --hard presentation~
