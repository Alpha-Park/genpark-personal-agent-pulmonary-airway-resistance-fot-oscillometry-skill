---
name: genpark-personal-agent-pulmonary-airway-resistance-fot-oscillometry-skill
version: 1.0.0
description: Zero-dependency sovereign personal agent skill for calculating Forced Oscillation Technique (FOT / IOS) respiratory impedance, peripheral resistance (R5-R20), and reactance.
author: AlphaPark Inc.
license: Apache-2.0
tags:
  - personal-agent
  - ai-agent
  - openclaw
  - genpark
  - mcp
  - mcp-server
  - model-context-protocol
  - python
  - zero-dependency
  - wellness
  - productivity
  - production-ready
metadata:
  openclaw_compatible: true
  hermes_compatible: true
  zero_dependency: true
---

# Forced Oscillation Technique (FOT / IOS) Skill

A sovereign personal agent capability for assessing total and peripheral respiratory system impedance, effort-independent airway resistance ($R_5, R_{20}$), and small-airway narrowing via impulse oscillometry.

## Core Capabilities
- **Total vs Central Resistance**: Decomposes 5 Hz total respiratory resistance ($R_5$) and 20 Hz central large-airway resistance ($R_{20}$).
- **Peripheral Frequency Dependence ($R_5 - R_{20}$)**: Sensitive biomarker of subclinical peripheral small-airway obstruction.
- **Respiratory Reactance ($X_5$) & Resonant Frequency**: Tracks lung elastance and inertance balance.
- **Respiratory Environmental Health**: Actionable HEPA filtration alerts and bronchodilatory diaphragmatic guidance.

## Fast Invocation
```python
from client import PulmonaryOscillometryClient

client = PulmonaryOscillometryClient()
res = client.evaluate_respiratory_impedance(
    resistance_5hz_cmh2o_l_s=3.15,
    resistance_20hz_cmh2o_l_s=2.70
)
print("R5-R20 Peripheral:", res["peripheral_frequency_dependence_r5_r20"])
print("Impedance Score:", res["respiratory_impedance_score"])
```
