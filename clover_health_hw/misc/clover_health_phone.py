# 1000  -> '1,000'
# -1000 -> '-1,000'
# 0    -> '0'
# 10000000 -> '1,000,000'
# abc ->



def positiveNumberToComponents(number):
  number_string = str(number)
  components = []
  component = ""
  idx = len(number_string) - 1


  while idx >= 0:
    component = number_string[idx] + component

    if len(component) == 3:
      components.insert(0, component)
      component = ""
    idx -= 1

  if len(component) > 0:
    components.insert(0, component)
  return components


def numberToString(number):
  sign_component = None
  if number < 0:
    number = abs(number)
    sign_component = "-"

  components = positiveNumberToComponents(number)
  res = ','.join(components)
  if sign_component:
    res = sign_component + ','.join(components)

  return res

print numberToString(1000)
print numberToString(1000000)
print numberToString(10)
print numberToString(100)
print numberToString(1234)
print numberToString(-1)
print numberToString(-123)
print numberToString(-1234)
print numberToString(-12347654)
