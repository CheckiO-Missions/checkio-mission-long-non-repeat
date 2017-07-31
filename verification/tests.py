"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": "aaaaa",
            "answer": 'a'
        },
        {
            "input": "abdjwawk",
            "answer": 'abdjw'
        },
        {
            "input": "abcabcffab",
            "answer": 'abcf'
        }
    ],
    "Extra": [
        {
            "input": "ccccc",
            "answer": 'c'
        },
        {
            "input": "afafafaf",
            "answer": 'af'
        },
        {
            "input": "abcabcfabcabc",
            "answer": 'abcf'
        },
        {
            "input": "",
            "answer": ''
        },
        {
            "input": "w",
            "answer": 'w'
        },
        {
            "input": "wq",
            "answer": 'wq'
        },
        {
            "input": "dfghj",
            "answer": 'dfghj'
        },
        {
            "input": "fghfhy",
            "answer": 'fgh'
        },
        {
            "input": "fghfrtyfgh",
            "answer": 'ghfrty'
        }
    ]
}
