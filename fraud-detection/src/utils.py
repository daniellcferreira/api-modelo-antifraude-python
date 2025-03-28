# converter a hora em minutos desde 00:00
def hour_to_minutes(hour: str) -> int:
  h, m = map(int, hour.split(':'))
  return h * 60 + m