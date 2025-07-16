# 使用 FastMCP 框架
from fastmcp import FastMCP
from datetime import datetime
import zoneinfo  # 支持时区

mcp = FastMCP("TimeService")

@mcp.tool(name="get_time", description="返回 ISO 8601 格式时间")
def get_current_time(timezone: str = "UTC") -> str:
    return datetime.now(zoneinfo.ZoneInfo(timezone)).isoformat()

if __name__ == "__main__":
    mcp.run(host="0.0.0.0", port=8000)  # 云部署需 0.0.0.0
