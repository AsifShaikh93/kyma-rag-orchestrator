Auto-Scaling RAG Orchestrator (Kyma + LangGraph)

A production-grade, latency-aware RAG pipeline built for high-concurrency environments. Unlike standard RAG demos, this project leverages Kubernetes-native autoscaling (KEDA) and Redis-based semantic caching to ensure high performance and cost efficiency.

🚀 Architecture Overview
This system is designed to handle variable traffic by decoupling inference logic from infrastructure scaling.

Key Engineering Features
Latency-Driven Autoscaling: Uses KEDA and Prometheus Gauges to scale worker pods based on real-time request latency rather than CPU usage.

Semantic Caching: Integrates RedisSemanticCache to intercept repetitive queries, reducing LLM API costs by ~70% and latency by ~90%.

Production Telemetry: Instrumented with custom Prometheus Gauges to track active concurrent requests, providing the metrics pipeline the data needed for proactive infrastructure scaling.

Secure Gateway: Managed via SAP Kyma APIRules (Istio) with JWT-based authentication and mTLS support.

System Flow
Technical Stack
Orchestration: SAP Kyma / Kubernetes

Autoscaling: KEDA (Kubernetes Event-Driven Autoscaling)

AI Framework: LangChain, LangGraph

Vector DB: Qdrant

Telemetry: Kyma MetricPipeline (OTLP/Prometheus)

Caching: Redis Cloud (Vector-enabled)

Deployment Requirements
Kyma Namespace: Must have istio-injection=enabled.

Telemetry Pipeline: A MetricPipeline configured to scrape pod metrics on port 8000.

Secrets Management: Environment variables provided via K8s Secrets.

Why this project stands out
Beyond the Script: Demonstrates deep knowledge of the "Day 2 Operations" of AI—security, scaling, and cost optimization.

Observability: Shows that you can build systems where you don't just "hope it works," but "know it works" via metric-driven alerts.