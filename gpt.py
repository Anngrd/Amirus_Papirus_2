import openai
API_key = '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'
# Установите ваш API ключ
openai.api_key = API_key

def load_text_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

# Загрузка текста
text_content = load_text_from_file('правила _проживания_в_интернате.txt')
# Добавляем текст в правила для контекста
rules = [
    {"role": "system", "content": f"Вот информация, на основе которой ты будешь отвечать на вопросы,давать информацию по окредитованию частных лиц это ваша главная задача: {text_content}"}
]
chat_history = []
def get_text(prompt):
    global chat_history
    chat_history.append({"role": "user", "content": prompt})
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",  
        messages= rules + chat_history,
        max_tokens=1000,
        temperature=0.7,
    )
    return response['choices'][0]['message']['content']
    chat_history.append(response)