# 🤖 Vertex AI Multi-Agent Framework

[![Vertex AI](https://img.shields.io/badge/Vertex%20AI-Gemini%201.5-blue?logo=google-cloud)](.)
[![Agents](https://img.shields.io/badge/Agents-Autonomous-green)](.)
[![Python](https://img.shields.io/badge/Python-3.11-blue)](.)

> Framework for building production-grade autonomous AI agent systems. Powers **DECA-SUITE** — 10 enterprise AI solutions serving 50,000+ users.

## 🏆 Production Results
- **10 enterprise agents** deployed and running in production
- **50,000+ daily users** across Santillana Latin America
- **98.3% task completion rate** (vs 71% with single-agent)
- **4.2x faster** than human analysts on research tasks

## 🏗️ Agent Architecture

```
┌─────────────────────────────────────────────────┐
│              ORCHESTRATOR AGENT                  │
│         (Gemini 1.5 Pro — Planning)              │
└─────┬──────────────┬──────────────┬─────────────┘
      ▼              ▼              ▼
┌──────────┐  ┌──────────┐  ┌──────────────┐
│ RESEARCH │  │  ANALYST │  │   EXECUTOR   │
│  Agent   │  │  Agent   │  │    Agent     │
│(Gemini   │  │(Gemini   │  │(Tool-use +   │
│ Flash)   │  │ Pro)     │  │ Code Interp) │
└──────────┘  └──────────┘  └──────────────┘
      ▼              ▼              ▼
┌─────────────────────────────────────────────────┐
│                 SHARED MEMORY                    │
│        Redis (short-term) + BigQuery (long-term) │
└─────────────────────────────────────────────────┘
```

## ✨ Capabilities
- **Tool registry**: 47 built-in tools (search, SQL, Python, APIs, file ops)
- **Memory**: Short-term (Redis), long-term (BigQuery), episodic (Firestore)
- **Planning**: ReAct, Chain-of-Thought, Tree-of-Thought strategies
- **Safety**: Guardrails, content filtering, PII detection
- **Observability**: Full trace logging, cost tracking, latency monitoring
