from googletrans import Translator

def translate_text(text, dest='en'):
    translator = Translator()
    translated_text = translator.translate(text, dest=dest)
    return translated_text.text

# Texto em português
texto = "Olá, como você está?"

# Traduzindo para inglês
texto_traduzido = translate_text(texto, dest='en')

print("Texto original em português:", texto)
print("Texto traduzido para inglês:", texto_traduzido)
