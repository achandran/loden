"""Run the complete Loden audit and generation pipeline."""

from audit_palette import main as audit
from generate_themes import main as generate


if __name__ == "__main__":
    audit("loden-night")
    audit("loden-day")
    generate()
