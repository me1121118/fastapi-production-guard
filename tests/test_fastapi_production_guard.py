import pytest
from fastapi import FastAPI
from fastapi_production_guard import audit_production_app

def test_production_guard():
    # Insecure configuration
    insecure_app = FastAPI(debug=True, docs_url="/docs")
    report_bad = audit_production_app(insecure_app, environment="production", secret_key="changeme")
    assert report_bad.is_safe is False
    assert len(report_bad.issues) >= 2

    # Secure production configuration
    secure_app = FastAPI(debug=False, docs_url=None, redoc_url=None)
    report_good = audit_production_app(
        secure_app,
        environment="production",
        secret_key="a-very-long-secure-random-cryptographic-key-32-chars"
    )
    assert report_good.is_safe is True
    assert len(report_good.issues) == 0
