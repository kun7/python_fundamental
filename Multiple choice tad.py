from kuesioner import Question

question_prompt = [
    "What color are apples?\n(a)Red/Green\n(b)Purple\n(c)Orange\n\n",
    "What color are bananas?\n(a)Teal\n(b)Magenta\n(c)Yellow\n\n",
    "What color are strawberries?\n(a)Yellow\n(b)Red\n(c)Blue\n\n"


]

questions =[

        Question(question_prompt[0], "a"),
        Question(question_prompt[1], "c"),
        Question(question_prompt[2], "b"),
]

def run_test(questions):
            score = 0
            for Question in questions:

                answer= input(Question.prompt)

                if answer == Question.answer:
                        score += 1

            print("You got " + str(score) + "/" + str(len(questions)) + " Correct")


run_test(questions)