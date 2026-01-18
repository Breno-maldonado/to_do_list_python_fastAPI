from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List, Optional
import json
import os

app = FastAPI(title="Minha API de Tarefas Pro")

ARQUIVO_JSON = "tarefas.json"

class Tarefa(BaseModel):
    id: Optional[int] = None
    titulo: str = Field(..., min_length=3, max_length=50, description="O nome da tarefa")
    descricao: Optional[str] = Field(None, max_length=200, description="Detalhes da tarefa")
    concluido: bool = False

def ler_banco():
    if not os.path.exists(ARQUIVO_JSON):
        return []
    with open(ARQUIVO_JSON, "r", encoding="utf-8") as f:
        return json.load(f)

def salvar_banco(dados):
    with open(ARQUIVO_JSON, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)

@app.get("/tarefas", response_model=List[Tarefa])
def listar_tarefas():
    """Retorna todas as tarefas do arquivo."""
    return ler_banco()

@app.post("/tarefas", status_code=201)
def criar_tarefa(nova_tarefa: Tarefa):
    """Cria uma tarefa e gera o ID automaticamente."""
    banco = ler_banco()
    
    novo_id = banco[-1]["id"] + 1 if banco else 1
    
    tarefa_dict = nova_tarefa.dict()
    tarefa_dict["id"] = novo_id
    
    banco.append(tarefa_dict)
    salvar_banco(banco)
    return tarefa_dict

@app.get("/tarefas/{id_procurado}")
def buscar_por_id(id_procurado: int):
    banco = ler_banco()
    for t in banco:
        if t["id"] == id_procurado:
            return t
    raise HTTPException(status_code=404, detail="Tarefa não encontrada")

@app.put("/tarefas/{id_procurado}")
def atualizar_tarefa(id_procurado: int, tarefa_atualizada: Tarefa):
    """Atualiza uma tarefa existente, validando os novos dados."""
    banco = ler_banco()
    
    for indice, t in enumerate(banco):
        if t["id"] == id_procurado:
            dados_novos = tarefa_atualizada.dict()
            dados_novos["id"] = id_procurado
            
            banco[indice] = dados_novos
            salvar_banco(banco)
            return {"mensagem": "Atualizado com sucesso", "tarefa": dados_novos}
            
    raise HTTPException(status_code=404, detail="ID não encontrado para atualização")

@app.delete("/tarefas/{id_procurado}")
def deletar_tarefa(id_procurado: int):
    banco = ler_banco()
    for indice, t in enumerate(banco):
        if t["id"] == id_procurado:
            banco.pop(indice)
            salvar_banco(banco)
            return {"mensagem": f"Tarefa {id_procurado} removida"}
            
    raise HTTPException(status_code=404, detail="Não foi possível deletar: ID inexistente")