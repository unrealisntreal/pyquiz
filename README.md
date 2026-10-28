# pyquiz
A fun and lightweight python quiz loader, tested in Python `3.14`.

## How to use
Install the required dependencies.

- 💻 Windows
```bash
py -m pip install -r requirements.txt
```

- 🐧 On Linux / 🍎 MacOS
```bash
pip install -r requirements.txt
```

Launch the program.

```bash
py pyquiz
```

## Make your own quiz!
You can format your quizzes in two different ways.

Two examples can be found in `quizzes/` and be tested within the application.

- **Modern Format `.json`**
```json
{
    "name": "The Ultimate Math Test",
    "author": "unrealisntreal",
    "questions": [
        {
            "text": "What's 1+1?",
            "choices": [
                {
                    "text": "2",
                    "correct": true,
                    "required": true
                },
                {
                    "text": "3 - 1",
                    "correct": true
                },
                {
                    "text": "4",
                    "correct": false,
                    "feedback": "Why the hell would 1+1 = 4?"
                }
            ]
        },
        {
            "text": "Is 1/0 a valid mathematical operation?",
            "choices": [
                {
                    "text": "No",
                    "correct": true,
                    "feedback": "Good job!"
                },
                {
                    "text": "Yes",
                    "correct": false
                }
            ]
        },
        {
            "text": "Pick a fraction equal to 4/3",
            "choices": [
                {
                    "text": "6/4",
                    "correct": false
                },
                {
                    "text": "8/6",
                    "correct": true
                }
            ]
        }
    ]
}
```

- **Legacy Format `.txt`**
```
Q|How many minutes in an hour?
A|60|V
A|30|X

Q|How many seconds in an minute?
A|60|V
A|15|X
A|120|X|120 seconds is equal to 2 minutes!

Q|How many days in a month?
A|29|V
A|31|V
A|30|V
A|28|X
```

> [!WARNING]
> Legacy Format does not support the quiz `name`, `author` and `required` field!
