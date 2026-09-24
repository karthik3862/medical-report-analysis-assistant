from pydantic import BaseModel, Field


class VitalSign(BaseModel):
    name: str
    result: str
    reference_range: str | None = None


class LabResult(BaseModel):
    test_name: str
    value: float | str
    unit: str | None = None
    reference_range: str | None = None


class MedicalReport(BaseModel):
    patient_name: str | None = None
    report_date: str | None = None

    vital_signs: list[VitalSign] = Field(default_factory=list)
    laboratory_results: list[LabResult] = Field(default_factory=list)