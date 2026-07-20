'''
# Total Trades
# Winning Trades
# Losing Trades
# Win Rate
# Total Profit
# Total Loss
# Net PnL
# Final Capital
# Total Return (%)
# Average Profit
# Average Loss
Profit Factor
'''


class GetMetrics:
    def __init__(self, state_history):
        self.state_history = state_history

    def __total_profit(self):
        total_profit = 0.0
        count = 0

        for trade in self.state_history:
            total_profit += trade.get("profit", 0.0)
            if trade.get("profit", 0.0) > 0:
                count += 1

        avg_profit = total_profit / count if count else 0.0
        return total_profit, avg_profit

    def __total_loss(self):
        total_loss = 0.0
        count = 0

        for trade in self.state_history:
            total_loss += trade.get("loss", 0.0)
            if trade.get("loss", 0.0) > 0:
                count += 1

        avg_loss = total_loss / count if count else 0.0
        return total_loss, avg_loss

    def __win_loss_trade(self):
        win_trade = 0
        loss_trade = 0

        for trade in self.state_history:
            if trade.get("profit", 0.0) > 0:
                win_trade += 1
            if trade.get("loss", 0.0) > 0:
                loss_trade += 1

        return win_trade, loss_trade

    def metrics(self):
        win_trade, loss_trade = self.__win_loss_trade()
        total_profit, avg_profit = self.__total_profit()
        total_loss, avg_loss = self.__total_loss()

        total_trades = len(self.state_history)
        win_rate = win_trade / total_trades if total_trades else 0.0
        net_pnl = total_profit - total_loss

        final_capital = self.state_history[-1]["amount"] if self.state_history else 0.0
        initial_capital = self.state_history[0]['initial_amount'] if self.state_history else 0.0
        total_return = (
            ((final_capital - initial_capital) / initial_capital) * 100
            if initial_capital != 0
            else 0.0
        )

        profit_factor = total_profit / total_loss if total_loss else float("inf")

        return {
            "win_trades": win_trade,
            "loss_trades": loss_trade,
            "total_trades": total_trades,
            "win_rate": win_rate,
            "total_loss": total_loss,
            "total_profit": total_profit,
            "net_pnl": net_pnl,
            "final_capital": final_capital,
            "total_return": total_return,
            "avg_profit": avg_profit,
            "avg_loss": avg_loss,
            "profit_factor": profit_factor,
        }
