# System Design – Bridal Harmony (Applied AI MVP)

## 1. Design Goals

The system is designed to:
- convert subjective styling decisions into deterministic outcomes
- reduce decision anxiety through constraint-based filtering
- provide transparent, explainable reasoning
- remain extensible to more complex decision systems

The focus is correctness and trust, not content generation.

---

## 2. High-Level Architecture

The MVP follows a modular, pipeline-based architecture with clear separation of concerns:

Input → Vision Analysis → Decision Logic → Explanation → Output

Each module is designed to later evolve into a specialized agent.

---

## 3. Component Breakdown

### 3.1 Input & Validation Layer
- Accepts up to three user-uploaded images
- Validates image format, size, and safety
- Normalizes images for consistent analysis

Purpose:
Ensure reliable downstream processing despite real-world input variability.

---

### 3.2 Vision Analysis Engine
Implemented in: `skin_analysis.py`

Extracts:
- brightness
- redness
- approximate skin tone

Techniques:
- OpenCV image processing
- pixel-level aggregation
- normalization across multiple images

Purpose:
Convert unstructured visual data into measurable signals.

---

### 3.3 Deterministic Decision Logic Engine
Implemented in: `material_logic.py`

Responsibilities:
- map skin features to compatible fabric categories
- enforce predefined styling constraints
- filter incompatible materials

This engine is rule-based by design to ensure:
- repeatability
- correctness
- auditability

---

### 3.4 Explanation Engine (LLM-Assisted)
Implemented in: `explanation.py`

- Uses Google Gemini to generate natural-language explanations
- Receives structured inputs (metrics + selected materials)
- Outputs human-readable reasoning

Important:
The LLM **does not make decisions** — it explains them.

---

### 3.5 Frontend & Output Layer
Implemented in: `app.py`

- Displays original images and extracted metrics
- Shows filtered material recommendations
- Presents AI-generated explanations
- Allows users to download recommendations

---

## 4. Failure Handling & Constraints

- Image variability handled via normalization
- User intent always preserved
- Deterministic rules override ambiguous AI signals
- No hidden or non-explainable decisions

---

## 5. Why This Is Applied GenAI

- Solves a real-world decision problem
- AI is used where signal extraction and explanation are needed
- Deterministic logic is used where correctness matters
- Outputs are explainable and reproducible

---

## 6. Extension Path (Planned)

The architecture is intentionally designed to evolve into:
- multi-agent orchestration
- multi-entity optimization (e.g., couple harmony)
- execution feasibility constraints (inventory, timelines)

These extensions build directly on the MVP’s decision-first foundation.
