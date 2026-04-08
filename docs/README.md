# Data Pipeline Documentation

## Overview

The Data Pipeline service is responsible for ingesting, transforming, and delivering data across the TechCorp platform. This document provides an up-to-date guide for developers and operators.

## Architecture

```
[Source Systems] → [Ingestion Layer] → [Transform Layer] → [Sink Layer] → [Consumers]
```

### Components

1. **Ingestion Layer** — Accepts data from upstream sources via REST API and message queue subscribers.
2. **Transform Layer** — Applies business rules, schema validation, and enrichment.
3. **Sink Layer** — Writes processed data to the target data stores (Postgres, S3, Elasticsearch).

## Getting Started

### Prerequisites

- Python 3.11+
- Docker & Docker Compose
- Access to the TechCorp container registry

### Local Development

```bash
# Clone the repository
git clone https://github.com/TechCorp/data-pipeline.git
cd data-pipeline

# Start dependencies
docker compose up -d

# Run the pipeline locally
make run
```

### Running Tests

```bash
make test
```

## Configuration

Environment variables are used for all runtime configuration. See `.env.example` for a full list.

| Variable | Description | Default |
|---|---|---|
| `PIPELINE_BATCH_SIZE` | Number of records per batch | `500` |
| `PIPELINE_WORKERS` | Parallel worker count | `4` |
| `SINK_POSTGRES_URL` | Postgres connection string | — |
| `SINK_S3_BUCKET` | Target S3 bucket name | — |

## Deployment

Deployment is managed via the CI/CD pipeline. Merges to `main` trigger an automatic deployment to staging. Production deployments require manual approval.

## Monitoring & Alerts

- **Metrics**: Published to CloudWatch under the `TechCorp/DataPipeline` namespace.
- **Logs**: Structured JSON logs shipped to CloudWatch Logs.
- **Alerts**: PagerDuty alerts are configured for error-rate spikes and latency thresholds.

## Contributing

1. Create a feature branch from `main`.
2. Open a pull request with a clear description of changes.
3. Ensure all CI checks pass before requesting review.
4. At least one approval from a platform team member is required.

## Contacts

- **Platform Team Lead**: Carol Williams
- **On-Call Rotation**: See PagerDuty schedule `data-pipeline-oncall`

---

_Last updated: 2025-07-09 by Bob Martinez_
