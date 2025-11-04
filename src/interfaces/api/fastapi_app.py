from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from infrastructure.ai.openai_client import OpenAIClient
from infrastructure.database.postgres_query_repository import PostgresQueryRepository
from domain.services.insight_service import InsightService
from application.use_cases.generate_sql_use_case import GenerateSQLUseCase
from application.use_cases.summarize_insight_use_case import SummarizeInsightUseCase
from application.use_cases.generate_chart_use_case import GenerateChartUseCase

origins = ["http://localhost:5173"]

app = FastAPI(title="Restaurant Analytics API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

ai_client = OpenAIClient()
query_repo = PostgresQueryRepository()
insight_service = InsightService(ai_client)

@app.get("/insight")
def insight(prompt: str = Query(...)):
    base_prompt = open("prompt.txt", encoding="utf-8").read()
    use_case = GenerateSQLUseCase(ai_client, query_repo, base_prompt)
    insight = use_case.execute(prompt)

    summary_use_case = SummarizeInsightUseCase(insight_service)
    summary = summary_use_case.execute(prompt, str(insight.result))
    return summary

@app.get("/chart")
def chart(prompt: str = Query(...)):
    base_prompt = open("prompt.txt", encoding="utf-8").read()
    sql_use_case = GenerateSQLUseCase(ai_client, query_repo, base_prompt)
    insight = sql_use_case.execute(prompt)

    chart_use_case = GenerateChartUseCase(insight_service, query_repo)
    chart_data = chart_use_case.execute(prompt, insight.sql)
    return chart_data
