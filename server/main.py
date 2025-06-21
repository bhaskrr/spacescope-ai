from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from server.config.settings import AppSettings
from server.database.client import get_client
from server.schemas.route_schemas import InputQuery
from server.utils.process_input_query import preprocess_query
from server.pipelines.input_processor import process_and_check_input_appropriateness
from server.pipelines.answer_generator import (
    generate_direct_answer_from_llm,
    answer_with_rag,
)

app = FastAPI()

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=AppSettings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=AppSettings.CORS_METHODS,
    allow_headers=AppSettings.CORS_HEADERS,
)


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
def ask(payload: InputQuery):
    """Generates answer"""
    raw_query = payload.query.strip()
    answer_mode = payload.mode.value
    
    # ! Debugging
    print("Raw Query:", raw_query)
    print("Answer Mode:", answer_mode)

    if raw_query == "":
        return JSONResponse(content="The input can not be empty.", status_code=400)

    moderation_output = process_and_check_input_appropriateness(raw_query)

    if moderation_output is True:
        # Preprocess
        preprocessed_query = preprocess_query(raw_query)
        # Proceed to generate
        if answer_mode == "normal":
            # * Generate the answer directly from the LLM
            answer = generate_direct_answer_from_llm(preprocessed_query)
            print("Answer:", answer)

            # Return the generated answer back to the client
            return JSONResponse(content=answer, status_code=200)
        elif answer_mode == "rag":
            # * Generate the answer by augmenting the query with context retrieved from chromadb
            answer = answer_with_rag(preprocessed_query)
            print("Answer:", answer)

            # Return the generated answer back to the client
            return JSONResponse(content=answer, status_code=200)

    # else, the content is not appropriate, so return an error message indicating the failed moderation
    else:
        return JSONResponse(
            content={"error": "The input did not pass the moderation check."},
            status_code=400,
        )
