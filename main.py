from fastapi import FastAPI
from transformers import AutoModelForCausalLM, AutoTokenizer

checkpoint = "bigscience/bloomz-560m"

print("Getting model")
tokenizer = AutoTokenizer.from_pretrained(checkpoint)
model = AutoModelForCausalLM.from_pretrained(checkpoint)

print("Starting API")
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/encode")
async def encode(message: str = ''):
    inputs = tokenizer.encode(message, return_tensors="pt")
    print("Past inputs")
    outputs = model.generate(inputs)
    print(tokenizer.decode(outputs[0]))
    return {"message": tokenizer.decode(outputs[0])}