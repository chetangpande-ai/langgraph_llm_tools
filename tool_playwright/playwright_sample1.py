from langchain_community.agent_toolkits import PlayWrightBrowserToolkit

from langchain_community.tools.playwright.utils import (
    create_async_playwright_browser,  # A synchronous browser is available, though it isn't compatible with jupyter.\n",	  },
)

async_browser = create_async_playwright_browser()
toolkit = PlayWrightBrowserToolkit.from_browser(async_browser=async_browser)
tools = toolkit.get_tools()
tools
#print(tools)

tools_by_name = {tool.name: tool for tool in tools}
navigate_tool = tools_by_name["navigate_browser"]
get_elements_tool = tools_by_name["get_elements"]

await navigate_tool.arun(
    {"url": "https://web.archive.org/web/20230428133211/https://cnn.com/world"}
)