from medical_report_analysis_assistant.ingestion.pdf_loader import (
    extract_text_from_pdf,
)

from medical_report_analysis_assistant.extraction.report_parser import (
    parse_report,
)

from medical_report_analysis_assistant.analysis.abnormal_detector import (
    detect_abnormal_values,
)


def main():
    # Path to the medical report PDF
    pdf_path = "data/input/medical_report.pdf"

    # --------------------------------------------------
    # 1. Extract text from PDF
    # --------------------------------------------------
    text = extract_text_from_pdf(pdf_path)

    print("\n========== RAW TEXT ==========\n")
    print(text)

    # --------------------------------------------------
    # 2. Extract structured information using Grok
    # --------------------------------------------------
    report = parse_report(text)

    print("\n========== STRUCTURED REPORT ==========\n")
    print(report.model_dump_json(indent=2))

    # --------------------------------------------------
    # 3. Detect abnormal laboratory values
    # --------------------------------------------------
    abnormal_values = detect_abnormal_values(report)

    print("\n========== ABNORMAL VALUES ==========\n")

    if not abnormal_values:
        print("No abnormal values detected.")

    else:
        for item in abnormal_values:
            print(f"Test: {item['test_name']}")
            print(f"Value: {item['value']} {item['unit']}")
            print(f"Reference: {item['reference_range']}")
            print(f"Status: {item['status']}")
            print("-" * 50)


if __name__ == "__main__":
    main()