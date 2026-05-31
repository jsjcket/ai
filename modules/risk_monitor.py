"""
风险预警模块
功能：监控持仓、设置预警、大跌提醒
"""

from datetime import datetime

class RiskMonitor:
    def __init__(self):
        self.name = "风险预警模块"
        
    def check_market_risk(self, index_change):
        """
        检查市场风险等级
        
        Args:
            index_change: 指数涨跌幅（如-3.5表示跌3.5%）
        """
        if index_change >= 0:
            risk_level = "正常"
            suggestion = "市场上涨，保持观察"
        elif index_change > -1:
            risk_level = "低风险"
            suggestion = "小幅回调，无需恐慌"
        elif index_change > -2:
            risk_level = "中等风险"
            suggestion = "注意观察，考虑是否加仓"
        elif index_change > -3:
            risk_level = "较高风险"
            suggestion = "谨慎操作，不要盲目抄底"
        elif index_change > -5:
            risk_level = "高风险"
            suggestion = "大跌，冷静观察，不要恐慌卖出"
        else:
            risk_level = "极高风险"
            suggestion = "暴跌，保持冷静，评估是否加仓机会"
        
        return {
            "risk_level": risk_level,
            "change": index_change,
            "suggestion": suggestion
        }
    
    def generate_risk_report(self, positions):
        """
        生成持仓风险报告
        
        Args:
            positions: 持仓列表 [{"name": "基金A", "amount": 10000, "current_return": 0.05}]
        """
        report = f"""
# 持仓风险报告
生成时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## 持仓概览

| 名称 | 持仓金额 | 当前收益率 | 风险提示 |
|------|---------|-----------|---------|
"""
        total_amount = 0
        total_return = 0
        for pos in positions:
            name = pos["name"]
            amount = pos["amount"]
            ret = pos["current_return"]
            total_amount += amount
            total_return += amount * ret
            
            ret_str = f"+{ret*100:.1f}%" if ret >= 0 else f"{ret*100:.1f}%"
            
            if ret < -0.10:
                risk_tip = "⚠️ 亏损超10%"
            elif ret < -0.05:
                risk_tip = "注意亏损"
            elif ret > 0.20:
                risk_tip = "考虑止盈"
            else:
                risk_tip = "正常"
            
            report += f"| {name} | {amount}元 | {ret_str} | {risk_tip} |\n"
        
        avg_return = total_return / total_amount if total_amount > 0 else 0
        avg_return_str = f"+{avg_return*100:.1f}%" if avg_return >= 0 else f"{avg_return*100:.1f}%"
        
        report += f"""
## 汇总
- 总持仓：{total_amount}元
- 总收益：{total_return:.0f}元
- 平均收益率：{avg_return_str}

## 风险提示
"""
        if avg_return < -0.10:
            report += "- ⚠️ 整体亏损超过10%，请评估是否需要调整\n"
        elif avg_return < -0.05:
            report += "- 整体亏损，建议保持冷静，不要恐慌卖出\n"
        elif avg_return > 0.15:
            report += "- 收益较好，可考虑部分止盈\n"
        else:
            report += "- 持仓正常，继续观察\n"
        
        return report
    
    def set_alert(self, alert_type, threshold, message):
        """
        设置预警
        
        Args:
            alert_type: 预警类型 (大跌预警/止盈提醒/定投提醒)
            threshold: 阈值
            message: 提醒消息
        """
        alert = f"""
# 预警设置

## 预警信息
- 预警类型：{alert_type}
- 触发条件：{threshold}
- 提醒消息：{message}

## 预警类型说明

### 大跌预警
- 当指数跌幅超过阈值时触发
- 建议：设置-3%到-5%

### 止盈提醒
- 当收益率超过阈值时触发
- 建议：设置15%到20%

### 定投提醒
- 每月定投日期前提醒
- 建议：设置每月定投日前1天

## 使用方式
1. 将预警设置保存到配置文件
2. 定期运行检查程序
3. 触发条件时发送通知
"""
        return alert

if __name__ == "__main__":
    monitor = RiskMonitor()
    risk = monitor.check_market_risk(-2.5)
    print(f"风险等级：{risk['risk_level']}")
    print(f"建议：{risk['suggestion']}")
