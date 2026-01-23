"""Utilities for minting compact kernel-state tokens."""

from dataclasses import dataclass

VALID_VERDICTS = {"SAFE", "BOUNDARY", "UNSAFE", "UNKNOWN"}


@dataclass(frozen=True)
class KernelState:
    vehicle_id: str
    scenario_id: str
    epoch: str
    chamber: str
    merkle_root: str
    verdict: str
    invset_id: str


def emit_kernel_state_token(
    vehicle_id: str,
    scenario_id: str,
    epoch: str,
    chamber: str,
    merkle_root: str,
    verdict: str,
    invset_id: str,
) -> str:
    """
    Emit a one-line kernel state token suitable for prompt injection or registry storage.
    """
    for field_name, value in {
        "vehicle_id": vehicle_id,
        "scenario_id": scenario_id,
        "epoch": epoch,
        "chamber": chamber,
        "merkle_root": merkle_root,
        "verdict": verdict,
        "invset_id": invset_id,
    }.items():
        if value is None or str(value).strip() == "":
            raise ValueError(f"{field_name} must be provided")
        if any(char in str(value) for char in "[];\n"):
            raise ValueError(f"{field_name} contains a reserved character")

    if verdict not in VALID_VERDICTS:
        raise ValueError(f"verdict must be one of {sorted(VALID_VERDICTS)}")

    return (
        "KERNEL_STATE["
        f"vehicle={vehicle_id};"
        f"scenario={scenario_id};"
        f"epoch={epoch};"
        f"chamber={chamber};"
        f"merkle_root={merkle_root};"
        f"verdict={verdict};"
        f"invariants={invset_id}"
        "]"
    )


def emit_kernel_state_token_from_state(state: KernelState) -> str:
    """Emit a kernel state token from a KernelState dataclass."""
    return emit_kernel_state_token(
        vehicle_id=state.vehicle_id,
        scenario_id=state.scenario_id,
        epoch=state.epoch,
        chamber=state.chamber,
        merkle_root=state.merkle_root,
        verdict=state.verdict,
        invset_id=state.invset_id,
    )
