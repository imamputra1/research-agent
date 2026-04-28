from src.core.provider import ask


def test_kimi_hello():
    response = ask("Reply with exactly the word 'Hello' and nothing else.")
    print(f"\n[RESPONSE] {response}")
    assert "Hello" in response, f"Expected 'Hello', got: {response}"
