import logging
from transformers import AutoModelForCausalLM, AutoTokenizer

class AISummarizer:
    def __init__(self, model_name='your_fine_tuned_model'):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(model_name)
        self.logger = logging.getLogger(__name__)

    def generate_policy_summary(self, policy_text):
        try:
            inputs = self.tokenizer(policy_text, return_tensors='pt')
            summary_ids = self.model.generate(inputs['input_ids'], max_length=150)
            summary = self.tokenizer.decode(summary_ids[0], skip_special_tokens=True)
            return summary
        except Exception as e:
            self.logger.error(f'Error generating summary: {e}')
            return 'Error generating summary.'

    def generate_plain_language_explanation(self, summary):
        try:
            inputs = self.tokenizer(summary, return_tensors='pt')
            explanation_ids = self.model.generate(inputs['input_ids'], max_length=50)
            explanation = self.tokenizer.decode(explanation_ids[0], skip_special_tokens=True)
            return explanation
        except Exception as e:
            self.logger.error(f'Error generating explanation: {e}')
            return 'Error generating explanation.'

if __name__ == '__main__':
    summarizer = AISummarizer()
    # Example usage:
    # policy_text = 'Your policy text here...'
    # summary = summarizer.generate_policy_summary(policy_text)
    # explanation = summarizer.generate_plain_language_explanation(summary)