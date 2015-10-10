"""
Code from Dr. Tim Menzies
See license https://github.com/txt/mase/blob/master/LICENSE.md
"""

class o:
  """Emulate Javascript's uber simple objects.
  Note my convention: I use "`i`" not "`this`."""
  def __init__(i,**d)    : i.__dict__.update(d)
  def __setitem__(i,k,v) : i.__dict__[k] = v
  def __getitem__(i,k)   : return i.__dict__[k]
  def __repr__(i)        : return 'o'+str(i.__dict__)
