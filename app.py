
import streamlit as st

from src.config import MAX_INPUT_CHARS, MAX_OUTPUT_CHARS
from src.library_guardrails import (
    validate_input_with_library,
    validate_output_with_library
)

from src.library_security import (
    mask_pii_with_library,
    check_prompt_injection_with_library
)


from src.guardrails import mask_pii, check_prompt_injection
from src.email_rewriter import rewrite_email


st.set_page_config(page_title="MailMate AI", page_icon="✉️")

st.title("MailMate AI")
st.write("Rewrite emails with AI-powered guardrails.")

tone = st.selectbox(
    "Choose Email Tone",
    ["Professional", "Friendly", "Formal", "Concise"]
)

email_text = st.text_area(
    "Enter your email",
    height=200,
    max_chars=MAX_INPUT_CHARS
)

if st.button("Rewrite Email"):
    try:
        validated_email = validate_input_with_library(#Input Validateion#1 with use custom Python code 
            email_text, MAX_INPUT_CHARS
        )

        # OPTION A: Custom Python implementation
        check_prompt_injection(validated_email) #Input Validateion#2 with use custom Python code
        #masked_email = mask_pii(validated_email) #Input Validateion#3 with use custom Python code

        # OPTION B: Guardrails AI security validators
        #check_prompt_injection_with_library(validated_email)
        masked_email = mask_pii_with_library(validated_email)  

        #Secret and credential detection -Not implemented
        #Malicious content and instruction detection -Implemented DetectJailbreak
        #Input type and content validation -Partially implemented — input length validation only
        #Unsafe content screening - Not implemented
        #Sensitive identifier detection -Partially implemented — email addresses and phone numbers are configured for PII masking
        #Input abuse and resource limits -Partially implemented — maximum input length limit only; no rate limiting

        with st.expander("View data sent to the LLM"):
            st.text_area(
                "Masked input",
                value=masked_email,
                height=200,
                disabled=True
            )

        rewritten_email = rewrite_email(masked_email, tone)

        # Output Guardrail #1: Mask PII in generated output
        rewritten_email = mask_pii_with_library(rewritten_email)

        # Output Guardrail #2: Validate output length
        rewritten_email = validate_output_with_library(
            rewritten_email, MAX_OUTPUT_CHARS
        )

        # Output Guardrail #3: Ensure output is not empty
        if not rewritten_email.strip():
            raise ValueError("The AI generated an empty email.")
        
        #PII leakage detection - Implemented, with limitations
        #Output format validation -Not implemented
        #Tone validation - Not implemented
        #Original meaning preservation - Not implemented
        #Unsafe content detection - Not implemented
        #Secret and credential detection - Not implemented
        
        st.subheader("Rewritten Email")
        st.text_area(
            "Final email",
            value=rewritten_email,
            height=200
        )

        st.download_button(
            "Download Rewritten Email",
            data=rewritten_email,
            file_name="rewritten_email.txt",
            mime="text/plain"
        )

    except Exception as error:
        st.error(str(error))
