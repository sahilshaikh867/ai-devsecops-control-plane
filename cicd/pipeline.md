# CI/CD Pipeline Design

## Purpose
This document represents the CI/CD layer integration with the AI DevSecOps Control Plane.

## Pipeline Stages

1. Source Code Commit
   - Developer pushes code to repository

2. Build & Test
   - Application is built
   - Unit and integration tests are executed

3. Security Scanning
   - Static code analysis
   - Dependency vulnerability scanning
   - Container image scanning (future scope)

4. AI Risk Evaluation (Control Plane)
   - CI/CD pipeline sends context to AI risk API
   - Risk score and deployment decision are returned

5. Deployment Decision
   - ALLOW → normal deployment
   - CANARY → limited rollout
   - BLOCK → deployment stopped

6. Audit Logging
   - All decisions are logged for compliance

## Notes
- CI/CD execution is simulated in this project
- Design aligns with Jenkins / GitHub Actions pipelines
- Control plane ensures security is enforced before production
