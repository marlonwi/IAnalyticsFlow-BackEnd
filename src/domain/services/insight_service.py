import json

class InsightService:
    def __init__(self, ai_client):
        self.ai = ai_client

    def generate_sql(self, prompt: str, base_prompt: str) -> str:
        return self.ai.chat(base_prompt, prompt)

    def summarize(self, prompt: str, data_json: str) -> str:
        summary_prompt = (
            f"Baseado na pergunta que fiz anteriormente, sendo ela: {prompt} \
                Analise o json a seguir e faça um resumo detalhado: {data_json}\n\n \
                Não dê a resposta como se fosse para um programador, fale em tom de resumo para o usuário final para ele usar em \
                tomada de decisões"

        )
        return self.ai.chat("Você é um analista de negócios para restaurantes.", summary_prompt)

    def generate_chart_config(self, prompt: str, data_sample: str) -> dict:
        config_prompt = f"""
        Dado o seguinte JSON de resultados e o prompt original:
        PROMPT: "{prompt}"
        RESULTADO: {data_sample}  # amostra de até 20 linhas

        Retorne um JSON com a configuração ideal de gráfico
        com os campos chartType, xFields, yFields e title.
        Decida o chartType baseado no prompt e JSON, sendo eles:
        BarChart,
        LineChart,
        AreaChart,
        PieChart,
        ScatterChart,
        RadarChart,
        ComposedChart,
        """
        content = self.ai.chat("Você é um gerador de gráficos inteligente.", config_prompt)
        
        return json.loads(content)
