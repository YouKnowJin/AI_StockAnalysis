# 📈 CrewAI Stock Analysis Project Overview

Welcome to the **CrewAI Stock Analysis** project! 🚀 This project is designed to help you analyze stocks using a team of virtual agents. Each agent specializes in different aspects of stock analysis, such as financial data, market trends, and investment advice. With this tool, you can get a comprehensive report on any stock you're interested in. Whether you're a seasoned investor or just getting started, CrewAI is here to assist you! 💼📊

### 🛠️ Technical Explanation

The CrewAI Stock Analysis project is built using a modular architecture with several key components:

1. **Agents**: These are specialized entities that perform specific tasks. For example, the `股票研究分析师` (Stock Research Analyst) agent gathers and analyzes news and market data, while the `财务数据分析师` (Financial Data Analyst) focuses on financial metrics.

2. **Tasks**: Each agent is assigned tasks that align with their expertise. Tasks are defined in the `stock_analysis_tasks.py` file and include activities like generating research reports and financial analyses.

3. **Tools**: The project utilizes various tools to gather and process data. These tools are defined in the `tools` directory and include modules for web scraping, financial calculations, and data retrieval from Yahoo Finance.

4. **Crew**: The `Crew` class orchestrates the agents and tasks, ensuring that each agent contributes to the overall analysis process. The `FinancialCrew` class in `main.py` is responsible for setting up and running the crew.

5. **Environment Variables**: The project uses environment variables to manage API keys and other sensitive information, loaded via `dotenv`.

### 🚀 Getting Started

To start using the CrewAI Stock Analysis project, follow these steps:

1. **Clone the Repository**: First, clone the project repository to your local machine.

   ```bash
   git clone https://github.com/thewilddoor/Multi-Agent_AI-Stock-Analyze.git
   cd crewai_stock_analysis
   ```

2. **Install Dependencies**: Ensure you have Python installed, then install the required packages using pip.

   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Environment Variables**: Create a `.env` file in the root directory and add your API keys and other necessary environment variables. For example:

   ```
   BROWSERLESS_API_KEY=your_browserless_api_key
   SERPER_API_KEY=your_serper_api_key
   SEC_API_API_KEY=your_sec_api_key
   ```

4. **Run the Application**: Execute the `main.py` script to start the stock analysis process.

   ```bash
   python crewai_stock_analysis/main.py
   ```

5. **Input Stock Name**: When prompted, enter the stock name or ticker symbol you wish to analyze.

### 📦 Dependencies

The project relies on several Python libraries, including:

- `yfinance`: For retrieving financial data from Yahoo Finance.
- `requests`: For making HTTP requests to external APIs.
- `dotenv`: For loading environment variables.
- `langchain`: For handling language processing tasks.
- `unstructured`: For parsing HTML content.

Make sure all dependencies are installed by running the `pip install -r requirements.txt` command.

With these steps, you're all set to explore the world of stock analysis with CrewAI! Happy analyzing! 📊✨
