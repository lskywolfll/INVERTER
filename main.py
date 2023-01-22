from typing import Union
import uvicorn
from fastapi import FastAPI


def pairwise(iterable):
    "s -> (s0, s1), (s2, s3), (s4, s5), ..."
    a = iter(iterable)
    return zip(a, a)


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/inverse_element/{element}")
def read_item(element: str, q: Union[str, None] = None):
    resultTest = ""
    parsing_text = element
    testing = parsing_text[::-1]

    for x, y in pairwise([*testing]):
        resultTest += f"{y}{x}"

    if len(parsing_text) % 2 == 0:
        print("work")
    else:
        resultTest += parsing_text[0]
    return resultTest


if __name__ == "__main__":
    uvicorn.run("server.api:app", host="0.0.0.0", port=8000, reload=True)
