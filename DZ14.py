s = "I am learning Python. hello, World!"
print(s.replace(s[s.find("h"): s.rfind("h") + 1], s[s.find("h"): s.rfind("h") + 1][::-1]))
