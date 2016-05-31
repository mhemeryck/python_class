# labelbox

Object Relational Mapper example Martyn

## Rationale

Build an entire python package from scratch. Focus on Object Relational Mapper: basically a software wrapper for connecting to relational (SQL-like) databases.

## Repo navigating

Next: to child commit (towards `labelbox` branch pointer):

    git reset --hard `git log --reverse --ancestry-path HEAD..labelbox | head -n 1 | cut -d \  -f 2`

Previous: to parent commit

    git reset --hard presentation~
