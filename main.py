from pypandoc import convert_text
from google import genai
from time import sleep
from os import mkdir


# GEMINI_API_KEY
API_KEY = "AIzaSyBftd0C_yf4KyD0Nk2Vt9YXSO3aBhmwDRk"

# The client gets the API key from the environment variable `GEMINI_API_KEY`.
client = genai.Client(api_key=API_KEY)


# Создание файла MarkDown с лекционным материалом
def writeMD( filename: str, text: str ):
    
    filename += ".md"
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write( text )
        
        print(f"Сгенерированный Markdown-отчет сохранен в файл '{filename}'")
    
    except IOError as e:
        print(f"Ошибка при сохранении файла: {e}")


def writeWord( filename: str, text: str ):
    filename += ".docx"

    convert_text(
        text,
        'docx',
        format="md",
        outputfile=filename,
        extra_args=['--standalone'] # --standalone создаст полный документ Word
    )

    print(f"Сгенерированный Markdown-отчет сохранен в файл '{filename}'")



# Текстовый промпт для отправки в нейронку
def sendPrompt( title: str ) -> str:
    
    prompt = f"""
Напиши образовательный лекционный материал по теме `{title}` в формате Markdown по следующему шаблону:

```
### Лекция
#### Тема лекции: [вставь тему]

Основные разделы образовательного материала:
1. Введение
2. Основные понятия
3. Примеры и пояснения
4. Практическое применение
5. Заключение

Текст образовательного материала:
[сформулируй развернутый текст с пояснениями, примерами и выводами по теме]
```
    """

    ### Ответ от нейронки
    return client.models.generate_content(
        model="gemini-2.5-flash", contents=prompt
    )


# Функция чтения тем из текстового файла
def readTheme( filename="data/theme.txt" ) -> list:

    themes = []

    with open( filename, "r", encoding='utf-8') as f:
        
        for line_number, line in enumerate(f, 1): # enumerate для получения номера строки
            # Каждая строка будет включать символ нового строки (\n) в конце,
            # если он присутствует в файле.
            # Для удаления пробельных символов (включая \n) можно использовать .strip()
            themes.append(f"{line_number}. {line.strip()}")

    return themes


def main():
    
    while True:

        # Получаем название дисциплины
        subject_name = input( "\nВведите название предмета: " )

        if subject_name == "q":
            break

        mkdir( subject_name )  # Создаем папку под дисциплину 
        sleep( 1 )

        themes = readTheme()   # Получаем темы

        for theme in themes:
            response = sendPrompt( theme )

            writeMD( f"{subject_name}/{theme}", response.text )
            writeWord( f"{subject_name}/{theme}", response.text )

            sleep( 3 )


if __name__ == '__main__':
    main()