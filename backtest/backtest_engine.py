from typing import TypedDict


class State(TypedDict):
    initial_amount:float|None
    position: bool | None
    entry_date: str | None
    entry_price: float | None
    exit_date: str | None
    exit_price: float | None
    quantity: int | None
    profit: float | None
    loss: float | None
    pnl: float | None
    amount: float | None
    winning_trade : int
    loosing_trade : int


class BackTest:

    def __init__(self, amount):
        self.amount = amount
        self.position = False
        self.state_history = []

        self.state: State = {
            'initial_amount':self.amount,
            "position": None,
            "entry_date": None,
            "entry_price": None,
            "exit_date": None,
            "exit_price": None,
            "quantity": None,
            "profit": None,
            "loss": None,
            "pnl": None,
            "amount": amount,
            'winning_trade' : 0,
            'loosing_trade' : 0
        }

    def _reset_state(self) -> State:
        return {
            'initial_amount':self.amount,
            "position": None,
            "entry_date": None,
            "entry_price": None,
            "exit_date": None,
            "exit_price": None,
            "quantity": None,
            "profit": None,
            "loss": None,
            "pnl": None,
            "amount": self.amount,
            'winning_trade' : 0,
            'loosing_trade' : 0
        }

    def back_test_engine(self, data, strategy):
        

        for c in range(1, len(data)):
            signal_result = strategy.generate_signal(data[: c + 1])
            signal = signal_result.get("signal")

            if signal == "HOLD":
                continue

            current_date = signal_result.get("date", data.index[c])
            current_price = float(signal_result.get("price", data.iloc[c]["Close"]))

            if signal == "BUY":
                if self.position:
                    continue

                print("BUY signal received...")

                quantity = int(self.amount // current_price)

                if quantity == 0:
                    self.position = False
                    continue

                self.position = True
                self.state["position"] = True
                self.state["entry_date"] = current_date
                self.state["entry_price"] = current_price
                self.state["quantity"] = quantity

                invested_amount = quantity * current_price
                self.amount -= invested_amount
                self.state["amount"] = self.amount

                print(f"Bought {quantity} shares @ {current_price}")
                print(f"Cash Left : {self.amount:.2f}")

            elif signal == "SELL":
                if not self.position:
                    continue

                print("SELL signal received")

                self.position = False
                self.state["position"] = False
                self.state["exit_date"] = current_date
                self.state["exit_price"] = current_price

                return_per_share = self.state["exit_price"] - self.state["entry_price"]
                pnl = return_per_share * self.state["quantity"]

                self.state["pnl"] = pnl

                if pnl >= 0:
                    self.state["profit"] = pnl
                    self.state['winning_trade']+=1
                    self.state["loss"] = 0.0
                else:
                    self.state["profit"] = 0.0
                    self.state["loss"] = abs(pnl)
                    self.state['loosing_trade'] +=1

                total_sell_value = self.state["quantity"] * self.state["exit_price"]
                self.amount += total_sell_value
                self.state["amount"] = self.amount

                print(f"Sold {self.state['quantity']} shares @ {current_price}")
                print(f"PnL : {pnl:.2f}")
                print(f"Cash Available : {self.amount:.2f}")

                self.state_history.append(self.state.copy())
                self.state = self._reset_state()

        # print("\nTrade History")
        # for trade in self.state_history:
        #     print(trade)

        return self.state_history