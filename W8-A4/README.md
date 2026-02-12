# AI-Powered CV Analysis (Multi-Container Docker)

This project analyzes CV files (PDF/DOCX) using the Google Gemini API.\
It is deployed as a multi-container Docker application using Docker
Compose.

---

## Multi-Container Architecture

The application runs using two containers:

- cli\
    Interactive container where the user enters a CV file path and
    receives analysis results.

- worker\
    Automatically processes a sample CV file to demonstrate background
    execution.

Both containers: 
- Use the same Python application 
- Share the `inputs/` folder for CV files 
- Share the `output/` folder (if saving results) 
- Use an environment variable for the API key

---

## How to Run

Build and start containers:

```
docker compose up -d --build
```

Check running containers:
```
docker ps
```
Attach to the CLI container:
```
docker attach cv_cli
```
Stop containers:
```
docker compose down
```
----

## Features

-   Extracts text from PDF and DOCX files
-   Uses Gemini API to analyze CV content
-   Suggests suitable job roles
-   Provides improvement recommendations
-   Demonstrates multi-container Docker deployment
