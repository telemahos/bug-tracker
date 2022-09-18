### REPORT ###

- When I call via SQL many row.sall(), then I have to do List[schema.tableModel], otherwise row.first(), must be simple schema.tableModel and not list
- On an error 422 on API call, check if send correct data, e.g. String as String or integer as integer. Copy a call Example Value Schema from Swager and compare it to the data that the application is sending. You may send wrong data types 
 