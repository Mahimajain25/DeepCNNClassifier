from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True) ## works like namedtuples
class DataIngestionConfig:
    # class variables
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path
