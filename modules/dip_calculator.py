"""
定投计算器模块
功能：计算定投收益、设置提醒
"""

from datetime import datetime, timedelta

class DIPCalculator:
    def __init__(self):
        self.name = "定投计算器"
        
    def calculate_return(self, monthly_amount, years, annual_return_rate):
        """
        计算定投收益
        
        Args:
            monthly_amount: 每月定投金额
            years: 定投年数
            annual_return_rate: 年化收益率（如0.08表示8%）
        """
        months = years * 12
        monthly_rate = annual_return_rate / 12
        
        total_invested = monthly_amount * months
        
        if monthly_rate == 0:
            final_value = total_invested
        else:
            final_value = monthly_amount * ((1 + monthly_rate) ** months - 1) / monthly_rate
        
        total_return = final_value - total_invested
        return_rate = (final_value / total_invested - 1) * 100
        
        report = f"""
# 定投收益计算
生成时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## 定投参数
- 每月定投：{monthly_amount}元
- 定投年数：{years}年
- 预期年化收益：{annual_return_rate*100:.1f}%

## 计算结果
- 总投入：{total_invested:.0f}元
- 预期终值：{final_value:.0f}元
- 预期收益：{total_return:.0f}元
- 收益率：{return_rate:.1f}%

## 不同收益率对比

| 年化收益 | 预期终值 | 预期收益 |
|---------|---------|---------|
"""
        for rate in [0.02, 0.05, 0.08, 0.10, 0.15]:
            m_rate = rate / 12
            if m_rate == 0:
                f_value = total_invested
            else:
                f_value = monthly_amount * ((1 + m_rate) ** months - 1) / m_rate
            t_return = f_value - total_invested
            report += f"| {rate*100:.0f}% | {f_value:.0f}元 | {t_return:.0f}元 |\n"
        
        return report
    
    def generate_schedule(self, monthly_amount, start_date, years, day_of_month=1):
        """
        生成定投计划表
        
        Args:
            monthly_amount: 每月定投金额
            start_date: 开始日期
            years: 定投年数
            day_of_month: 每月几号定投
        """
        schedule = f"""
# 定投计划表
生成时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## 基本信息
- 每月定投：{monthly_amount}元
- 开始日期：{start_date}
- 定投年数：{years}年
- 定投日期：每月{day_of_month}号

## 定投时间表（前12个月）

| 期数 | 定投日期 | 定投金额 | 累计投入 |
|------|---------|---------|---------|
"""
        cumulative = 0
        for i in range(min(12, years * 12)):
            cumulative += monthly_amount
            schedule += f"| {i+1} | 第{i+1}月{day_of_month}号 | {monthly_amount}元 | {cumulative}元 |\n"
        
        if years * 12 > 12:
            schedule += f"| ... | ... | ... | ... |\n"
            schedule += f"| {years*12} | 第{years*12}月{day_of_month}号 | {monthly_amount}元 | {monthly_amount * years * 12}元 |\n"
        
        return schedule
    
    def stop_profit_analysis(self, target_return_rate):
        """
        止盈策略分析
        
        Args:
            target_return_rate: 目标收益率
        """
        analysis = f"""
# 止盈策略分析

## 目标收益率：{target_return_rate*100:.0f}%

## 止盈策略建议

### 策略一：目标止盈
- 达到{target_return_rate*100:.0f}%收益时全部赎回
- 优点：简单明确
- 缺点：可能错过后续上涨

### 策略二：分批止盈
- 达到{target_return_rate*100:.0f}%收益时赎回50%
- 继续上涨{target_return_rate*100:.0f}%时再赎回剩余50%
- 优点：兼顾止盈和继续上涨
- 缺点：操作复杂

### 策略三：移动止盈
- 达到{target_return_rate*100:.0f}%收益后设置回撤止盈
- 从最高点回撤10%时全部赎回
- 优点：能吃到更多上涨
- 缺点：可能回撤较多

## 建议
- 新手建议使用策略一（目标止盈）
- 有经验后可尝试策略二或三
- 定投时间越长，止盈目标可适当提高
"""
        return analysis

if __name__ == "__main__":
    calc = DIPCalculator()
    print(calc.calculate_return(1000, 3, 0.08))
