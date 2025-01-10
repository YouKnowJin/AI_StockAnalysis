# 文件名: main.py

from crewai import Crew
from stock_analysis_agents import StockAnalysisAgents
from stock_analysis_tasks import StockAnalysisTasks
from dotenv import load_dotenv
import os

# 加载环境变量
load_dotenv()

class FinancialCrew:
    def __init__(self, stock_name):
        self.stock_name = stock_name

    def run(self):
        agents = StockAnalysisAgents()
        tasks = StockAnalysisTasks()

        # 创建代理
        research_analyst_agent = agents.股票研究分析师(self.stock_name)
        financial_analyst_agent = agents.财务数据分析师(self.stock_name)
        investment_advisor_agent = agents.投资顾问(self.stock_name)

        # 创建任务
        research_task = tasks.股票研究分析(research_analyst_agent, self.stock_name)
        financial_task = tasks.财务分析任务(financial_analyst_agent, self.stock_name)
        recommend_task = tasks.投资建议任务(investment_advisor_agent, self.stock_name)

        # 创建并启动Crew
        crew = Crew(
            agents=[
                research_analyst_agent,
                financial_analyst_agent,
                investment_advisor_agent
            ],
            tasks=[
                research_task,
                financial_task,
                recommend_task
            ],
            verbose=True
        )

        result = crew.kickoff()
        return result

if __name__ == "__main__":
    print("## 欢迎使用股票分析团队")
    print('-------------------------------')
    stock_name = input("请输入您想分析的股票名称（股票代码）：").strip().upper()

    if not stock_name:
        print("股票名称不能为空！")
        exit(1)

    financial_crew = FinancialCrew(stock_name)
    result = financial_crew.run()
    print("\n\n########################")
    print("## 分析报告")
    print("########################\n")
    print(result)
