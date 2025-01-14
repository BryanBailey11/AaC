"""Provides the model's textual view."""
from tkinter import PanedWindow, Text, GROOVE


def get_model_text_view(parent_window: PanedWindow):
    """Provides a view containing the text representation of a model."""
    model_text_view = Text(parent_window, bd=2, relief=GROOVE)
    model_text_view.insert("1.0", _get_sample_model_text())
    return model_text_view


def _get_sample_model_text() -> str:
    """Temporary function, remove it once models are actually loaded."""
    return """---
imports:
  - Imported_Enum_Data.yaml
  - Imported_Data.yaml
model:
  name: Test Model A
  components:
    - Component 1
    - Component 2
  behavior:
    - name: Behavior 1
      type: pub-sub
      acceptance:
        - scenario: A simple flow through the system
          given:
            - The system is in a valid state
          when:
            - The user does something
          then:
            - The system responds
    - name: Behavior 2
      type: pub-sub
      acceptance:
        - scenario: Another simple flow through the system
          given:
            - The system is in a valid state
          when:
            - The user does something
          then:
            - The system responds
---
model:
  name: Test Model B
  components:
    - Component 2
  behavior:
    """
