"""
Forced Oscillation Technique (FOT / IOS) & Respiratory Impedance Engine.
Provides deterministic, zero-dependency modeling of total airway resistance (R5), central resistance (R20),
peripheral small-airway frequency dependence (R5-R20), reactance (X5), and resonant frequency (Fres).
"""

from typing import Dict, Any, List, Optional


class PulmonaryOscillometryClient:
    """
    Deterministic client for calculating Impulse Oscillometry (IOS) and Forced Oscillation Technique (FOT).
    Assesses effort-independent total respiratory system resistance, small peripheral airway narrowing,
    and elastic lung recoil during tidal breathing.
    """

    def __init__(self):
        pass

    def evaluate_respiratory_impedance(
        self,
        resistance_5hz_cmh2o_l_s: float,
        resistance_20hz_cmh2o_l_s: float,
        reactance_5hz_cmh2o_l_s: float = -0.9,
        resonant_frequency_hz: float = 10.5
    ) -> Dict[str, Any]:
        """
        Calculates R5-R20 peripheral resistance and respiratory health score.
        Normative adult references:
        - R5 (total resistance): 2.0 - 4.5 cmH2O*s/L
        - R20 (central resistance): 1.8 - 3.8 cmH2O*s/L
        - R5-R20 (peripheral frequency dependence): < 0.8 cmH2O*s/L
        - X5 (capacitive reactance): > -1.5 cmH2O*s/L
        - Fres (resonant frequency): 7.0 - 14.0 Hz
        """
        if resistance_5hz_cmh2o_l_s <= 0 or resistance_20hz_cmh2o_l_s <= 0:
            return {"error": "Resistances R5 and R20 must be positive"}

        r5_minus_r20 = round(resistance_5hz_cmh2o_l_s - resistance_20hz_cmh2o_l_s, 2)

        # Respiratory Impedance Score (0 - 100):
        # R5 <= 3.6, R5-R20 <= 0.6, Fres <= 12 Hz -> 90 - 100.
        score = 80.0
        if resistance_5hz_cmh2o_l_s <= 3.5:
            score += 10.0
        elif resistance_5hz_cmh2o_l_s > 5.5:
            score -= 25.0

        if r5_minus_r20 <= 0.5:
            score += 10.0
        elif r5_minus_r20 > 1.2:
            score -= 25.0
        elif r5_minus_r20 > 0.8:
            score -= 10.0

        if resonant_frequency_hz <= 12.0:
            score += 5.0
        elif resonant_frequency_hz > 18.0:
            score -= 15.0

        if reactance_5hz_cmh2o_l_s < -2.0:
            score -= 15.0

        impedance_score = round(min(100.0, max(5.0, score)), 1)

        has_peripheral_narrowing = r5_minus_r20 >= 0.85
        has_high_resistance = resistance_5hz_cmh2o_l_s >= 4.8

        if impedance_score >= 85.0:
            tier = "OPTIMAL_RESPIRATORY_IMPEDANCE"
            interp = f"Low airway resistance (R5 {resistance_5hz_cmh2o_l_s}, R5-R20 {r5_minus_r20} cmH2O*s/L); open, unobstructed tracheobronchial tree."
            guidance = "Optimal pulmonary conductance and elastic lung compliance. High ventilatory throughput during deep exertion."
        elif impedance_score >= 70.0:
            tier = "PRESERVED_VENTILATORY_CONDUCTANCE"
            interp = f"Normal respiratory mechanics (R5 {resistance_5hz_cmh2o_l_s}, Fres {resonant_frequency_hz} Hz); acceptable age-adjusted impedance."
            guidance = "Normal airway caliber. Maintain clean indoor air and routine cardiovascular conditioning."
        elif has_peripheral_narrowing and not has_high_resistance:
            tier = "PERIPHERAL_SMALL_AIRWAY_RESISTANCE"
            interp = f"Elevated frequency dependence (R5-R20 {r5_minus_r20} >= 0.85 cmH2O*s/L); reflects early peripheral bronchiolar constriction or particulate irritation."
            guidance = "Small-airway narrowing detected. Check indoor PM2.5 levels, verify air purifier filters, and engage in gentle diaphragmatic hum breathing."
        else:
            tier = "OBSTRUCTIVE_AIRWAY_IMPEDANCE"
            interp = f"High total resistance (R5 {resistance_5hz_cmh2o_l_s}) with negative reactance (X5 {reactance_5hz_cmh2o_l_s}); significant ventilatory mechanical impedance."
            guidance = "Obstructive ventilatory load detected. Avoid cold/dusty air exposure and consult pulmonology for comprehensive spirometric evaluation."

        return {
            "resistance_5hz_cmh2o_l_s": resistance_5hz_cmh2o_l_s,
            "resistance_20hz_cmh2o_l_s": resistance_20hz_cmh2o_l_s,
            "peripheral_frequency_dependence_r5_r20": r5_minus_r20,
            "reactance_5hz_cmh2o_l_s": reactance_5hz_cmh2o_l_s,
            "resonant_frequency_hz": resonant_frequency_hz,
            "respiratory_impedance_score": impedance_score,
            "classification": tier,
            "physiological_interpretation": interp,
            "actionable_guidance": guidance
        }
