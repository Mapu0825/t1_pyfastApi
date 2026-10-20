from src.templates.controllers import create_trainee, get_all_trainees, get_trainee_by_id, update_trainee, delete_trainee

from src.models.model import TraineeModel, TraineeUpdateModel
from fastapi import FastAPI, HTTPException, status
# uvicorn src.main:app --reload

app = FastAPI(
    title="Gestion de datos de los aprendices",
    description="API simple con FastApi para consumir los dados de los aprendices",version = "1.0.0",
)
# Mensaje de bienvenida
@app.get("/")
async def root():
    return {"message": "Hello World"}

# Registrar aprendices 
@app.post(
    "/trainees", response_description="Registrar un aprendiz", status_code=status.HTTP_201_CREATED
)

def create_trainee_api(trainee: TraineeModel):
    # validar si ya existe el documento
    return create_trainee(trainee)

# Onbtener la lista de aprendices
@app.get("/trainees", response_description="listar todos los aprendices"
)
def get_all_trainees_api():
    return get_all_trainees()

# Obtener un aprendiz por id
@app.get(
    "/trainees/{id}", response_description="Obtener un aprendiz por id"
)
def get_trainee_by_id_api(id: str):
    return get_trainee_by_id(id)
    if not trainee:
        raise HTTPExeption(status_code=404, detail="Aprendiz no encontrado")
    return Trainee

# Actualizar datos de un aprendiz por su id
@app.put(
    "/trainees/{id}", response_description="Actualizar datos un aprendiz por id"
)
def update_trainee_api(id: str, trainee: TraineeUpdateModel):
    trainee = update_trainee(id, trainee)
    if not trainee_update:
        raise HTTPExeption(
            status_code=404, detail="Aprendiz no encontrado o sin datos a actualizar",
        )
        return trainee_update

# Eliminar un aprendiz por su id
@app.delete(
    "/trainees/{id}", response_description="Eliminar daros de un aprendiz "
)
def delete_trainee_api(id: str):
    trainee =  delete_trainee(id)
    if not trainee:
        raise HTTPExeption(
            status_code=404, detail="Aprendiz no encontrado"
        )
        return {"message": "Aprendiz eliminado con exito"}