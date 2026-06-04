from pathlib import Path


def test_module12_notebook_exists():
    notebook = Path(__file__).resolve().parent.parent / '12_Final_Projects_and_Next_Steps.ipynb'
    assert notebook.exists()
