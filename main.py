from fastapi import FastAPI #IMPORT


app = FastAPI() #INSTANCE OF FASTAPI

@app.get('/') #ROUTE
async def index() -> dict[str, str]: #ASYNC FUNCTION WITH PROPER RETURN TYPE
    return {'hello': 'world'}

@app.get('/about')
async def about() -> str:
    return 'AN EXCEPTIONAL COMAPNY"

