import json
import requests
from loguru import logger
from config import PERPLEXITY_API_URL, PERPLEXITY_API_KEY, PERPLEXITY_MODEL

class PerplexityConnector(object):
    def __init__(self):
        self.API_URL: str = PERPLEXITY_API_URL
        self.API_KEY: str = PERPLEXITY_API_KEY

    def get_response(self, questions: dict) -> dict:
        """
        Sends the questions to the API and retrieves answers.
        """
        logger.debug(f"Making an API Request to {PERPLEXITY_MODEL}...")

        # We define the schema strictly in the prompt instead of the API parameters
        # to avoid compatibility issues with the Gemini OpenAI endpoint.
        system_prompt = (
            "You are an expert exam solver. You must answer the following questions.\n"
            "CRITICAL INSTRUCTION: You must output ONLY valid, raw JSON. Do not use Markdown code blocks.\n"
            "The output structure must be exactly like this:\n"
            "{\n"
            "  \"responses\": [\n"
            "    {\n"
            "      \"question_id\": \"<id>\",\n"
            "      \"option_id\": [\"<correct_option_id>\"],\n"
            "      \"type\": \"Single\" or \"Multi\"\n"
            "    }\n"
            "  ]\n"
            "}\n"
            "Ignore HTML tags in the question text. Be precise."
        )

        headers = {
            "Authorization": f"Bearer {self.API_KEY}",
            "Content-Type": "application/json"
        }

        # We use "response_format": {"type": "json_object"} which is widely supported
        # and safer than passing the full Pydantic schema.
        payload = {
            "model": PERPLEXITY_MODEL,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": json.dumps(questions)}
            ],
            "response_format": {"type": "json_object"},
            "temperature": 0.1
        }

        try:
            response = requests.post(url=self.API_URL, headers=headers, json=payload).json()

            # --- ERROR HANDLING ---
            if "error" in response:
                logger.error(f"API Error: {response['error'].get('message', response['error'])}")
                return {}
            
            if "choices" not in response:
                logger.error(f"Unexpected response format: {response}")
                return {}
            # ----------------------

            content = response["choices"][0]["message"]["content"]

            # Clean up Markdown if the model ignores the "No Markdown" rule
            if content.strip().startswith("```"):
                content = content.replace("```json", "").replace("```", "")

            return json.loads(content.strip())

        except Exception as e:
            logger.error(f"Connector Exception: {e}")
            return {}
