from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://didactic-tribble-97j65vjp676wh975x-5173.app.github.dev"],  # Use ["https://5173-...github.dev"] for tighter security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Dummy users
users = [
    {"username": "admin", "password": "admin123"},
    {"username": "user1", "password": "pass1"},
    {"username": "user2", "password": "pass2"}
]

# Login request model
class LoginRequest(BaseModel):
    username: str
    password: str

@app.post("/login")
def login(data: LoginRequest):
    for user in users:
        if user["username"] == data.username and user["password"] == data.password:
            return {"message": "Login successful", "user": user["username"]}
    raise HTTPException(status_code=401, detail="Invalid username or password")

@app.get("/returns")
def get_returns():
    return {"returns": ["Return #1", "Return #2", "Return #3"]}

@app.get("/admin")
def get_admin_dashboard():
    return {"admin": {"users": len(users), "status": "active"}}

@app.get("/billing")
def get_billing_info():
    return {"billing": {"invoices": 5, "pending": 2}}

@app.get("/hub")
def get_hub_data():
    return {"hub": "Central dashboard data"}
