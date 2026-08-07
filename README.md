# Escruta - Search

> [!CAUTION]
> **This repository has been deprecated.**
> Its functionality has been merged into the unified [Helper](https://github.com/escruta/helper) service.

Dedicated microservice for web search within the Escruta platform. Allows users to search the web directly from their notebooks, returning structured results (title, link, snippet) for AI processing.

Built with Python, FastAPI, and DDGS.

> [!NOTE]
> This service is **no longer part of the active Escruta ecosystem**. Web search is now provided by [Helper](https://github.com/escruta/helper) (`POST /search`). This repository is kept for archival purposes only.

## Getting Started (legacy)

> [!WARNING]
> The instructions below only apply if you are running this service for historical or development purposes. New deployments should use the [Helper](https://github.com/escruta/helper) service instead.

1. `uv sync` - Install dependencies
2. `uv run --env-file .env fastapi run --port 8001` - Start the development server

The search service will be available at [localhost:8001](http://localhost:8001).

## Configuration

### Environment Variables

The application is secured and configured using environment variables. These must be set in your `.env` file or environment.

| Variable                   | Description                                           | Default    |
| -------------------------- | ----------------------------------------------------- | ---------- |
| `ESCRUTA_INTERNAL_API_KEY` | Internal API Key for service-to-service communication | (Required) |
