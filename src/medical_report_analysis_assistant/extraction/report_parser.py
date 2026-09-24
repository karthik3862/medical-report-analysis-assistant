from medical_report_analysis_assistant.llm.llm_client import get_llm
from medical_report_analysis_assistant.llm.prompts import EXTRACTION_PROMPT
from medical_report_analysis_assistant.models.report_models import MedicalReport


def parse_report(text: str) -> MedicalReport:
    llm = get_llm()

    structured_llm = llm.with_structured_output(MedicalReport)

    prompt = f"""
{EXTRACTION_PROMPT}

Here is the medical report:

--- BEGIN REPORT ---

{text}

--- END REPORT ---
"""

    result = structured_llm.invoke(prompt)

    return result