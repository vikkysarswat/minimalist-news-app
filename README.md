# Minimalist News App

A lightweight, minimalist news application using FastMCP Server for delivering news content in carousel/widget format. This project demonstrates clean Python MCP server implementation following OpenAI's pizzaz_server_python style.

## Features

- 🎨 **Minimalist Design**: Clean, modern UI components
- 🎠 **Carousel View**: Swipeable news carousel for browsing multiple articles
- 🃏 **Card View**: Individual news cards for focused reading
- ⚡ **Fast MCP Server**: Asynchronous Python server for quick responses
- 🔧 **Easy Customization**: Modular HTML components ready for editing
- 📱 **Responsive**: Mobile-friendly design with smooth interactions

## Project Structure

```
minimalist-news-app/
├── assets/
│   └── components/
│       ├── news_card.html      # Single news article card component
│       └── news_carousel.html  # Multi-article carousel component
├── main.py                     # FastMCP server implementation
├── requirements.txt            # Python dependencies
├── .gitignore                  # Python gitignore template
└── README.md                   # This file
```

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/vikkysarswat/minimalist-news-app.git
   cd minimalist-news-app
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the server**
   ```bash
   python main.py
   ```

## Usage

The MCP server provides a `get_news` tool that accepts:

### Parameters

- **topic** (required): News topic or search query
- **format** (optional): Display format - `"carousel"` or `"card"` (default: `"carousel"`)
- **limit** (optional): Number of articles to return (default: 5)

### Example Requests

```python
# Get news in carousel format
{
  "topic": "artificial intelligence",
  "format": "carousel",
  "limit": 5
}

# Get single news card
{
  "topic": "climate change",
  "format": "card"
}
```

## Components

### News Card (`news_card.html`)
Displays a single news article with:
- Article title
- Source and timestamp
- Description/summary
- Read more link
- Hover effects for better UX

### News Carousel (`news_carousel.html`)
Interactive carousel featuring:
- Section header
- Navigation controls (← →)
- Horizontal scrollable articles
- Smooth scroll behavior
- Image support with fallback

## Customization

All HTML components are located in `assets/components/` and use inline CSS for easy customization:

1. **Styling**: Modify the `<style>` blocks in each component
2. **Layout**: Adjust HTML structure as needed
3. **Colors**: Update color values in CSS (currently uses Material Design palette)
4. **Responsive**: Modify breakpoints and sizing

## Development

### Adding News API Integration

Replace the mock data in `main.py` with a real news API:

```python
# Example: Using News API
import aiohttp

async def fetch_news(topic: str, limit: int):
    async with aiohttp.ClientSession() as session:
        async with session.get(f"https://newsapi.org/v2/everything?q={topic}") as resp:
            data = await resp.json()
            return data['articles'][:limit]
```

### Extending Functionality

- Add more HTML components in `assets/components/`
- Create new tools in `main.py` using `@app.list_tools()` and `@app.call_tool()`
- Implement caching for better performance
- Add error handling and logging

## Technical Stack

- **Python 3.8+**: Core language
- **FastMCP**: Model Context Protocol server framework
- **asyncio**: Asynchronous programming
- **HTML/CSS**: Frontend components
- **JavaScript**: Client-side interactions

## Dependencies

```txt
mcp>=1.0.0              # Core MCP Server
aiohttp>=3.9.0          # Async HTTP client
python-dotenv>=1.0.0    # Environment management
```

## Architecture

Follows the **pizzaz_server_python** style:

1. **Modular Components**: Separate HTML templates for reusability
2. **Async-First**: Asynchronous operations throughout
3. **Type Hints**: Full type annotations for clarity
4. **Logging**: Comprehensive logging for debugging
5. **Error Handling**: Graceful error management
6. **Documentation**: Inline docstrings and comments

## Contributing

Contributions are welcome! Please feel free to:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is open source and available for modification and distribution.

## Future Enhancements

- [ ] Real news API integration (NewsAPI, Guardian, etc.)
- [ ] Category filtering (Tech, Sports, Business, etc.)
- [ ] Search functionality
- [ ] Bookmark/save articles
- [ ] Dark mode support
- [ ] Performance optimization
- [ ] Caching layer
- [ ] Rate limiting
- [ ] User preferences
- [ ] Multi-language support

## Support

For issues, questions, or contributions, please open an issue on GitHub.

---

**Built with ❤️ using FastMCP Server**
