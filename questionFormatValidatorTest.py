import unittest

import questionFormatValidator


class MyTestCase(unittest.TestCase):
    def test_validate_pass(self):
        json = {
            "question": "employees 테이블의 hire_date 컬럼에 인덱스가 걸려 있다면 다음 쿼리는 인덱스를 사용할 수 있다.\nSELECT * FROM employees WHERE YEAR(hire_date) > 2005;",
            "choices": ["O", "X"],
            "correct": "O",
            "explanation": "함수를 사용해서 컬럼의 원래 값을 변경하면 인덱스를 적용할 수 없다. 인덱스를 사용하고 싶다면 다음과 같이 쿼리를 변경할 수 있다.\nSELECT * FROM employees WHERE hire_date > '2005-12-31';",
            "sources": [],
            "tags": ["DB"]
        }
        questionFormatValidator.validate_question_format(0, json)

    def test_validate_fail_wrong_type(self):
        choices_wrong_json = {
            "question": "employees 테이블의 hire_date 컬럼에 인덱스가 걸려 있다면 다음 쿼리는 인덱스를 사용할 수 있다.\nSELECT * FROM employees WHERE YEAR(hire_date) > 2005;",
            "choices": "O",
            "correct": "O",
            "explanation": "함수를 사용해서 컬럼의 원래 값을 변경하면 인덱스를 적용할 수 없다. 인덱스를 사용하고 싶다면 다음과 같이 쿼리를 변경할 수 있다.\nSELECT * FROM employees WHERE hire_date > '2005-12-31';",
            "sources": [],
            "tags": ["DB"]
        }
        self.assertRaises(ValueError, questionFormatValidator.validate_question_format, 0, choices_wrong_json)

    def test_validate_fail_empty(self):
        correct_empty_json = {
            "question": "employees 테이블의 hire_date 컬럼에 인덱스가 걸려 있다면 다음 쿼리는 인덱스를 사용할 수 있다.\nSELECT * FROM employees WHERE YEAR(hire_date) > 2005;",
            "choices": "O",
            "correct": "O",
            "explanation": "함수를 사용해서 컬럼의 원래 값을 변경하면 인덱스를 적용할 수 없다. 인덱스를 사용하고 싶다면 다음과 같이 쿼리를 변경할 수 있다.\nSELECT * FROM employees WHERE hire_date > '2005-12-31';",
            "sources": [],
            "tags": ["DB"]
        }
        self.assertRaises(ValueError, questionFormatValidator.validate_question_format, 0, correct_empty_json)


if __name__ == '__main__':
    unittest.main()
