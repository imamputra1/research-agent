from litellm import completion
from src.core import config

_PROVIDERS = {
    "openclaw": {
        "api_base": config.OPENCLAW_BASE_URL,
        "api_key": config.KIMI_API_KEY,
        "prefix": "openai",
    },
    "openrouter": {
        "api_base": None,
        "api_key": config.OPENROUTER_API_KEY,
        "prefix": "openrouter",
    },
}


def ask(
    prompt: str,
    system: str = "You are a helpful research assistant.",
    model: str | None = None,
    provider: str | None = None,
    temperature: float = 0.7,
    max_tokens: int = 256,
) -> str:
    """Send a chat completion request via LiteLLM."""
    p = provider or config.DEFAULT_PROVIDER
    cfg = _PROVIDERS[p]

    model_id = f"{cfg['prefix']}/{model or config.DEFAULT_MODEL}"

    resp = completion(
        model=model_id,
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": prompt},
        ],
        api_base=cfg["api_base"],
        api_key=cfg["api_key"] or "sk-no-key",
        temperature=temperature,
        max_tokens=max_tokens,
    )
    return resp.choices[0].message.content
