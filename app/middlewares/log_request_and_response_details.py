from fastapi import Request


async def log_request_response(request: Request, call_next):
    # Log request details
    print(f"Request: {request.method} {request.url}")
    print(f"Headers: {request.headers}")
    
    response = await call_next(request)
    
    # Log response details
    print(f"Response status: {response.status_code}")
    print(f"Response headers: {response.headers}")
    
    return response