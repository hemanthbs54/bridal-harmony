# Problem Summary – Bridal Harmony (Applied AI Decision System)

## 1. Problem Statement

High-stakes personalization decisions are often subjective, inconsistent, and difficult to trust when multiple constraints must be satisfied simultaneously.

In the luxury wedding context, even a single individual’s outfit selection involves:
- physical attributes (skin tone, brightness, visual balance)
- personal preferences
- high emotional and financial stakes
- the need for confidence before entering a boutique

Today, these decisions rely heavily on human intuition and trial-and-error, which does not scale and cannot consistently explain *why* a particular choice works.

The core problem addressed in this MVP is converting a **subjective styling decision** into a **deterministic, explainable process** using applied AI.

---

## 2. Why This Is a Hard Problem

This is not a simple recommendation task.

Even at the individual level, the system must handle:
- noisy visual inputs (photos taken under different lighting conditions)
- ambiguous skin tone signals
- subjective preferences that must be respected
- the need for transparent explanations, not just outputs

Pure ML ranking is insufficient because decisions must be **explainable and trustworthy**, not just statistically likely.

This makes the problem **constraint-driven and decision-focused**, rather than purely predictive.

---

## 3. Solution Overview

I built an **Applied AI decision engine** that combines:
- computer vision–based analysis
- deterministic rule logic
- LLM-based explanation generation

The system is designed to **filter incorrect choices before recommending anything**, reducing decision anxiety rather than overwhelming the user with options.

---

## 4. System Architecture (Current MVP)

### Component 1: Input & Validation Layer
- Accepts up to three user-uploaded images
- Performs basic safety and format validation
- Normalizes inputs for downstream analysis

---

### Component 2: Vision Analysis Engine
- Extracts measurable skin features:
  - brightness
  - redness
  - approximate skin tone
- Designed to be robust to real-world photo variability

---

### Component 3: Deterministic Material Logic Engine
- Applies rule-based logic to map skin features to suitable fabric types
- Ensures recommendations follow predefined styling constraints
- Filters out incompatible materials

---

### Component 4: Explanation Engine (LLM-Assisted)
- Uses a large language model to generate:
  - human-readable explanations
  - reasoning behind each recommendation
- Focuses on transparency rather than persuasion

---

## 5. Design for Extension (Agentic Roadmap)

While the current MVP focuses on a single individual, the system is **intentionally designed for extension** into:
- multi-agent decomposition (analysis, harmony, feasibility)
- multi-entity optimization (bride + groom coordination)
- execution feasibility checks (inventory, tailoring constraints)

These extensions follow the same decision-first, constraint-driven principles demonstrated in the MVP.

---

## 6. Current Status

- End-to-end MVP implemented
- Vision analysis + deterministic decision logic operational
- Explainable outputs generated via LLM
- Working Streamlit application demonstrating real-world usage

Repository contains:
- core logic modules
- executable application
- example decision flows

---

## 7. Key Takeaway

This project demonstrates how **applied AI systems** can convert subjective, high-stakes decisions into **explainable, constraint-aware outcomes**.

The same architectural approach can be extended to more complex personalization, configuration, and optimization problems where trust and correctness matter more than raw prediction.
