# 文件名: crewai_stock_analysis/tools/YFinanceTools.py

import json
import yfinance as yf
from tools.crewai_tools import Tool, tool

def value_to_crores(value: int) -> float:
    """将数值转换为亿单位。

    Args:
        value (int): 需要转换的数值。

    Returns:
        float: 转换后的数值，保留两位小数。
    """
    return round(value / 10 ** 7, 2)

class YFinanceTools:
    """使用Yahoo Finance API获取财务数据的工具集。"""

    @staticmethod
    @tool(name="获取公司信息", description="获取指定股票代码的公司信息和概述。")
    def get_company_info(symbol: str) -> str:
        """获取指定股票代码的公司信息和概述。

        Args:
            symbol (str): 股票代码。

        Returns:
            str: 包含公司简介和概述的JSON字符串。
        """
        try:
            company_info_full = yf.Ticker(symbol).info
            if company_info_full is None:
                return f"无法获取{symbol}的公司信息"

            company_info_cleaned = {
                "名称": company_info_full.get("shortName"),
                "股票代码": company_info_full.get("symbol"),
                "当前股价": company_info_full.get('regularMarketPrice', company_info_full.get('currentPrice')),
                "市值（亿）": f"{value_to_crores(company_info_full.get('marketCap'))}亿",
                "行业": company_info_full.get("sector"),
                "子行业": company_info_full.get("industry"),
                "公司地址": company_info_full.get("address1"),
                "城市": company_info_full.get("city"),
                "州": company_info_full.get("state"),
                "邮编": company_info_full.get("zip"),
                "国家": company_info_full.get("country"),
                "每股收益（EPS）": company_info_full.get("trailingEps"),
                "市盈率（P/E Ratio）": company_info_full.get("trailingPE"),
                "52周最低价": company_info_full.get("fiftyTwoWeekLow"),
                "52周最高价": company_info_full.get("fiftyTwoWeekHigh"),
                "50日平均价": company_info_full.get("fiftyDayAverage"),
                "200日平均价": company_info_full.get("twoHundredDayAverage"),
                "公司网站": company_info_full.get("website"),
                "公司简介": company_info_full.get("longBusinessSummary"),
                "分析师推荐": company_info_full.get("recommendationKey"),
                "分析师意见数量": company_info_full.get("numberOfAnalystOpinions"),
                "员工总数": company_info_full.get("fullTimeEmployees"),
                "总现金": company_info_full.get("totalCash"),
                "自由现金流": company_info_full.get("freeCashflow"),
                "经营现金流": company_info_full.get("operatingCashflow"),
                "息税折旧及摊销前利润（EBITDA）": company_info_full.get("ebitda"),
                "收入增长率": company_info_full.get("revenueGrowth"),
                "毛利率": company_info_full.get("grossMargins"),
                "息税折旧及摊销利润率": company_info_full.get("ebitdaMargins"),
            }
            return json.dumps(company_info_cleaned, indent=2, ensure_ascii=False)
        except Exception as e:
            return f"获取{symbol}公司概况时出错: {e}"

    @staticmethod
    @tool(name="获取历史股价", description="获取指定股票代码的历史股价。")
    def get_historical_stock_prices(symbol: str, period: str = "1mo", interval: str = "5d") -> str:
        """获取指定股票代码的历史股价。

        Args:
            symbol (str): 股票代码。
            period (str): 获取历史价格的时间范围。默认为 "1mo"。
            interval (str): 数据点之间的时间间隔。默认为 "5d"。

        Returns:
            str: 历史股价的JSON字符串或错误信息。
        """
        try:
            stock = yf.Ticker(symbol)
            historical_price = stock.history(period=period, interval=interval)
            return historical_price.to_json(orient="index", ensure_ascii=False)
        except Exception as e:
            return f"获取{symbol}的历史股价时出错: {e}"

    @staticmethod
    @tool(name="获取基本面数据", description="获取指定股票代码的基本面数据。")
    def get_stock_fundamentals(symbol: str) -> str:
        """获取指定股票代码的基本面数据。

        Args:
            symbol (str): 股票代码。

        Returns:
            str: 基本面数据的JSON字符串或错误信息。
        """
        try:
            stock = yf.Ticker(symbol)
            info = stock.info
            fundamentals = {
                "股票代码": symbol,
                "公司名称": info.get("longName", ""),
                "行业": info.get("sector", ""),
                "子行业": info.get("industry", ""),
                "市值": info.get("marketCap", "N/A"),
                "市盈率": info.get("forwardPE", "N/A"),
                "市净率": info.get("priceToBook", "N/A"),
                "股息率": info.get("dividendYield", "N/A"),
                "每股收益（EPS）": info.get("trailingEps", "N/A"),
                "贝塔值": info.get("beta", "N/A"),
                "52周最高价": info.get("fiftyTwoWeekHigh", "N/A"),
                "52周最低价": info.get("fiftyTwoWeekLow", "N/A"),
            }
            return json.dumps(fundamentals, indent=2, ensure_ascii=False)
        except Exception as e:
            return f"获取{symbol}的基本面数据时出错: {e}"

    @staticmethod
    @tool(name="获取收益报表", description="获取指定股票代码的收益报表。")
    def get_income_statements(symbol: str) -> str:
        """获取指定股票代码的收益报表。

        Args:
            symbol (str): 股票代码。

        Returns:
            str: 收益报表的JSON字符串或错误信息。
        """
        try:
            stock = yf.Ticker(symbol)
            financials = stock.financials
            return financials.to_json(orient="index", ensure_ascii=False)
        except Exception as e:
            return f"获取{symbol}的收益报表时出错: {e}"

    @staticmethod
    @tool(name="获取关键财务比率", description="获取指定股票代码的关键财务比率。")
    def get_key_financial_ratios(symbol: str) -> str:
        """获取指定股票代码的关键财务比率。

        Args:
            symbol (str): 股票代码。

        Returns:
            str: 关键财务比率的JSON字符串或错误信息。
        """
        try:
            stock = yf.Ticker(symbol)
            key_ratios = stock.info
            return json.dumps(key_ratios, indent=2, ensure_ascii=False)
        except Exception as e:
            return f"获取{symbol}的关键财务比率时出错: {e}"

    @staticmethod
    @tool(name="获取分析师推荐", description="获取指定股票代码的分析师推荐。")
    def get_analyst_recommendations(symbol: str) -> str:
        """获取指定股票代码的分析师推荐。

        Args:
            symbol (str): 股票代码。

        Returns:
            str: 分析师推荐的JSON字符串或错误信息。
        """
        try:
            stock = yf.Ticker(symbol)
            recommendations = stock.recommendations
            return recommendations.to_json(orient="index", force_ascii=False)
        except Exception as e:
            return f"获取{symbol}的分析师推荐时出错: {e}"

    @staticmethod
    @tool(name="获取公司新闻", description="获取指定股票代码的公司新闻和新闻稿。")
    def get_company_news(symbol: str, num_stories: int = 3) -> str:
        """获取指定股票代码的公司新闻和新闻稿。

        Args:
            symbol (str): 股票代码。
            num_stories (int): 返回的新闻数量。默认为3。

        Returns:
            str: 公司新闻的JSON字符串或错误信息。
        """
        try:
            news = yf.Ticker(symbol).news
            return json.dumps(news[:num_stories], indent=2, ensure_ascii=False)
        except Exception as e:
            return f"获取{symbol}的公司新闻时出错: {e}"

    @staticmethod
    @tool(name="获取技术指标", description="获取指定股票代码的技术指标。")
    def get_technical_indicators(symbol: str, period: str = "5d") -> str:
        """获取指定股票代码的技术指标。

        Args:
            symbol (str): 股票代码。
            period (str): 获取技术指标的时间范围。默认为 "5d"。

        Returns:
            str: 技术指标的JSON字符串或错误信息。
        """
        try:
            indicators = yf.Ticker(symbol).history(period=period)
            return indicators.to_json(orient="index", ensure_ascii=False)
        except Exception as e:
            return f"获取{symbol}的技术指标时出错: {e}"

    def tools(self):
        """
        返回所有工具的列表。（此方法原样保留）
        """
        return [
            self.get_company_info,
            self.get_historical_stock_prices,
            self.get_stock_fundamentals,
            self.get_income_statements,
            self.get_key_financial_ratios,
            self.get_analyst_recommendations,
            self.get_company_news,
            self.get_technical_indicators,
        ]