"""
Configuration management for Project ORE with validation
"""
import os
from typing import Dict, Any, List, Optional
from dataclasses import dataclass
from enum import Enum
import logging
from pydantic_settings import BaseSettings
from pydantic import Field, validator

class EmotionalDimension(str, Enum):
    CURIOSITY = "curiosity"
    FRUSTRATION = "frustration"
    SATISFACTION = "satisfaction"
    ANTICIPATION = "anticipation"
    CONFUSION = "confusion"
    RESOLUTION = "resolution"
    STRESS = "stress"

@dataclass
class MonitoringThresholds:
    """Thresholds for system vitals monitoring"""
    CPU_CRITICAL: float = 90.0
    CPU_WARNING: float = 75.0
    MEMORY_CRITICAL: float = 90.0
    MEMORY_WARNING: float = 80.0
    DISK_CRITICAL: float = 95.0
    DISK_WARNING: float = 85.0

class OREConfig(BaseSettings):
    """Main configuration class with validation"""
    
    # Firebase Configuration
    FIREBASE_CREDENTIALS_PATH: str = Field(
        default="credentials/firebase-service-account.json",