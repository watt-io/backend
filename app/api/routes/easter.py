import fastapi

router = fastapi.APIRouter()

@router.get('/easter')
async def egg():
	return {
		"body": "Have you notice that all preloaded movies are from Adam Sandler ?",
		"answer": "I guess not! Gotcha!"
	}