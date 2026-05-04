# ⚙️ Livraria Mackenzie — API (Servidor)

API REST desenvolvida com Flask, independente de qualquer interface. Atua exclusivamente como provedora de dados em formato JSON.

---

## 🏛️ Arquitetura

O projeto segue os princípios da **Clean Architecture**:

```
src/
├── domain/             → Modelos de dados e interfaces (contratos) do sistema
├── app/
│   └── service.py      → Regras de negócio (ex: calcular banner, filtrar livros)
└── infrastructure/     → Leitura dos arquivos de dados (livros.txt, banners.txt, avaliacao.txt)
app.py                  → Controlador: expõe os endpoints REST
```

---

## ✨ Feature Implementada

- **Múltiplas Avaliações:** suporte para exibir várias críticas e notas de diferentes leitores para o mesmo livro.

---

## 🚀 Como Executar

```bash
# Passo 1: Criar o ambiente virtual
python -m venv venv

# Passo 2: Ativar o ambiente virtual
# Windows:
.\venv\Scripts\activate
# Linux/macOS:
source venv/bin/activate

# Passo 3: Instalar as dependências
pip install flask flask-cors

# Passo 4: Rodar o servidor
python app.py
```

O servidor ficará disponível em:

```
http://127.0.0.1:5000/api/livros
```

---

## 🛠️ Tecnologias

| Tecnologia | Uso |
|---|---|
| Python | Linguagem principal |
| Flask | Framework web |
| Flask-CORS | Liberação de acesso cross-origin para o cliente |
