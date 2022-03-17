class FlatIterator:
   def __init__(self, iterable):
      self._iterable = self._flatten(iterable)
      self._counter = 0

   def __iter__(self):
      return self
   
   def __next__(self):
      if self._counter < len(self._iterable):
         self._counter += 1
         return self._iterable[self._counter - 1]
      else:
         raise StopIteration
   
   def _flatten(self, arg):
      ret = []
      if type(arg) == list:
         for item in arg:
            ret.extend(self._flatten(item))
      else:
         ret.append(arg)
      return ret

def main():
   
   nested_list = [
      ['a', 'b', 'c'],
      ['d', 'e', 'f', 'h', False],
      [1, 2, None],
   ]
   my_iter = FlatIterator(nested_list)
   for item in my_iter:
      print(item)

if __name__ == "__main__":
   main()