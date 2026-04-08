# Data Pipeline

ETL and data processing services for TechCorp.

## Overview
This repository contains data pipeline utilities for extracting, transforming, and loading data across TechCorp's platforms.

## Getting Started
```bash
pip install -r requirements.txt
python main.py
```

## Configuration
Set the following environment variables:
- `DATA_SOURCE_URL`: URL of the data source
- `DATA_SINK_URL`: URL of the data sink
- `PIPELINE_BATCH_SIZE`: Number of records per batch (default: 1000)
