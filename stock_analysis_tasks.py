from crewai import Task
from textwrap import dedent

class StockAnalysisTasks:
    def __init__(self):
        pass

    def 股票研究分析(self, agent, stock_name):
        """
        股票研究分析任务，生成研究报告。
        """
        return Task(
            description=dedent(
                f"""
        收集和总结最近的新闻文章，出版
        发布，以及与股票相关的市场分析
        其行业。
        特别关注任何重大事件、市场
        情绪和分析师的意见。还包括即将推出的
        收入等事件。
          
        您的最终答案必须是一份包含
        最新消息的综合摘要，任何值得注意的
        市场情绪的转变，以及对
        股票。
        还要确保归还股票行情。
        
          
        请确保尽可能使用最新的数据。
          
        客户选择的公司：{stock_name}
                """
            ),
            expected_output=dedent(
                f"""
                一份详细的{stock_name}股票研究分析报告，内容包括：
                # 股票研究报告：{stock_name}
                ## 基本信息
                ## 新闻分析
                ## 趋势分析
                ## 市场情绪
                ## 其他分析师观点（如有）
                ## 结论
                报告格式为MarkDown。
                """
            ),
            verbose=True,
            agent=agent,
        )

    def 财务分析任务(self, agent, stock_name):
        """
        财务分析任务，生成财务报告。
        """
        return Task(
            description=dedent(
                f"""
        对股票的财务状况进行彻底分析
        健康和市场表现。
        这包括检查关键的财务指标，如
        市盈率、每股收益增长、收入趋势，以及
        债务股本比率。
        此外，比较分析股票的表现
        其行业同行和整体市场趋势。

        您的最终报告必须在提供的摘要基础上进行扩展
        但现在包括对股票的明确评估
        财务状况及其优势和劣势，
        以及在当前与竞争对手的竞争中
        市场情景.

        请确保尽可能使用最新的数据。

                """
            ),
            expected_output=dedent(
                f"""
                一份详细的{stock_name}公司财务分析报告，内容包括：
                # 财务分析报告：{stock_name}
                ## 收入分析
                ## 利润分析
                ## 现金流分析
                ## 负债分析
                ## 关键财务比率
                ## 结论与建议
                报告格式为MarkDown。
                """
            ),
            verbose=True,
            agent=agent,
        )

    def 投资建议任务(self, agent, stock_name):
        """
        投资建议任务，生成投资建议报告。
        """
        return Task(
            description=dedent(
                f"""
        审查并综合由提供的分析
      财务分析师和新闻分析师。
      将这些见解结合起来，形成一个全面的
      投资建议。
              
      你必须考虑所有方面，包括财务
      健康、市场情绪和定性数据
      EDGAR文件。

      确保包括一个显示内部人士的部分
      交易活动以及收益等即将发生的事件。

      您的最终答案必须是针对您的
      顾客它应该是一份完整的超级详细的报告，提供
      明确的投资立场和战略以及支持性证据。
      为您的客户制作美观且格式良好的表格。
                """
            ),
            expected_output=dedent(
                f"""
                一份详细的{stock_name}股票投资建议报告，内容包括：
                # 投资建议报告：{stock_name}
                ## 投资概况
                ## 全部优势与全部劣势
                ## 市场前景
                ## 风险评估
                ## 投资推荐
                ## 结论，持有评级，时间
                报告格式为MarkDown。
                """
            ),
            verbose=True,
            agent=agent,
        )

