# fastapi-production-guard

[![PyPI version](https://img.shields.io/badge/pypi-v0.1.0-blue.svg)](https://pypi.org/project/fastapi-production-guard/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)

Production readiness checklist and security audit middleware for FastAPI. Halts startup if insecure secrets, debug flags, or docs are exposed in production.

---

## 🚀 Features

- 🔒 **Insecure Secret Detection**: Detects default dummy keys (`secret`, `password`, `changeme`).
- 🚨 **Debug Mode Blocker**: Alerts if `app.debug = True` in production environments.
- 📋 **Docs Exposure Guard**: Warns if Swagger `/docs` and `/redoc` are left exposed on public APIs.

---

## 📦 Installation

```bash
pip install fastapi-production-guard
```

---

## 🛠️ Quickstart

```python
from fastapi import FastAPI
from fastapi_production_guard import audit_production_app

app = FastAPI()

# Audit app settings during startup
audit_report = audit_production_app(
    app=app,
    environment="production",
    secret_key="my-super-secret-production-key-here"
)

if not audit_report.is_safe:
    print("Security warnings:", audit_report.issues)
```

---

## ☕ Support My Studies / Buy Me a Coffee

I am an independent developer and student building open-source developer productivity tools. If this production security auditor protected your deployments from leaks, please consider supporting my studies:

- ☕ **Buy Me a Coffee:** [buymeacoffee.com/kcidi4148](https://buymeacoffee.com/kcidi4148)
- ⭐ **Star this repository** on GitHub!

---

## 📄 License

MIT License. See [LICENSE](LICENSE) for details.
