import json

"""
Constants
"""
UTF8 = 'utf-8'

FILE_NAME = 'questions.json'

QUESTION = 'question'
CHOICES = 'choices'
CORRECT = 'correct'
EXPLANATION = 'explanation'
SOURCES = 'sources'
TAGS = 'tags'
"""
Function
"""


def validate_question_format(index, data):
    """질문 str"""
    if not isinstance(data[QUESTION], str) or data[QUESTION] == "":
        value_error(index, QUESTION)

    """선택지 str[]"""
    if not isinstance(data[CHOICES], list):
        value_error(index, CHOICES)

    """정답 str"""
    if not isinstance(data[CORRECT], str) or data[CORRECT] == "":
        value_error(index, CORRECT)

    """문제 답에 대한 해설 str"""
    if not isinstance(data[EXPLANATION], str):
        value_error(index, EXPLANATION)

    """출처 str[]"""
    if not isinstance(data[SOURCES], list):
        value_error(index, SOURCES)

    """문제 유형 : OS, Network, Database, Java, JavaScript, Browser, Node.js, ... str[]"""
    if not isinstance(data[TAGS], list):
        value_error(index, TAGS)


def question_data(filename):
    with open(filename, 'r', encoding=UTF8) as file:
        return json.load(file)


def value_error(index, field):
    raise ValueError(f"{index}번째 index 문제의 {field} 값에 문제가 발견되었습니다.")


if __name__ == "__main__":
    for idx, datum in enumerate(question_data(FILE_NAME)):
        validate_question_format(idx, datum)
