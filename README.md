# IAG - Ingeligência Artificial Generativa

Repositório da disciplina de Ingeligência Artificial Generativa.

## Requisitos

- Python 3.12+ (o projeto exige `>=3.12`)
- [uv](https://docs.astral.sh/uv/) instalado

### Instalar o `uv`

macOS/Linux:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Verificar instalação:

```bash
uv --version
```

## Setup do projeto

No diretório raiz (`ar/`):

```bash
uv sync
```

Esse comando:
- cria automaticamente `.venv/` (se não existir)
- instala todas as dependências definidas no `pyproject.toml`

Dependências principais deste repositório:
- `matplotlib`
- `tiktoken`
- `torch`

