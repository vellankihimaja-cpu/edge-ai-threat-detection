# Development Log – Edge AI Threat Detection

---

## Himaja – Feb 26

Action Attempted:
Started infrastructure using:
docker compose up --build

Output:
All containers started successfully.
- FastAPI running on port 8000
- Elasticsearch running on port 9200
- Kibana running on port 5601

Issue Encountered:
Initial error: index_not_found_exception for "edge-alerts"

Resolution:
Created index manually using curl POST request.
Verified document ingestion via Kibana Index Management.

Next Step:
Implement automatic Elasticsearch logging from API layer.
Tune model to reduce false positives.

---

## Team Notes

MVP Successfully Achieved:
- End-to-end prediction pipeline operational
- Alerts stored in Elasticsearch
- Data view created in Kibana
- Index visible and searchable

Current Technical Debt:
- Model predicts 1 for most inputs (possible class imbalance)
- No automated alert push from API (manual curl used)

Planned Improvements:
- Evaluate precision/recall
- Add probability thresholding
- Implement auto-alert ingestion
- Prepare Kubernetes deployment
