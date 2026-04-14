from fastapi import FastAPI
from app.routes.issues import router as issue_routes
from fastapi.middleware.cors import CORSMiddleware
from app.middlewares.timing import timing_middleware
from app.middlewares.log_request_and_response_details import log_request_response

app = FastAPI(
    title="Issue Tracker API",
    description="A simple API for tracking issues, allowing you to create, read, update, and delete issues. Each issue has a title, description, status, and a unique ID.",
    version="1.0.0",
)

app.middleware("http")(timing_middleware)
app.middleware("http")(log_request_response)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  #
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



app.include_router(issue_routes, prefix="/api/v1")    

# @app.get("/")
# async def root():
#     return {"message": "Hello World"}

# items : list[dict[str, str]] = [
#     {"id": 1, "name": "Item 1", "description": "This is item 1"},
#     {"id": 2, "name": "Item 2", "description": "This is item 2"},
#     {"id": 3, "name": "Item 3", "description": "This is item 3"},
# ]

# @app.get("/items")
# async def read_items():
#     return items

# @app.get("/items/{item_id}")
# async def read_item(item_id: str):                                                                                                                      
#     try:                                                                                                    
#         return next(item for item in items if item["id"] == int(item_id))                                     
#     except KeyError:
#         return {"error": "Item not found"}
#     except StopIteration:
#         return {"error": "Item not found"}
    
# @app.post("/items")
# async def create_item(item: dict[str, str]):
#     item["id"] = len(items) + 1
#     items.append(item)
#     return item

# @app.put("/items/{item_id}")
# async def update_item(item_id: str, item: dict[str, str]):
#     try:
#         existing_item = next(item for item in items if item["id"] == int(item_id))
#         existing_item.update(item)
#         return existing_item
#     except KeyError:
#         return {"error": "Item not found"}
#     except StopIteration:
#         return {"error": "Item not found"}
    
# @app.delete("/items/{item_id}")
# async def delete_item(item_id: str):
#     try:
#         item = next(item for item in items if item["id"] == int(item_id))
#         items.remove(item)
#         return {"message": "Item deleted"}
#     except KeyError:
#         return {"error": "Item not found"}
#     except StopIteration:
#         return {"error": "Item not found"}

