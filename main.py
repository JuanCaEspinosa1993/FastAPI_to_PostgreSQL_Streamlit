from fastapi import FastAPI, Response
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT
from backend.model.user_connection import Userconnection
from backend.schema.user_schema import UserSchema

app = FastAPI()
conn = Userconnection()

@app.get("/", status_code=HTTP_200_OK)
def root():
    items = []
    for data in  conn.read_all():
        dictionary = {}
        dictionary["id"] = data[0]
        dictionary["name"] = data[1]
        dictionary["phone"] = data[2]
        items.append(dictionary)
    return items


@app.get("/api/user/{id}", status_code=HTTP_200_OK)
def get_one(id:str):
    dictionary = {}
    data = conn.read_one(id)
    dictionary["id"] = data[0]
    dictionary["name"] = data[1]
    dictionary["phone"] = data[2]
    return dictionary


@app.post("/api/insert", status_code=HTTP_201_CREATED)
def insert(user_data:UserSchema):
    data = user_data.model_dump()
    data.pop("id")
    conn.write(data)

    return Response(status_code=HTTP_201_CREATED)


@app.put("/api/update/{id}", status_code=HTTP_204_NO_CONTENT)
def update(user_data:UserSchema, id:str):
    data =  user_data.model_dump()
    data["id"] = id
    conn.update(data)
    return Response(status_code=HTTP_204_NO_CONTENT)


@app.delete("/api/delete/{id}", status_code=HTTP_204_NO_CONTENT)
def delete(id:str):
    conn.delete(id)
    return Response(status_code=HTTP_204_NO_CONTENT)