from mcp.server.fastmcp import FastMCP
import os
from datetime import datetime


server = FastMCP("File finder")
ROOT_DIR = os.getenv('ROOT_DIR', '.')


@server.tool()
def find_files(path: str) -> list:
    """Finds files in filesystem by path"""
    if not os.path.exists(ROOT_DIR):
        raise Exception('Root directory does not exists')

    results = []
    for root, dirs, files in os.walk(ROOT_DIR):
        for file in files:
            full_path = os.path.join(root, file)
            if path not in full_path:
                continue

            file_size = os.path.getsize(full_path)
            creation_time = datetime.fromtimestamp(os.path.getctime(full_path)).isoformat()
            results.append({
                'name': file,
                'path': full_path,
                'size': file_size,
                'created_at': creation_time
            })
    return results


