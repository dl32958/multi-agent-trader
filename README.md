# 🤖 Multi-Agent Trader

A multi-agent trading system that uses AI agents to simulate autonomous stock trading with real market data. Each agent has its own investment strategy, portfolio management, and decision-making capabilities powered by large language models.

## 🌟 Features

- **Multi-Agent Architecture**: Multiple AI trading agents with distinct personalities and strategies
- **Real Market Data**: Integration with Polygon.io API for live and historical stock data
- **Portfolio Management**: Comprehensive account management with transaction tracking
- **Research Capabilities**: AI-powered research using web search and knowledge graphs
- **Email Notifications**: Automated trading alerts via SendGrid
- **MCP Integration**: Model Context Protocol for seamless AI tool interactions
- **Database Persistence**: SQLite database for accounts, transactions, and market data
- **Configurable Trading**: Customizable trading schedules and parameters

## 🏗️ System Architecture

![System Architecture](./docs/architecture1.svg)

## 🚀 Quick Start

### Prerequisites
- Python 3.12+
- [uv](https://github.com/astral-sh/uv) package manager

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/multi-agent-trader.git
   cd multi-agent-trader
   ```

2. **Install dependencies**
   ```bash
   uv sync
   ```

3. **Set up environment variables**
   ```bash
   cp .env
   # Edit .env with your API keys (see Configuration section)
   ```

4. **Run the trading floor**
   ```bash
   uv run python trading_floor.py
   ```

## 🛠️ Technology Stack

- **Agent Framework**: [OpenAI Agent SDK](https://github.com/openai/openai-python) for AI agent orchestration
- **MCP Servers**: Built with [FastMCP](https://github.com/jlowin/fastmcp) for high-performance tool serving
- **MCP Client**: Uses [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk) for agent communication
- **AI Models**: Support for OpenAI, OpenRouter, DeepSeek, Google Gemini, and Grok
- **Database**: SQLite for data persistence
- **Market Data**: Polygon.io API integration

## ⚙️ Configuration

Create a `.env` file with the following variables:

### Required Variables
```bash
# AI Model API (choose at least one)
OPENAI_API_KEY=your_openai_api_key_here
OPENROUTER_API_KEY=your_openrouter_api_key_here
DEEPSEEK_API_KEY=your_deepseek_api_key_here
GOOGLE_API_KEY=your_google_api_key_here
GROK_API_KEY=your_grok_api_key_here

# Market Data
POLYGON_API_KEY=your_polygon_api_key_here
POLYGON_PLAN=free  # or 'paid', 'realtime'

# Trading Configuration
RUN_EVERY_N_MINUTES=60
RUN_EVEN_WHEN_MARKET_IS_CLOSED=false
RESET_TRADERS=true
USE_MANY_MODELS=false
```

### Optional Variables
```bash
# Email Notifications
SENDGRID_API_KEY=your_sendgrid_api_key_here
FROM_EMAIL=your_email@example.com
TO_EMAIL=recipient@example.com

# Research Capabilities
BRAVE_API_KEY=your_brave_search_api_key_here
```

---

**Happy Trading! 📈🤖**