from openai import OpenAI

class Resumentexto:
    model_openia = "gpt-3.5-turbo"
    
    def __init__(self, api_key):
        self.api_key = api_key
        
    def resumen(self, texto, idioma):
        client = OpenAI(api_key=self.api_key)
        response = client.chat.completions.create(
            model=self.model_openia,
            messages=[
                {"role": "system", "content": f"Eres un asistente que puede leer un texto, resumirlo en 10 oraciones o menos, y luego traducirlo al idioma: {idioma}."},
                {"role": "user", "content": f"Resumen y traduce al {idioma} el siguiente texto:\n" + texto}
            ]
        )
        respuesta = response.choices[0].message['content']
        client.close()
        return respuesta




