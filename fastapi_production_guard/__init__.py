from dataclasses import dataclass, field
from typing import List, Optional
from fastapi import FastAPI

INSECURE_SECRET_KEYWORDS = {
    "secret", "changeme", "admin", "password", "test", "demo", "123456", "dev"
}

@dataclass
class AuditResult:
    is_safe: bool
    issues: List[str] = field(default_factory=list)

def audit_production_app(
    app: FastAPI,
    environment: str = "production",
    secret_key: Optional[str] = None,
) -> AuditResult:
    """Audit FastAPI application configuration for production security risks."""
    issues = []
    env_lower = environment.strip().lower()

    if env_lower in ("production", "prod"):
        # 1. Check debug mode
        if getattr(app, "debug", False):
            issues.append("FastAPI debug mode is enabled in production!")

        # 2. Check secret key strength
        if secret_key:
            if len(secret_key) < 32:
                issues.append(f"Secret key is too short ({len(secret_key)} chars). Recommended: >= 32 chars.")
            if secret_key.lower() in INSECURE_SECRET_KEYWORDS:
                issues.append(f"Insecure default secret key detected: '{secret_key}'")

        # 3. Check OpenAPI / Docs exposure
        if app.docs_url is not None or app.redoc_url is not None:
            issues.append("Interactive API documentation (Swagger/ReDoc) is exposed in production.")

    return AuditResult(is_safe=len(issues) == 0, issues=issues)
