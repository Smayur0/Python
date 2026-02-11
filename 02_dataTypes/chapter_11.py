import arrow

brew_time = arrow.utcnow()
brew_time.to("Asia/Kolkata")
print(f"Current brew time in Kolkata: {brew_time}")    


from collections import namedtuple
Tea = namedtuple("Tea", ["type", "size", "sugar"])
