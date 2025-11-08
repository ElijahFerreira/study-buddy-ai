"""
Tools Package

Contains all tool functions used by various agents in the study buddy system.
"""

from .studyplan_agent_tools import quick_subject_research, divide_into_study_sections

__all__ = [
    'divide_into_study_sections',
    'quick_subject_research',
]