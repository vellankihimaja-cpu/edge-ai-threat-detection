# Edge AI–Based Cyber Threat Detection Framework

## Overview
This project implements an Edge AI-based intrusion detection system for cloud-connected environments. The system performs real-time threat classification at the edge using a machine learning model and forwards alerts to Elasticsearch for centralized storage and visualization via Kibana.

---

## Architecture

User Input  
↓  
FastAPI Edge Service (ML Model Inference)  
↓  
Prediction Generated  
↓  
Elasticsearch Index (edge-alerts)  
↓  
Kibana Visualization  

---

## Environment Specifications

Operating System:
- macOS (Tested on Apple Silicon M4)
- Compatible with Linux

Software Versions:
- Python 3.10
- Docker Desktop 29.x
- Elasticsearch 8.5.0
- Kibana 8.5.0

Python Dependencies:
- pandas
- scikit-learn
- fastapi
- uvicorn
- joblib

---

## Getting Started

1. Clone repository:

git clone https://github.com/vellankihimaja-cpu/edge-ai-threat-detection.git
cd edge-ai-threat-detection


2. Start infrastructure:

docker compose up --build


3. Access services:
- API Docs: http://localhost:8000/docs
- Elasticsearch: http://localhost:9200
- Kibana: http://localhost:5601

---

## MVP Achieved

- Real-time prediction endpoint operational
- Alert successfully ingested into Elasticsearch
- Index pattern created in Kibana
- End-to-end detection-to-storage pipeline validated

---

## Known Challenges

- Model class imbalance
- False positive tuning
- Threshold optimization
- Kubernetes scalability (future phase)

---

## Future Work

- Automatic alert push from API to Elasticsearch
- Precision/Recall evaluation
- Kubernetes deployment
- Dashboard visualization improvements
