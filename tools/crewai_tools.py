# 文件名: crewai_stock_analysis/tools/crewai_tools.py

class Tool:
    """
    一个工具类，包含name、func和description属性。
    """
    def __init__(self, name: str, func, description: str):
        self.name = name
        self.func = func
        self.description = description

def tool(name: str, description: str):
    """
    工具装饰器，用于创建Tool实例。
    """
    def decorator(func):
        return Tool(name=name, func=func, description=description)
    return decorator
