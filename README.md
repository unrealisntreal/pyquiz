# pyquiz
A fun and lightweight python quiz loader.

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
You can format your quizes in two different ways.

#### JSON Format
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

#### Legacy Format
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

> [!warn] Legacy Format does not support the quiz name and author field!
