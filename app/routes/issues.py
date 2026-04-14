import uuid
from fastapi import APIRouter, HTTPException, status
from app.schemas import IssueCreate, IssueOut, IssueStatus, IssueUpdate
from app.storage import load_data, save_data

router = APIRouter(
    prefix="/issues",
    tags=["issues"],
)

@router.get("/", response_model=list[IssueOut], status_code=status.HTTP_200_OK, summary="Get all issues", description="Retrieve a list of all issues")
async def get_all_issues():
    return load_data()

@router.get("/{issue_id}", response_model=IssueOut, status_code=status.HTTP_200_OK, summary="Get issue by ID", description="Retrieve a single issue by its ID")
async def get_issue(issue_id: str):
    issues = load_data()
    issue = next((issue for issue in issues if issue["id"] == issue_id), None)
    if not issue:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Issue not found")
    return issue

@router.post("/", response_model=IssueOut, status_code=status.HTTP_201_CREATED, summary="Create a new issue", description="Create a new issue with the provided details")
async def create_issue(issue: IssueCreate):
    new_issue = issue.model_dump()
    new_issue["id"] = str(uuid.uuid4())
    new_issue["status"] = IssueStatus.open.value
    
    issues = load_data()
    issues.append(new_issue)
    save_data(issues)
    
    return new_issue

@router.put("/{issue_id}", response_model=IssueOut, status_code=status.HTTP_200_OK, summary="Update an issue", description="Update an existing issue with the provided details")
async def update_issue(issue_id: str, issue_update: IssueUpdate):
    issues = load_data()
    issue = next((issue for issue in issues if issue["id"] == issue_id), None)
    if not issue:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Issue not found")
    
    update_data = issue_update.model_dump(exclude_unset=True)
   
    for key, value in update_data.items():
        issue[key] = value
    
    save_data(issues)
    return issue

@router.delete("/{issue_id}", status_code=status.HTTP_204_NO_CONTENT, summary="Delete an issue", description="Delete an existing issue by its ID")
async def delete_issue(issue_id: str):
    issues = load_data()
    issue = next((issue for issue in issues if issue["id"] == issue_id), None)
    if not issue:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Issue not found")
    
    issues.remove(issue)
    save_data(issues)
    return None

@router.get("/status/{status}", response_model=list[IssueOut], status_code=status.HTTP_200_OK, summary="Get issues by status", description="Retrieve a list of issues filtered by their status")
async def get_issues_by_status(status: IssueStatus):
    issues = load_data()
    filtered_issues = [issue for issue in issues if issue["status"] == status.value]
    return filtered_issues

