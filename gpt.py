import openai
API_key = 'Apik key'
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
