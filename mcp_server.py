"""
MCP Server for Forced Oscillation Technique (FOT / IOS) Skill.
Exposes JSON-RPC Model Context Protocol tools for evaluating respiratory resistance, small-airway impedance, and reactance.
"""

import sys
import json
from typing import Dict, Any
from client import PulmonaryOscillometryClient


def get_tools_manifest() -> Dict[str, Any]:
    return {
        "tools": [
            {
                "name": "evaluate_respiratory_impedance",
                "description": "Calculates total airway resistance (R5), central resistance (R20), peripheral resistance (R5-R20), and respiratory impedance score.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "resistance_5hz_cmh2o_l_s": {
                            "type": "number",
                            "description": "Total respiratory system resistance at 5 Hz in cmH2O*s/L (e.g. 3.2 cmH2O*s/L)."
                        },
                        "resistance_20hz_cmh2o_l_s": {
                            "type": "number",
                            "description": "Central airway resistance at 20 Hz in cmH2O*s/L (e.g. 2.7 cmH2O*s/L)."
                        },
                        "reactance_5hz_cmh2o_l_s": {
                            "type": "number",
                            "description": "Respiratory reactance at 5 Hz in cmH2O*s/L (typically -0.5 to -1.5).",
                            "default": -0.9
                        },
                        "resonant_frequency_hz": {
                            "type": "number",
                            "description": "Resonant frequency where reactance is zero in Hz (typically 8.0 - 14.0 Hz).",
                            "default": 10.5
                        }
                    },
                    "required": ["resistance_5hz_cmh2o_l_s", "resistance_20hz_cmh2o_l_s"]
                }
            }
        ]
    }


def handle_request(client: PulmonaryOscillometryClient, req: Dict[str, Any]) -> Dict[str, Any]:
    method = req.get("method")
    params = req.get("params", {})
    req_id = req.get("id")

    if method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": get_tools_manifest()
        }
    elif method == "tools/call":
        name = params.get("name")
        args = params.get("arguments", {})

        if name == "evaluate_respiratory_impedance":
            res = client.evaluate_respiratory_impedance(
                resistance_5hz_cmh2o_l_s=float(args.get("resistance_5hz_cmh2o_l_s", 3.2)),
                resistance_20hz_cmh2o_l_s=float(args.get("resistance_20hz_cmh2o_l_s", 2.7)),
                reactance_5hz_cmh2o_l_s=float(args.get("reactance_5hz_cmh2o_l_s", -0.9)),
                resonant_frequency_hz=float(args.get("resonant_frequency_hz", 10.5))
            )
            return {
                "jsonrpc": "2.0",
                "id": req_id,
                "result": {
                    "content": [
                        {
                            "type": "text",
                            "text": json.dumps(res, indent=2)
                        }
                    ]
                }
            }
        else:
            return {
                "jsonrpc": "2.0",
                "id": req_id,
                "error": {
                    "code": -32601,
                    "message": f"Method {name} not found"
                }
            }
    else:
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "error": {
                "code": -32600,
                "message": "Invalid request"
            }
        }


def main():
    client = PulmonaryOscillometryClient()
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            req = json.loads(line)
            resp = handle_request(client, req)
            sys.stdout.write(json.dumps(resp) + "\n")
            sys.stdout.flush()
        except Exception as e:
            err_resp = {
                "jsonrpc": "2.0",
                "id": None,
                "error": {"code": -32700, "message": str(e)}
            }
            sys.stdout.write(json.dumps(err_resp) + "\n")
            sys.stdout.flush()


if __name__ == "__main__":
    main()
