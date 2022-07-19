
def beta(a):
  def inner():
    print("added beta")
    a()
  return inner

def alpha(f):
  def inner():
    print("added alpha")
    f()
  return inner

@alpha
@beta
def monroe():
  print("i am monroe")

if __name__ == "__main__":
  monroe()


