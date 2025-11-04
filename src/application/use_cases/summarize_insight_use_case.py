class SummarizeInsightUseCase:
    def __init__(self, insight_service):
        self.service = insight_service

    def execute(self, prompt: str, data_json: str):
        return self.service.summarize(prompt, data_json)
