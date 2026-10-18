
from guardrails import Guard
from guardrails.hub import ValidLength


def validate_input_with_library(text, max_chars):
    guard = Guard().use(
        ValidLength(min=1, max=max_chars, on_fail="exception")
    )

    result = guard.validate(text)
    return result.validated_output


def validate_output_with_library(text, max_chars):
    guard = Guard().use(
        ValidLength(min=1, max=max_chars, on_fail="exception")
    )

    result = guard.validate(text)
    return result.validated_output
