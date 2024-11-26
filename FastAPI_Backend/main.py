from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, conlist
from typing import List, Optional
import pandas as pd
from model import recommend, output_recommended_recipes

# Load dataset
dataset = pd.read_csv('../Data/dataset.csv', compression='gzip')

app = FastAPI()

class Params(BaseModel):
    n_neighbors: int = 5
    return_distance: bool = False

class PredictionIn(BaseModel):
    nutrition_input: conlist(float, min_items=9, max_items=9)
    ingredients: List[str] = []
    params: Optional[Params]

class Recipe(BaseModel):
    Name: str
    CookTime: str
    PrepTime: str
    TotalTime: str
    RecipeIngredientParts: List[str]
    Calories: float
    FatContent: float
    SaturatedFatContent: float
    CholesterolContent: float
    SodiumContent: float
    CarbohydrateContent: float
    FiberContent: float
    SugarContent: float
    ProteinContent: float
    RecipeInstructions: List[str]

class PredictionOut(BaseModel):
    output: Optional[List[Recipe]] = None

@app.get("/")
def home():
    return {"health_check": "OK"}

@app.post("/predict/", response_model=PredictionOut)
def update_item(prediction_input: PredictionIn):
    try:
        recommendation_dataframe = recommend(
            dataset,
            prediction_input.nutrition_input,
            prediction_input.ingredients,
            prediction_input.params.dict() if prediction_input.params else {}
        )
        output = output_recommended_recipes(recommendation_dataframe)
        if output is None:
            return {"output": None}
        return {"output": output}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
