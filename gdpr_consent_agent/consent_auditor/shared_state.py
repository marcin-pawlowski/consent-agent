"""In-memory audit state shared across all sub-agents in a session."""

_audit_state: dict = {}


def set(key: str, value) -> None:
    _audit_state[key] = value


def get(key: str, default=None):
    return _audit_state.get(key, default)


def get_all() -> dict:
    return dict(_audit_state)


def reset() -> None:
    _audit_state.clear()
