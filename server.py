import uvicorn
from api.main import create_app

# Initialize the FastAPI server
app = create_app()

if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=8080)