import platform


def greet(name: str) -> str:
    if not name:
        raise ValueError("name must not be empty")
    return f"Hello, {name}! Running on {platform.system()}."


def build_id(job: str, run_number: str) -> str:
    return f"{job}-{run_number}"
