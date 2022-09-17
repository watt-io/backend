from fastapi import APIRouter, Depends, HTTPException, status

router = APIRouter()

@router.get("/filmes")