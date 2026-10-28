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
    "name": "My Awesome Quiz",
    "author": "John",
    "questions": [
        {
            "text": "What's 1+1?",
            "choices": [
                {
                    "text": "2",
                    "correct": true
                },
                {
                    "text": "4",
                    "correct": false
                }
            ]
        },
        {
            "text": "How many days in a month?",
            "choices": [
                {
                    "text": "29",
                    "correct": true,
                    "required": true
                },
                {
                    "text": "31",
                    "correct": true,
                    "required": true
                },
                {
                    "text": "30",
                    "correct": true,
                    "required": true
                },
                {
                    "text": "28",
                    "correct": false,
                    "required": false
                }
            ]
        }
    ]
}
```

- **Legacy Format `.txt`**
```
Q|What's 1+1?
A|2|V
A|4|X

Q|How many days in a month?
A|29|V
A|31|V
A|30|V
A|28|X
```

> [!WARNING]
> Legacy Format does not support the quiz `name` and `author` field!
