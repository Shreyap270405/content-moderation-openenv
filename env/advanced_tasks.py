ADVANCED_TASKS = {
    "easy": [
        {"content": "You are stupid", "label": "toxic", "correct_action": "remove", "sentiment": "negative", "flags": 2},
        {"content": "Thanks for your help!", "label": "safe", "correct_action": "allow", "sentiment": "positive", "flags": 0},
        {"content": "I appreciate your effort", "label": "safe", "correct_action": "allow", "sentiment": "positive", "flags": 0}
    ],
    "medium": [
        {"content": "Nice job breaking it again genius 🙄", "label": "abusive", "correct_action": "warn", "sentiment": "negative", "flags": 1},
        {"content": "Buy followers cheap!!!", "label": "spam", "correct_action": "remove", "sentiment": "neutral", "flags": 2},
        {"content": "Visit my profile for exclusive content 😉", "label": "spam", "correct_action": "warn", "sentiment": "neutral", "flags": 2}
    ],
    "hard": [
        {"content": "Click this scam link idiot http://fake.com", "label": "spam", "correct_action": "remove", "sentiment": "negative", "flags": 3},
        {"content": "You are such an id!ot 😂", "label": "toxic", "correct_action": "warn", "sentiment": "negative", "flags": 2},
        {"content": "ये क्या बेकार चीज है", "label": "abusive", "correct_action": "warn", "sentiment": "negative", "flags": 1},
        {"content": "Free crypto giveaway send wallet details now", "label": "spam", "correct_action": "remove", "sentiment": "neutral", "flags": 3}
    ]
}
