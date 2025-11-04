from domain.entities.insight import Insight

class GenerateSQLUseCase:
    def __init__(self, ai_client, query_repo, base_prompt: str):
        self.ai = ai_client
        self.repo = query_repo
        self.base_prompt = base_prompt

    def execute(self, user_prompt: str) -> Insight:
        sql = self.ai.chat(self.base_prompt, user_prompt)
        print(sql)
        result = self.repo.run(sql)
        return Insight(prompt=user_prompt, sql=sql, result=result)