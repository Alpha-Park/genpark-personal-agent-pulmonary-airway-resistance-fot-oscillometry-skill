"""
Example Usage: Forced Oscillation Technique (FOT / IOS) & Respiratory Impedance.
Demonstrates calculation of total and peripheral small-airway resistance and reactance.
"""

from client import PulmonaryOscillometryClient


def main():
    client = PulmonaryOscillometryClient()
    print("=== Forced Oscillation Technique (FOT / IOS) Demo ===")

    # Test Case 1: Healthy unobstructed tracheobronchial tree
    res1 = client.evaluate_respiratory_impedance(
        resistance_5hz_cmh2o_l_s=3.15,
        resistance_20hz_cmh2o_l_s=2.70,
        reactance_5hz_cmh2o_l_s=-0.85,
        resonant_frequency_hz=10.2
    )
    print("\nTest Case 1: Healthy Pulmonary Impedance")
    print(f"  R5 (Total): {res1['resistance_5hz_cmh2o_l_s']} cmH2O*s/L | R20 (Central): {res1['resistance_20hz_cmh2o_l_s']} cmH2O*s/L")
    print(f"  R5-R20 (Peripheral): {res1['peripheral_frequency_dependence_r5_r20']} cmH2O*s/L")
    print(f"  X5 (Reactance): {res1['reactance_5hz_cmh2o_l_s']} | Fres: {res1['resonant_frequency_hz']} Hz")
    print(f"  Impedance Score: {res1['respiratory_impedance_score']} / 100")
    print(f"  Classification: {res1['classification']}")
    print(f"  Guidance: {res1['actionable_guidance']}")

    # Test Case 2: Peripheral small-airway resistance / smoke or dust exposure
    res2 = client.evaluate_respiratory_impedance(
        resistance_5hz_cmh2o_l_s=4.20,
        resistance_20hz_cmh2o_l_s=2.80,
        reactance_5hz_cmh2o_l_s=-1.80,
        resonant_frequency_hz=16.5
    )
    print("\nTest Case 2: Peripheral Small-Airway Constriction")
    print(f"  R5-R20 (Peripheral): {res2['peripheral_frequency_dependence_r5_r20']} cmH2O*s/L")
    print(f"  Fres: {res2['resonant_frequency_hz']} Hz | X5: {res2['reactance_5hz_cmh2o_l_s']}")
    print(f"  Impedance Score: {res2['respiratory_impedance_score']} / 100")
    print(f"  Classification: {res2['classification']}")
    print(f"  Guidance: {res2['actionable_guidance']}")


if __name__ == "__main__":
    main()
