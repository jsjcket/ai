"""
基金筛选配置模块
功能：根据风险偏好筛选基金，生成配置方案
"""

from datetime import datetime

class FundSelector:
    def __init__(self):
        self.name = "基金筛选模块"
        
    def get_fund_types(self):
        """
        返回基金类型及其特点
        """
        return {
            "货币基金": {"risk": "R1", "return": "1.5%-2%", "period": "随时"},
            "短债基金": {"risk": "R2", "return": "3%-5%", "period": "3-6个月"},
            "纯债基金": {"risk": "R2", "return": "4%-6%", "period": "1-3年"},
            "混合基金": {"risk": "R3-R4", "return": "-20%~+50%", "period": "长期"},
            "指数基金": {"risk": "R3-R4", "return": "跟随指数", "period": "长期定投"},
            "股票基金": {"risk": "R5", "return": "-50%~+100%", "period": "长期"}
        }
    
    def recommend_allocation(self, risk_level, total_amount):
        """
        根据风险偏好推荐配置方案
        
        Args:
            risk_level: 风险等级 (保守/稳健/平衡/进取)
            total_amount: 总金额
        """
        allocations = {
            "保守": {
                "货币基金": 0.60,
                "短债基金": 0.30,
                "纯债基金": 0.10
            },
            "稳健": {
                "货币基金": 0.40,
                "短债基金": 0.30,
                "纯债基金": 0.20,
                "指数基金": 0.10
            },
            "平衡": {
                "货币基金": 0.20,
                "纯债基金": 0.30,
                "混合基金": 0.30,
                "指数基金": 0.20
            },
            "进取": {
                "纯债基金": 0.10,
                "混合基金": 0.30,
                "指数基金": 0.40,
                "股票基金": 0.20
            }
        }
        
        if risk_level not in allocations:
            risk_level = "稳健"
        
        allocation = allocations[risk_level]
        report = f"""
# 基金配置方案
生成时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## 基本信息
- 风险偏好：{risk_level}
- 总金额：{total_amount}元

## 推荐配置

| 基金类型 | 配置比例 | 配置金额 |
|---------|---------|---------|
"""
        for fund_type, ratio in allocation.items():
            amount = total_amount * ratio
            report += f"| {fund_type} | {ratio*100:.0f}% | {amount:.0f}元 |\n"
        
        report += f"""
## 风险提示
⚠️ 投资有风险，入市需谨慎。
⚠️ 以上配置仅供参考，不构成投资建议。
⚠️ 请根据自身实际情况调整配置。
"""
        return report
    
    def screen_funds(self, fund_type, min_size=5, min_years=3):
        """
        基金筛选条件
        
        Args:
            fund_type: 基金类型
            min_size: 最小规模（亿）
            min_years: 最小成立年限
        """
        criteria = f"""
# 基金筛选条件

## 筛选标准
- 基金类型：{fund_type}
- 基金规模：>{min_size}亿
- 成立时间：>{min_years}年
- 基金经理任职：>3年
- 最大回撤：<10%

## 支付宝筛选步骤
1. 打开支付宝 → 理财 → 基金
2. 点击"基金排行" → "筛选"
3. 设置以上条件
4. 对比筛选结果

## 注意事项
- 不要只看收益排名
- 关注最大回撤
- 查看基金经理任职年限
- 注意费率结构
"""
        return criteria

if __name__ == "__main__":
    selector = FundSelector()
    print(selector.recommend_allocation("稳健", 10000))
