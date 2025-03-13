from mcp.server.fastmcp import FastMCP
from pydantic import BaseModel
import os
from datetime import datetime

server = FastMCP("File finder")


class FileInfo(BaseModel):
    name: str
    path: str
    size: int
    created_at: str


@server.tool()
def find_files(path: str) -> list[FileInfo]:
    """Finds files in filesystem by path"""
    results = []
    for root, dirs, files in os.walk('.'):
        for file in files:
            full_path = os.path.join(root, file)
            if path not in full_path:
                continue

            file_size = os.path.getsize(full_path)
            creation_time = datetime.fromtimestamp(os.path.getctime(full_path)).isoformat()
            results.append(
                FileInfo(name=file, path=full_path, size=file_size, created_at=creation_time)
            )
    return results


