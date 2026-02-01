# llm.py


# --------------------
# Provider handlers
# --------------------

def _groq(model, temperature, **kwargs):
    from langchain_groq import ChatGroq
    return ChatGroq(
        model=model,
        temperature=temperature,
        **kwargs,
    )


def _not_implemented(_, __, **___):
    raise NotImplementedError("LLM provider not implemented yet")


# --------------------
# Registry
# --------------------

_PROVIDERS = {
    "groq": _groq,
    "openai": _not_implemented,
    "gemini": _not_implemented,
    "local": _not_implemented,
}


# --------------------
# Public API
# --------------------

def get_llm(
        provider: str | None = None,
        model: str | None = None,
        temperature: float = 0.0,
        **kwargs,
):
    """
    Simple LLM factory.
    """

    # defaults live here (easy to see, easy to change)
    if provider is None or model is None:
        provider = "groq"
        model = "llama-3.1-8b-instant"

    provider = provider.lower()

    if provider not in _PROVIDERS:
        raise ValueError(f"Unknown provider: {provider}")

    return _PROVIDERS[provider](
        model,
        temperature,
        **kwargs,
    )
