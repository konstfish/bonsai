# bonsai_server

Bonsai Server, implemented in Python

### Directory Structure
#### head
bonsai.py - primary executable. Starts a bonsai server & ensures all dependencies are met
health.py - Health check script, used within the docker container
Dockerfile - Docker build instructions

#### controllers/
Contains classes used to interface with RethinkDB

#### certs/
Contains testing certificates

#### proto/
Contains the bonsai.proto definition, compiled python & the BonsaiService class implementation