# bonsai_server

Bonsai Socket, implemented using NodeJS. Listens to changes within the RethinkDB

### Directory Structure
#### head
index.js - primary executable. Starts a bonsai socket & ensures all dependencies are met
Dockerfile - Docker build instructions

#### api/
Contains functions used to implement the REST API, used for dashboarding
controllers - functions that interface with RethinkDB
routes - routes that expose the functions defined within the controllers directory

#### socket/
Contains functions used to implement Socket.IO, used for metric streaming
rethink.js - Implements a connection pool to rethinkDB
dbController.js - Implements database functions
