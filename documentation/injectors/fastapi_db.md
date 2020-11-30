Sample template for generating code for database.

```
---
    injectors:
        app_name: ['Name of the application']
        db_engine: [ 'mysql' | 'postgresql' | 'mariadb' | 'mongodb' | 'redis']
        tables:
            - name: 'playertype'
              columns:
                - name: 'Column Name'
                  type: 'Database Data Type'
                  is_primary: [ True | False ]
                  is_requried: [ True | False ]
                  is_unique : [ True | False ]

```