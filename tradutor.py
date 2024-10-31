from deep_translator import GoogleTranslator

def translate_text(text, target_lang='en'):
    translator = GoogleTranslator(source='auto', target=target_lang)
    return translator.translate(text)

# Texto em português
texto = "Olá, como você está?"

# Traduzindo para inglês
texto_traduzido = translate_text(texto, target_lang='en')

print("Texto original em português:", texto)
print("Texto traduzido para inglês:", texto_traduzido)

