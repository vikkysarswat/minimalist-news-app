#!/usr/bin/env python3
"""Minimalist News App - FastMCP Server

A lightweight MCP server that returns news content in carousel/widget format.
Follows OpenAI pizzaz_server_python style for Python MCP server formatting.
"""

import asyncio
import logging
from datetime import datetime
from pathlib import Path
from typing import Optional

from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent, ImageContent, EmbeddedResource

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize server
app = Server("minimalist-news-app")

# Load HTML templates
ASSETS_DIR = Path(__file__).parent / "assets" / "components"

def load_template(filename: str) -> str:
    """Load HTML template from assets/components directory."""
    try:
        template_path = ASSETS_DIR / filename
        return template_path.read_text()
    except Exception as e:
        logger.error(f"Failed to load template {filename}: {e}")
        return ""

def format_news_card(article: dict) -> str:
    """Format a single news article as a card."""
    template = load_template("news_card.html")
    return template.replace("{{title}}", article.get("title", ""))\
        .replace("{{source}}", article.get("source", ""))\
        .replace("{{time}}", article.get("time", ""))\
        .replace("{{description}}", article.get("description", ""))\
        .replace("{{url}}", article.get("url", "#"))

def format_news_carousel(articles: list, section_title: str = "Latest News") -> str:
    """Format multiple news articles as a carousel."""
    template = load_template("news_carousel.html")
    
    # Generate article items
    items = ""
    for article in articles:
        items += f'''
      <div class="carousel-item">
        <article>
          <img src="{article.get("image", "")}" alt="{article.get("title", "")}" onerror="this.style.display='none'">
          <h3>{article.get("title", "")}</h3>
          <p class="source">{article.get("source", "")} • {article.get("time", "")}</p>
          <p class="description">{article.get("description", "")}</p>
          <a href="{article.get("url", "#")}" target="_blank">Read more →</a>
        </article>
      </div>
'''
    
    # Replace template placeholders
    result = template.replace("{{section_title}}", section_title)
    # Replace Mustache-style loop with generated items
    result = result.split("{{#articles}}")[0] + items + \
             result.split("{{/articles}}")[1] if "{{#articles}}" in result else template
    
    return result

@app.list_tools()
async def list_tools() -> list[Tool]:
    """List available tools."""
    return [
        Tool(
            name="get_news",
            description="Get news articles in carousel/card format",
            inputSchema={
                "type": "object",
                "properties": {
                    "topic": {
                        "type": "string",
                        "description": "News topic or query"
                    },
                    "format": {
                        "type": "string",
                        "enum": ["carousel", "card"],
                        "description": "Display format (carousel or single card)",
                        "default": "carousel"
                    },
                    "limit": {
                        "type": "number",
                        "description": "Number of articles to return",
                        "default": 5
                    }
                },
                "required": ["topic"]
            }
        )
    ]

@app.call_tool()
async def call_tool(name: str, arguments: dict) -> list[TextContent]:
    """Handle tool calls."""
    if name == "get_news":
        topic = arguments.get("topic", "")
        format_type = arguments.get("format", "carousel")
        limit = arguments.get("limit", 5)
        
        # Mock news data (in production, integrate with news API)
        mock_articles = [
            {
                "title": f"Breaking: {topic} - Latest Developments",
                "source": "News Source",
                "time": datetime.now().strftime("%H:%M"),
                "description": f"Latest updates on {topic} with comprehensive coverage and analysis.",
                "url": "https://example.com/news/1",
                "image": "https://via.placeholder.com/300x160"
            },
            {
                "title": f"{topic}: Expert Analysis and Insights",
                "source": "Tech Daily",
                "time": "1h ago",
                "description": f"In-depth analysis of {topic} and its implications for the industry.",
                "url": "https://example.com/news/2",
                "image": "https://via.placeholder.com/300x160"
            },
            {
                "title": f"Global Impact: {topic} Trends",
                "source": "World News",
                "time": "2h ago",
                "description": f"How {topic} is affecting markets and communities worldwide.",
                "url": "https://example.com/news/3",
                "image": "https://via.placeholder.com/300x160"
            }
        ][:limit]
        
        # Format response based on requested format
        if format_type == "carousel":
            html_content = format_news_carousel(mock_articles, f"{topic} News")
        else:
            html_content = format_news_card(mock_articles[0]) if mock_articles else "No news available"
        
        return [TextContent(type="text", text=html_content)]
    
    raise ValueError(f"Unknown tool: {name}")

async def main():
    """Run the MCP server."""
    logger.info("Starting Minimalist News App MCP Server")
    async with stdio_server() as (read_stream, write_stream):
        await app.run(read_stream, write_stream, app.create_initialization_options())

if __name__ == "__main__":
    asyncio.run(main())
