# FastAPI Issue Tracker

A simple API for tracking issues, allowing you to create, read, update, and delete issues.

## Features

- Create, read, update, and delete issues
- Each issue has a title, description, status, and unique ID
- CORS enabled for web applications
- Request timing and logging middleware

## Local Development

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the application:
   ```bash
   uvicorn main:app --reload
   ```

3. Open http://localhost:8000/docs for the interactive API documentation

## Deployment on Vercel

This project is configured for deployment on Vercel:

1. Install Vercel CLI:
   ```bash
   npm install -g vercel
   ```

2. Deploy:
   ```bash
   vercel
   ```

3. Follow the prompts to link your Vercel account and deploy the project.

The API will be available at your Vercel domain, with the interactive docs at `/docs`.

**Important Note:** This deployment uses file-based storage which is not persistent on Vercel. Data will reset between deployments and cold starts. For production use, consider migrating to a database service like Vercel Postgres or MongoDB Atlas.

## API Endpoints

- `GET /api/v1/issues` - Get all issues
- `GET /api/v1/issues/{id}` - Get a specific issue
- `POST /api/v1/issues` - Create a new issue
- `PUT /api/v1/issues/{id}` - Update an issue
- `DELETE /api/v1/issues/{id}` - Delete an issue
