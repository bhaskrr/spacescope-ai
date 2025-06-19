from fastapi import FastAPI, Depends
from fastapi.responses import JSONResponse
from server.database.client import get_client
from server.schemas.route_schemas import InputQuery
from server.utils.process_input_query import preprocess_query
from server.pipelines.input_processor import process_and_check_input_appropriateness
from server.pipelines.answer_generator import generate_direct_answer_from_llm

app = FastAPI()

@app.get("/", tags=["Homepage"])
def main():
    """Homepage"""
    return {"Hello from": "server"}


@app.get("/collections")
def get_collections(client=Depends(get_client)):
    collections = client.list_collections()
    print("Collections:", collections)
    collection_names = [getattr(c, "name", str(c)) for c in collections]

    return {"collections": collection_names}


@app.post("/ask")
def ask_without_augmentation(payload: InputQuery):
    """Generates answer directly from the LLM"""
    raw_query = payload.query.strip()

    if raw_query == "":
        return JSONResponse(content="The input can not be empty.", status_code=400)

    moderation_output = process_and_check_input_appropriateness(raw_query)

    if moderation_output is True:
        # Preprocess
        preprocessed_query = preprocess_query(raw_query)
        # Proceed to generate
        answer = generate_direct_answer_from_llm(preprocessed_query)
        # Return the generated answer back to the client
        return JSONResponse(content={"answer": answer}, status_code=200)

    # else, the content is not appropriate, so return an error message indicating the failed moderation
    return JSONResponse(
        content={"error": "The input did not pass the moderation check."},
        status_code=400,
    )
