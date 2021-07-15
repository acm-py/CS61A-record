# import curses


# stdscr = curses.initscr()
# curses.noecho()
# curses.cbreak()
# stdscr.keypad(True)
# def main(stdscr):
#     # Clear screen
#     stdscr.clear()
#     pad = curses.newpad(100, 100)
#     # These loops fill the pad with letters; addch() is
#     # explained in the next section
#     for y in range(0, 99):
#         for x in range(0, 99):
#             pad.addch(y,x, ord('a') + (x*x+y*y) % 26)
#     pad.refresh( 0,0, 5,5, 20,75)

# curses.wrapper(main)
class Property(object):
	"在Object/descrobject.c模拟 PyProperty_Type()"

	def __init__(self, fget=None, fset=None, fdel=None, doc=None):
		self.fget = fget
		self.fset = fset
		self.fdel = fdel
		self.doc = doc
		if doc is None and fget is not None:
			doc = fget.__doc__
		self.__doc__ = doc
	def __get__(self, obj, objtype=None):
		if obj is None:
			return self
		if self.fget is None:
			raise AttributeError("unreadble attribute")
		return self.fget(obj)
	def __set__(self, obj, value):
		if self.fset is None:
			raise AttributeError("can't set attribute")
		self.fset(obj, value)
	def __delete__(self, obj):
		if self.fdel is None:
			raise AttributeError("can't delte a attribute")
		self.fdel(obj)
	def getter(self, fget):
		return type(self)(fget, self.fset, self.fdel, self.__doc__)
	def setter(self, fset):
		return type(self)(self.fget, fset, self.fdel, self.__doc__)
    #def deleter(self, fdel):
    #     return type(self)(self.fget, self.fset, fdel, self.__doc__)

a = Property()
