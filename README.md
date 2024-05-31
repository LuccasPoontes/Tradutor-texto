# Tradutor-texto
Este projeto é um tradutor de texto automático que utiliza a biblioteca googletrans para traduzir textos de uma língua para outra. O objetivo é fornecer uma maneira simples e rápida de traduzir textos diretamente no código Python, facilitando a internacionalização e a comunicação em vários idiomas.

# Tradutor de Texto Automático

## Descrição
Este projeto é um tradutor de texto automático desenvolvido em Python. Utilizando a biblioteca `googletrans`, é possível traduzir textos de uma língua para outra de maneira rápida e eficiente. Este tradutor pode ser útil em diversas aplicações, como internacionalização de softwares, comunicação multilinguística e aprendizado de idiomas.

## Funcionalidades
- Tradução de texto entre diversos idiomas suportados pelo Google Translate.
- Interface simples para integração com outros projetos em Python.
- Suporte para especificação do idioma de destino.

## Instalação
Para utilizar este projeto, você precisa ter o Python instalado em sua máquina. Siga os passos abaixo para instalar a biblioteca necessária:

1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/tradutor-texto-automatico.git
   cd tradutor-texto-automatico
   ```
### Instale a biblioteca googletrans:
``` pip install googletrans==4.0.0-rc1 ```

## Uso
Aqui está um exemplo de como utilizar o tradutor de texto:
```
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
```

## Licença
### Este projeto está licenciado sob a Licença MIT. Consulte o arquivo LICENSE para obter mais informações.

Este exemplo de README.md fornece uma descrição clara do projeto, suas funcionalidades, instruções de instalação e uso, além de informações sobre como contribuir para o projeto e a licença aplicável.




