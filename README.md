# python-frontend-frameworks
A comparison of different python web frameworks in creating dashboards.

## Example data
- the data used for these frontends is an example dataset from data.world of an e-commerce store.
- `https://data.world/jfreex/e-commerce-users-of-a-french-c2c-fashion-store`

Tested on a 2018 Mac Mini using python3.12

### Running and loading data
- `docker compose up -d`

### Pgadmin connection settings
- host: docker.for.mac.host.internal
- port: 5433
- user: postgres
- password: changeme
- database: postgres
- schema: public

### Dashboard specific frameworks
- Streamlit - DONE
- Panel - Half done
- Dash
- Taipy -
- Shiny - DONE
- Bokeh - Not doing (more of a plotting library)
- Bowtie (No longer maintained) - Attempted to run but failed

### General purpose frameworks
- Fasthtml - DONE
- Reactpy
- Flet
- Nicegui
- Mesop - DONE