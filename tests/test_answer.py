import answer

def test_correct_side():
    assert answer.ANSWER in ("heads", "tails"), (
        f"ANSWER must be 'heads' or 'tails', got {answer.ANSWER!r}"
    )

def test_answer_is_set():
    assert answer.ANSWER != "", "ANSWER must not be empty"
