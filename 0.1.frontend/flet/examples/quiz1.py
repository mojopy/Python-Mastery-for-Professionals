import flet as ft

questions = [
    {"question": "What is the capital of France?", "options": ["Paris", "London", "Berlin"], "answer": "Paris"},
    {"question": "What is 2 + 2?", "options": ["3", "4", "5"], "answer": "4"},
    {"question": "Which planet is known as the Red Planet?", "options": ["Earth", "Mars", "Jupiter"], "answer": "Mars"}
]

current_question_index = 0

def main(page: ft.Page):
    global current_question_index

    def next_question():
        global current_question_index
        if current_question_index < len(questions) - 1:
            current_question_index += 1
        else:
            current_question_index = 0

        question = questions[current_question_index]
        question_label.value = question["question"]
        for i, option in enumerate(option_buttons):
            option.text = question["options"][i]
        page.update()

    def check_answer(e):
        if e.control.text == questions[current_question_index]["answer"]:
            next_question()
        else:
            print("Wrong answer!")

    question_label = ft.Text(value=questions[current_question_index]["question"], size=20)

    option_buttons = [
        ft.ElevatedButton(text=option, on_click=check_answer) for option in questions[current_question_index]["options"]
    ]

    page.controls.append(question_label)
    page.controls.extend(option_buttons)
    page.update()

ft.app(target=main)
