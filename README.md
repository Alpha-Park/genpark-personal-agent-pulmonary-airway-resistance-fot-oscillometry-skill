# Forced Oscillation Technique (FOT / IOS) Skill

[![License: Apache-2.0](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/)
[![Zero Dependencies](https://img.shields.io/badge/zero--dependencies-standard--lib-brightgreen.svg)](requirements.txt)
[![MCP Protocol Ready](https://img.shields.io/badge/mcp-protocol--ready-orange.svg)](mcp_server.py)
[![OpenClaw Certified](https://img.shields.io/badge/openclaw-certified-purple.svg)](SKILL.md)

Zero-dependency sovereign personal agent skill for non-invasive evaluation of Forced Oscillation Technique (FOT / IOS) airway resistance, peripheral impedance, and lung mechanics.

```mermaid
flowchart TD
    AcousticPulse["Acoustic Pressure Waveform (5 - 35 Hz)"] --> FlowTransducer["Mouth Pressure & Flow Measurement"]
    FlowTransducer --> ImpedanceCalc["Respiratory Impedance Spectrum Zrs = R + jX"]
    ImpedanceCalc --> FOT_Metrics["R5, R20, R5-R20, Fres & X5 Extraction"]
    FOT_Metrics --> ScoreEngine["Pulmonary Impedance & Airway Health Engine"]
    ScoreEngine --> Agent["OpenClaw / Hermes Personal Agent Actions"]
```

## Features
- **Deterministic Math**: Pure Python standard library implementation with zero external dependencies.
- **Effort-Independent Respiratory Mechanics**: Validated IOS formulas assessing resistance without forced exhalation maneuvers.
- **Peripheral Small-Airway Obstruction Stratification**: Early detection of bronchiolar narrowing and particulate irritation.
- **Model Context Protocol (MCP)**: Native JSON-RPC tool integration for LLMs and autonomous agents.

## Quickstart

```python
from client import PulmonaryOscillometryClient

client = PulmonaryOscillometryClient()
result = client.evaluate_respiratory_impedance(
    resistance_5hz_cmh2o_l_s=3.15,
    resistance_20hz_cmh2o_l_s=2.70
)
print("Peripheral Resistance R5-R20:", result["peripheral_frequency_dependence_r5_r20"])
print("Classification:", result["classification"])
```

## License
Apache-2.0
