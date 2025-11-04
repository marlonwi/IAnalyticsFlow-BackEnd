# 🧠 IAnalytics Flow — DDD Architecture

API inteligente em **Python + FastAPI**, estruturada em **DDD (Domain-Driven Design)**, que transforma **requisições em linguagem natural** em consultas SQL otimizadas, executa no PostgreSQL e retorna resultados prontos para visualização em gráficos dinâmicos (via React + Recharts).

---

## 🚀 Visão Geral

Esta aplicação foi desenvolvida com foco em **tomada de decisão orientada por dados**, permitindo que o usuário digite algo como:

> "Mostrar o total de vendas por estado e mês dos últimos 6 meses"

E receba automaticamente um JSON estruturado pronto para visualização:

```json
{
  "config": {
    "chartType": "BarChart",
    "xFields": ["month"],
    "yFields": ["total_sales"],
    "title": "Total de Vendas por Mês"
  },
  "columns": ["month", "total_sales"],
  "rows": [
    { "month": "2025-05", "total_sales": 12345 },
    { "month": "2025-06", "total_sales": 17892 }
  ]
}
```

---

## 🏗️ Arquitetura (DDD)

A aplicação segue o padrão **Domain-Driven Design**, dividindo responsabilidades em camadas bem definidas:

```
src/
├── domain/
│   ├── entities/          # Entidades do domínio (Sales, Store, Brand, etc.)
│   ├── value_objects/     # Objetos de valor (Período, Estado, etc.)
│   ├── repositories/      # Interfaces dos repositórios
│   └── services/          # Lógica de negócio pura
│
├── infrastructure/
│   ├── database/          # Conexão e mapeamento PostgreSQL
│   ├── repositories/      # Implementações concretas (SQLAlchemy)
│   ├── openai_client.py   # Integração com OpenAI (montagem da query)
│
├── application/
│   ├── dto/               # Objetos de transferência de dados (entrada/saída)
│   ├── use_cases/         # Casos de uso (Ex: GerarGraficoUseCase)
│   └── services/          # Orquestra lógica entre domínio e infra
│
├── api/
│   ├── controllers/       # Endpoints FastAPI
│   ├── schemas/           # Pydantic models para request/response
│   └── routes.py          # Definição das rotas
│
└── main.py                # Ponto de entrada da aplicação
```

---

## ⚙️ Tecnologias Principais

| Camada | Tecnologias |
|--------|--------------|
| Backend | 🐍 **Python 3.11+**, **FastAPI**, **SQLAlchemy**, **psycopg2**, **OpenAI API** |
| Banco de Dados | 🐘 **PostgreSQL** |
| Frontend (exemplo) | ⚛️ **React + Recharts + TailwindCSS** |
| Cache (opcional) | 🔥 **Redis** |

---

## 💡 Funcionalidades

✅ Conversão de linguagem natural → SQL válida  
✅ Execução segura e parametrizada no PostgreSQL  
✅ Otimização de queries com índices e cache  
✅ Retorno no formato pronto para gráfico (JSON com `config`, `columns`, `rows`)  
✅ Geração automática de tipos de gráfico (`BarChart`, `PieChart`, `LineChart`, etc.)  
✅ Estrutura escalável e desacoplada em DDD  

---

## 🧩 Endpoints Principais

### `GET /grafico`
Gera automaticamente a consulta e o gráfico correspondente.

**Exemplo de uso:**
```bash
GET http://localhost:8000/chart?prompt=total de vendas por estado no último mês
```
```bash
GET http://localhost:8000/insight?prompt=Qual produto vende mais na quinta à noite no iFood?
```

**Retorno:**
```json
{
  "config": { "chartType": "BarChart", "xFields": ["state"], "yFields": ["total_sales"], "title": "Vendas por Estado" },
  "columns": ["state", "total_sales"],
  "rows": [
    {"state": "SP", "total_sales": 12000},
    {"state": "RJ", "total_sales": 8000}
  ]
}
```

---

## 🧠 Fluxo de Execução

1. **Usuário envia um prompt** descritivo (ex: “total de vendas por estado”).  
2. **Camada de aplicação** aciona o caso de uso `GerarGraficoUseCase`.  
3. **Serviço de domínio** traduz o prompt em SQL via **OpenAI API**.  
4. **Repositório** executa a query no PostgreSQL.  
5. **DTO** transforma o resultado em um JSON com configuração de gráfico.  
6. **Frontend (React)** exibe o gráfico automaticamente com base nesse JSON.

---

## 🗄️ Exemplo de Índices no Banco

Para performance em consultas analíticas:

```sql
CREATE INDEX idx_sales_period_state ON sales (sale_date, state);
CREATE INDEX idx_sales_store ON sales (store_id);
CREATE INDEX idx_sales_brand ON sales (brand_id);
```

---

## 🚀 Execução do Projeto

### 2. Criar ambiente virtual
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

### 3. Instalar dependências
```bash
pip install -r requirements.txt
```

### 4. Configurar variáveis de ambiente
Crie um arquivo `.env` com:

```
DATABASE_URL=postgresql://user:password@localhost:5432/seubanco
OPENAI_API_KEY=sk-xxxx
CACHE_ENABLED=true
```

### 5. Rodar o servidor
```bash
uvicorn src.main:app --reload
```

### 6. Acessar a api
- Swagger UI → [http://localhost:8000/docs](http://localhost:8000/docs)

## 🧭 Roadmap

- [ ] Melhorar caching de consultas repetidas  
- [ ] Suporte a queries complexas com joins automáticos  
- [ ] Detecção de tipo de gráfico via IA  
- [ ] Dashboard com múltiplos gráficos simultâneos  
- [ ] Exportação para CSV e Excel  

---

## 👨‍💻 Autor

**Marlon William**  
📧 marlonwilliammota@gmail.com
