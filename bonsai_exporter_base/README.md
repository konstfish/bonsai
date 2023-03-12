# bonsai_exporter_base

Basis for a bonsai exporter.

### Directory Structure
#### head
BonsaiClient.py - BonsaiClient Class definition. Handles metric gathering & sending.
BonsaiConfigLoader.py - BonsaiConfigLoader Class definition. Reads config files (like config.yaml)
Dockerfile - Docker build instructions

#### certs/
Contains testing certificates

#### exporters/
Contains exporter classes & the base exporter class under BonsaiExporter.py

#### proto/
Contains the bonsai.proto definition & compiled python