# Escruta - Search

> [!CAUTION]
> **This repository has been deprecated.**
> Its functionality has been merged into the unified [Helper](https://github.com/escruta/helper) service.

Dedicated microservice for web search within the Escruta platform. Allows users to search the web directly from their notebooks, returning structured results (title, link, snippet) for AI processing.

Built with Python, FastAPI, and DDGS.

> [!IMPORTANT]
> This service is a required component of the Escruta ecosystem. It must be accessible to the Core service for proper web search functionality.

## Getting Started

1. `uv sync` - Install dependencies
2. `uv run --env-file .env fastapi run --port 8001` - Start the development server

The search service will be available at [localhost:8001](http://localhost:8001). It is consumed by [Core](https://github.com/escruta/core) at this URL (configured via `ESCRUTA_SEARCH_URL`).

## Configuration

### Environment Variables

The application is secured and configured using environment variables. These must be set in your `.env` file or environment.

| Variable                   | Description                                           | Default    |
| -------------------------- | ----------------------------------------------------- | ---------- |
| `ESCRUTA_INTERNAL_API_KEY` | Internal API Key for service-to-service communication | (Required) |
