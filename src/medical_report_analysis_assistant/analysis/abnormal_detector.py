from medical_report_analysis_assistant.models.report_models import MedicalReport


def detect_abnormal_values(report: MedicalReport):
    abnormal_results = []

    for lab in report.laboratory_results:
        if lab.reference_range is None:
            continue

        try:
            value = float(lab.value)
        except (ValueError, TypeError):
            continue

        reference = lab.reference_range.strip()

        # Less than
        if reference.startswith("<"):
            limit = float(reference.replace("<", "").split()[0])

            if value >= limit:
                abnormal_results.append({
                    "test_name": lab.test_name,
                    "value": value,
                    "unit": lab.unit,
                    "reference_range": lab.reference_range,
                    "status": "Above reference target",
                })

        # Greater than or equal to
        elif reference.startswith("≥"):
            limit = float(reference.replace("≥", "").split()[0])

            if value < limit:
                abnormal_results.append({
                    "test_name": lab.test_name,
                    "value": value,
                    "unit": lab.unit,
                    "reference_range": lab.reference_range,
                    "status": "Below reference target",
                })

        # Numeric range: e.g. 70–99
        elif "–" in reference:
            lower, upper = reference.split("–")

            lower = float(lower.strip())
            upper = float(upper.strip())

            if value < lower or value > upper:
                abnormal_results.append({
                    "test_name": lab.test_name,
                    "value": value,
                    "unit": lab.unit,
                    "reference_range": lab.reference_range,
                    "status": "Outside reference range",
                })

    return abnormal_results