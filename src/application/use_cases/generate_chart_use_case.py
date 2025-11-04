class GenerateChartUseCase:
    def __init__(self, insight_service, query_repo):
        self.service = insight_service
        self.repo = query_repo

    def execute(self, prompt: str, sql: str):
        data = self.repo.run(sql)
        sample = data["rows"][:20]
        chart_config = self.service.generate_chart_config(prompt, str(sample))
        return {**data, "config": chart_config}
