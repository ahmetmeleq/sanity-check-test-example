import answer

JUDGE_RECORD = "heads"

def test_correct_side():
    assert answer.ANSWER == JUDGE_RECORD, (
        f"Expected {JUDGE_RECORD!r}, got {answer.ANSWER!r}"
    )
