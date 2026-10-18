
from guardrails import Guard
from guardrails_ai.detect_pii import DetectPII
from guardrails_ai.detect_jailbreak import DetectJailbreak


def mask_pii_with_library(text):
    guard = Guard().use(
        DetectPII(
            pii_entities=["EMAIL_ADDRESS", "PHONE_NUMBER"],
            on_fail="fix",
            use_local=True
        )
    )

    result = guard.validate(text)
    return result.validated_output


def check_prompt_injection_with_library(text):
    guard = Guard().use(
        DetectJailbreak(   #analyzes the supplied text for potential jailbreak attempts.
            threshold=0.9, #0-1 range, Lower is sensitive higher is less sensitive, default is 0.9
            on_fail="exception"
        )
    )

    result = guard.validate(text)
    return result.validated_output
