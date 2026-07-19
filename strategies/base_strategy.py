class BaseStrategy:
    def generate_signal(self):
        raise NotImplemented(
            'Every strategy must implement generate_signals()'
        )
    