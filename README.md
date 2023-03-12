<div align="center">
    <br />
    <img src="./bonsai_frontend/public/seedling-solid.svg" alt="Logo" width="150"/>
    <h1>Bonsai</h1>
    <h3>🌳 Minimal Monitoring System</h3>
</div>

<div align="center">

[![Publish](https://github.com/konstfish/bonsai/actions/workflows/publish.yml/badge.svg?branch=master)](https://github.com/konstfish/bonsai/actions/workflows/publish.yml)
[![license](https://img.shields.io/badge/license-MIT-brightgreen.svg)](https://github.com/konstfish/score4you/blob/master/LICENSE)

</div>

## Setup
This project can be deployed on any machine running docker using docker-compose:
`docker-compose build`
`docker-compose up -d`

## Usage
Once the project has been deployed, its status can be checked using `docker ps`
![docker ps sample](.github/img/docker.png)
The frontend is accessible under port 3000

### Frontend Views
#### Home
Gives an overview of all active exporters
![home](.github/img/main.png)

#### Node Graph
Gives a visual overview of all active exporters
![node-graph](.github/img/node-graph.png)

#### Dashboard
Interactive & Customizable dashboarding
![dashboard](.github/img/dashboard.png)

#### Explore
Provides the raw output from each exporter
![explore](.github/img/explore.png)

## Deploying Exporters
Additional exporters can be deployed either by running main.py (which is contained within bonsai_exporter_base) or by deploying an exporter container.

## Further Reading
See [INTRODUCTION.md](INTRODUCTION.md)