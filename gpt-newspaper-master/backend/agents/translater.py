from datetime import datetime
from langchain.adapters.openai import convert_openai_messages
from langchain_openai import ChatOpenAI
import json  

class TranslaterAgent:
    
    def __init__(self):
        pass
    
    def translater(self, article: dict):
        prompt = [{
            "role": "system",
            "content": "Você é um jornalista que sabe traduzir artigos para portugûes do Brasil."
        }, {
            "role": "user",
            "content": f"""
            
            Hoje é {datetime.now().strftime('%d/%m/%Y')}
            
            {str(article)}
            
            Quero que os valores das chaves:
            
            title
            content
            paragraphs
            
            Quero que seja traduzido para português brasileiro. De forma que passe o conteudo de uma forma clara e o meis precisa o possivel.
            
            mande unicamente o arquivo json traduzido da maneira especificada.
            """
        }]

        lc_messages = convert_openai_messages(prompt)
        
        response = ChatOpenAI(model='gpt-4', max_retries=1).invoke(lc_messages).content
        
        try:
            translated_data = json.loads(response)  
        except json.JSONDecodeError:
            print("Erro ao decodificar a resposta JSON.")
            return {}  
        
        print("translater_article_data : ", translated_data)
        
        return translated_data  
    
    def run(self, article: dict):
        print("article_data", str(article))
        
        translation_result = self.translater(article)  
        if isinstance(translation_result, dict):
            article.update(translation_result)
        else:
            print("Erro: A tradução não retornou um dicionário.")
        
        return article
