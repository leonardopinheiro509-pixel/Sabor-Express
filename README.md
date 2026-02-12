# Sabor Express

> Aplicativo CLI simples para gerenciar restaurantes (projeto pessoal).

## Como rodar

1. Abra o terminal na pasta do projeto.
2. (Opcional) crie e ative um ambiente virtual:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

3. Instale dependências (se houver):

```powershell
pip install -r requirements.txt
```

4. Execute:

```powershell
python app.py
```

## Subir para o GitHub

- Inicializar git localmente:

```powershell
git init
git add .
git commit -m "Initial commit"
```

- Criar repositório remoto (via GitHub website ou `gh` CLI) e dar push:

```powershell
# com gh
gh repo create NOME-DO-REPO --public --source=. --push

# ou manualmente
git remote add origin https://github.com/SEU_USUARIO/NOME-DO-REPO.git
git branch -M main
git push -u origin main
```

Substitua `NOME-DO-REPO` e `SEU_USUARIO` conforme necessário.