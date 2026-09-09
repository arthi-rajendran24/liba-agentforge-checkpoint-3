from pathlib import Path


def test_later_layers_do_not_duplicate_business_calculations():
    root = Path(__file__).parents[1]
    later_files = [
        root / "src/agentforge/service.py",
        root / "src/agentforge/evidence.py",
        root / "src/agentforge/memory.py",
        root / "src/agentforge/channel.py",
        root / "app.py",
        root / "telegram_bot.py",
    ]
    forbidden = ["break_even_units =", "conversion_rate =", "shortfall_units ="]
    for path in later_files:
        content = path.read_text(encoding="utf-8")
        assert not any(token in content for token in forbidden), path


def test_only_adapter_imports_student_tools_after_checkpoint_1():
    root = Path(__file__).parents[1] / "src/agentforge"
    importers = []
    for path in root.glob("*.py"):
        if path.name != "tools.py" and "from .tools import" in path.read_text(encoding="utf-8"):
            importers.append(path.name)
    assert importers == ["student_adapter.py"]
