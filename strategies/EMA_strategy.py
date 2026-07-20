from .base_strategy import BaseStrategy


class EMAStrategy(BaseStrategy):

    def __init__(self, ema_1: int, ema_2: int):
        self.ema_1 = ema_1
        self.ema_2 = ema_2

    @staticmethod
    def _to_float2(value):
        if value is None:
            return None
        return float(f"{float(value):.2f}")

    def _ema_slope(self, latest, previous, short_ema, long_ema):
        # Use ATR to decide whether the EMA movement is strong enough

        atr = latest["ATR"]
        threshold = atr * 0.2

        short_slope = latest[short_ema] - previous[short_ema]
        long_slope = latest[long_ema] - previous[long_ema]

        if short_slope > threshold and long_slope > threshold:
            trend = "Bullish"

        elif short_slope < -threshold and long_slope < -threshold:
            trend = "Bearish"

        else:
            trend = "Sideways"

        return {
            "trend": trend,
            "short_slope": self._to_float2(short_slope),
            "long_slope": self._to_float2(long_slope),
            "threshold": self._to_float2(threshold),
        }
    
    # volume in the market -> does this breakout have enough volume?
    def _volume_confirmation(self, data):
        current_volume = data.iloc[-1]["Volume"]
        average_volume = data["Volume"].tail(20).mean()

        return {
            "confirmed": True if current_volume > average_volume else False,
            "current_volume": self._to_float2(current_volume),
            "average_volume": self._to_float2(average_volume)
        }
    
    # stoploss
    def _stop_loss(self, signal, entry_price, atr):
        multiplier = 2

        if signal == "BUY":
            return self._to_float2(entry_price - multiplier * atr)

        elif signal == "SELL":
            return self._to_float2(entry_price + multiplier * atr)

        return None

# target hit
    def _target(self, signal, entry_price, stop_loss):
        if stop_loss is None:
            return None

        risk = abs(entry_price - stop_loss)
        reward_ratio = 2

        if signal == "BUY":
            return self._to_float2(entry_price + reward_ratio * risk)

        elif signal == "SELL":
            return self._to_float2(entry_price - reward_ratio * risk)
        return None
    
    # confidence score 
    def _confidence(self, signal, trend_info, volume_info):
        if signal == "HOLD":
            return 0.0

        confidence = 0.5

        if ( signal == "BUY" and trend_info["trend"] == "Bullish"):
            confidence += 0.25

        elif (signal == "SELL"and trend_info["trend"] == "Bearish"):
            confidence += 0.25

        if volume_info["confirmed"]:
            confidence += 0.25

        return self._to_float2(confidence)
# signal generator using crossover detection
    def generate_signal(self, data):

        if data.empty:
            raise ValueError("DataFrame is empty.")

        short_ema = f"EMA_{self.ema_1}"
        long_ema = f"EMA_{self.ema_2}"

        required_columns = [short_ema, long_ema, "ATR"]

        for column in required_columns:
            if column not in data.columns:
                raise ValueError(f"Required column '{column}' not found.")

        if len(data) < 2:
            raise ValueError("At least two candles are required.")

        latest = data.iloc[-1]
        previous = data.iloc[-2]

        latest_close = self._to_float2(latest["Close"])

        short_ema_latest = self._to_float2(latest[short_ema])
        long_ema_latest = self._to_float2(latest[long_ema])

        short_ema_prev = self._to_float2(previous[short_ema])
        long_ema_prev = self._to_float2(previous[long_ema])

        # Check whether a new crossover has occurred

        if (
            short_ema_prev <= long_ema_prev
            and short_ema_latest > long_ema_latest
        ):
            signal = "BUY"

            reason = (
                f"Bullish crossover: "
                f"{self._to_float2(short_ema_prev)} <= {self._to_float2(long_ema_prev)} "
                f"and "
                f"{self._to_float2(short_ema_latest)} > {self._to_float2(long_ema_latest)}"
            )
            

        elif (
            short_ema_prev > long_ema_prev
            and short_ema_latest <= long_ema_latest
        ):
            signal = "SELL"

            reason = (
                f"Bearish crossover: "
                f"{self._to_float2(short_ema_prev)} > {self._to_float2(long_ema_prev)} "
                f"and "
                f"{self._to_float2(short_ema_latest)} <= {self._to_float2(long_ema_latest)}"
            )

        else:
            signal = "HOLD"
            reason = "No EMA crossover detected."

        # Reject weak crossovers

        trend_info = self._ema_slope(
            latest,
            previous,
            short_ema,
            long_ema,
        )

        if signal == "BUY" and trend_info["trend"] != "Bullish":
            signal = "HOLD"
            reason = "Bullish crossover rejected due to weak EMA slope."

        elif signal == "SELL" and trend_info["trend"] != "Bearish":
            signal = "HOLD"
            reason = "Bearish crossover rejected due to weak EMA slope."
        
        volume_info = self._volume_confirmation(data)

        if signal != "HOLD" and not volume_info["confirmed"]:
            signal = "HOLD"
            reason = "Signal rejected due to low trading volume."
        
        stop_loss = self._stop_loss(
                signal,
                latest_close,
                latest["ATR"]
            )
        
        
        target = self._target(
                signal,
                latest_close,
                stop_loss
            )
        
        confidence = self._confidence(
                    signal,
                    trend_info,
                    volume_info
                )
        
        return {
        "signal": signal,
        "price": latest_close,
        "stop_loss": stop_loss,
        "target": target,
        "confidence": confidence,
        "reason": reason,
        "ema_slope": trend_info,
        "volume": volume_info,
       "date": data.index[-1]
        }
        
        
        
        