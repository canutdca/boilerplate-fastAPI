import uvicorn

if __name__ == "__main__":
    uvicorn.run("apps.api.main_api:app", host="127.0.0.1", port=8000, reload=True)
