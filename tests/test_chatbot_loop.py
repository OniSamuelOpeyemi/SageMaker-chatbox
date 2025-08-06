# test_chatbot_loop.py

import unittest
from chatbot_loop import get_bot_response, responses, fallback_responses


class TestSageBot(unittest.TestCase):

    def test_known_input_hello(self):
        user_input = "hello"
        response = get_bot_response(user_input)
        self.assertIn(response, responses["hello"])

    def test_known_input_joke(self):
        user_input = "tell me a joke"
        response = get_bot_response(user_input)
        self.assertIn(response, responses["joke"])

    def test_fallback_input(self):
        user_input = "what is the meaning of life?"
        response = get_bot_response(user_input)
        self.assertIn(response, fallback_responses)

    def test_exit_input_quit(self):
        response = get_bot_response("quit")
        self.assertEqual(response, "í±‹ Bye! Have a great day!")

    def test_exit_input_end(self):
        response = get_bot_response("end")
        self.assertEqual(response, "í±‹ Bye! Have a great day!")

    def test_case_insensitive_input(self):
        response = get_bot_response("HeLLo")
        self.assertIn(response, responses["hello"])


if __name__ == '__main__':
    unittest.main()
