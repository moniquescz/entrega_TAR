# This python3 file uses the following encoding: utf-8
"""autogenerated by genpy from kobuki_msgs/PowerSystemEvent.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class PowerSystemEvent(genpy.Message):
  _md5sum = "f6464657d6c911b00c7bc7b43a154bf8"
  _type = "kobuki_msgs/PowerSystemEvent"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """# Power system events
# This message is generated by important changes in the power system:
#  - plug/unplug to the docking base or adapter
#  - transitions to low/critical battery levels
#  - battery charge completed

uint8 UNPLUGGED           = 0
uint8 PLUGGED_TO_ADAPTER  = 1
uint8 PLUGGED_TO_DOCKBASE = 2
uint8 CHARGE_COMPLETED    = 3
uint8 BATTERY_LOW         = 4
uint8 BATTERY_CRITICAL    = 5

uint8 event
"""
  # Pseudo-constants
  UNPLUGGED = 0
  PLUGGED_TO_ADAPTER = 1
  PLUGGED_TO_DOCKBASE = 2
  CHARGE_COMPLETED = 3
  BATTERY_LOW = 4
  BATTERY_CRITICAL = 5

  __slots__ = ['event']
  _slot_types = ['uint8']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       event

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(PowerSystemEvent, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.event is None:
        self.event = 0
    else:
      self.event = 0

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self.event
      buff.write(_get_struct_B().pack(_x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      start = end
      end += 1
      (self.event,) = _get_struct_B().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python3 module
    """
    try:
      _x = self.event
      buff.write(_get_struct_B().pack(_x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python3 module
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      start = end
      end += 1
      (self.event,) = _get_struct_B().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_B = None
def _get_struct_B():
    global _struct_B
    if _struct_B is None:
        _struct_B = struct.Struct("<B")
    return _struct_B
