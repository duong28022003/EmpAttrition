from fastapi.middleware.cors import CORSMiddleware

origins = ["*"]

def setup_cors(app):
    app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  
    allow_credentials=True,
    allow_methods=["*"],    
    allow_headers=["*"],   
)
    