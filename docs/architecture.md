# System Architecture – AI DevSecOps Control Plane

## Overview
The AI DevSecOps Control Plane is a web-based platform designed to control and govern software deployments using AI-driven risk evaluation. It acts as a decision layer between CI/CD pipelines and production environments.

## Architecture Components

### 1. Frontend (Web UI)
- Simple HTML + JavaScript dashboard
- Allows users to trigger deployment requests
- Allows users to request AI-based risk evaluation
- Communicates with backend via REST APIs

### 2. Backend (FastAPI)
- Exposes REST APIs for deployment control
- Validates all inputs using Pydantic schemas
- Acts as the central control plane

### 3. AI Risk Engine
- Rule-based AI logic for deployment risk scoring
- Evaluates:
  - Security criticality
  - Infrastructure instability
  - Peak traffic hours
  - Past deployment failures
- Produces decisions: ALLOW / CANARY / BLOCK

### 4. Audit & Governance Layer
- Logs every deployment and risk decision
- Ensures traceability and compliance
- Designed to integrate with centralized logging systems

## High-Level Flow
1. User triggers deployment via UI
2. Backend validates request
3. AI engine calculates risk score
4. Decision is generated
5. Action is logged for audit
6. Response is returned to user

## Design Rationale
- Separation of concerns between UI, logic, and decision-making
- API-first architecture for easy CI/CD integration
- Explainable AI decisions suitable for enterprise environments
