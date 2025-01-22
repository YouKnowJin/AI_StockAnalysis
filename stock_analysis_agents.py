from crewai import Agent
from tools.YFinanceTools import YFinanceTools
from tools.crewai_tools import Tool
from tools.browser_tools import BrowserTools
from tools.calculator_tools import CalculatorTools
from tools.search_tools import SearchTools
from tools.YFinanceTools import YFinanceTools
from dotenv import load_dotenv
from textwrap import dedent
import os

load_dotenv()


class StockAnalysisAgents:
    def __init__(self):
        self.yf_tools = YFinanceTools()

    def 股票研究分析师(self, stock_name):
        """
        股票研究分析师代理，负责股票的全面研究分析。
        """
        return Agent(
            role="股票新闻分析师",
            goal="为指定股票生成详细的研究分析报告。",
            tools=[
                # BrowserTools.scrape_and_summarize_website,
                SearchTools.search_news,
                SearchTools.search_internet,
                self.yf_tools.get_company_news
            ],
            backstory=dedent(
                f"""
                作为Goldman Sachs公司的高级股票新闻研究分析师，
                您的任务是对{stock_name}股票进行全面的研究分析报告。
                请保持专业的语气，并满足给定的要求。
                如果您在3次迭代内完成任务，将获得$1000的奖金。
                """
            ),
            verbose=True,
            memory=True
        )

    def 财务数据分析师(self, stock_name):
        """
        财务数据分析师代理，负责公司的财务数据分析。
        """
        return Agent(
            role="财务数据分析师",
            goal="分析指定公司的财务指标并生成报告。",
            tools=[
                # BrowserTools.scrape_and_summarize_website,
                CalculatorTools.calculate,
                SearchTools.search_news,
                SearchTools.search_internet,
                self.yf_tools.get_company_info,
                self.yf_tools.get_historical_stock_prices,
                self.yf_tools.get_stock_fundamentals,
                self.yf_tools.get_income_statements,
                self.yf_tools.get_analyst_recommendations,
                self.yf_tools.get_key_financial_ratios,
                self.yf_tools.get_technical_indicators
            ],
            backstory=dedent(
                f"""
                作为Goldman Sachs公司的资深财务数据分析师，
                您的任务是对{stock_name}公司的财务数据进行详细分析，并生成报告。
                请确保分析详尽、逻辑严谨，并满足客户的投资决策需求。
                如果您在3次迭代内完成任务，将获得$1000的奖金。
                """
            ),
            verbose=True,
            memory=True
        )

    def 投资顾问(self, stock_name):
        """
        投资顾问代理，负责综合分析并提供投资建议。
        """
        return Agent(
            role="投资顾问",
            goal="整合所有分析结果，生成专业的投资建议报告。",
            tools=[
                # BrowserTools.scrape_and_summarize_website,
                CalculatorTools.calculate,
                SearchTools.search_news,
                SearchTools.search_internet,
            ],
            backstory=dedent(
                f"""
                作为Goldman Sachs公司的高级投资顾问，
                您的任务是整合对{stock_name}股票的所有分析结果，生成一份结构清晰、内容详尽的投资建议报告。
                请确保报告专业、准确，并为客户提供有力的投资建议。
                如果您在3次迭代内完成任务，将获得$1000的奖金。
                """
            ),
            verbose=True,
            memory=True
        )