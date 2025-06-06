# This python3 file uses the following encoding: utf-8
"""autogenerated by genpy from yocs_msgs/TrajectoryList.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import geometry_msgs.msg
import std_msgs.msg
import yocs_msgs.msg

class TrajectoryList(genpy.Message):
  _md5sum = "f0901d378c8ac2d2d3d8feafaa343a58"
  _type = "yocs_msgs/TrajectoryList"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """# A list of trajectories
Trajectory[] trajectories

================================================================================
MSG: yocs_msgs/Trajectory
# A named list of way points
Header header
string name
Waypoint[] waypoints

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in python3 the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in python3 the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
string frame_id

================================================================================
MSG: yocs_msgs/Waypoint
Header header
string name
geometry_msgs/Pose pose

================================================================================
MSG: geometry_msgs/Pose
# A representation of pose in free space, composed of position and orientation. 
Point position
Quaternion orientation

================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z

================================================================================
MSG: geometry_msgs/Quaternion
# This represents an orientation in free space in quaternion form.

float64 x
float64 y
float64 z
float64 w
"""
  __slots__ = ['trajectories']
  _slot_types = ['yocs_msgs/Trajectory[]']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       trajectories

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(TrajectoryList, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.trajectories is None:
        self.trajectories = []
    else:
      self.trajectories = []

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
      length = len(self.trajectories)
      buff.write(_struct_I.pack(length))
      for val1 in self.trajectories:
        _v1 = val1.header
        _x = _v1.seq
        buff.write(_get_struct_I().pack(_x))
        _v2 = _v1.stamp
        _x = _v2
        buff.write(_get_struct_2I().pack(_x.secs, _x.nsecs))
        _x = _v1.frame_id
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
        _x = val1.name
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
        length = len(val1.waypoints)
        buff.write(_struct_I.pack(length))
        for val2 in val1.waypoints:
          _v3 = val2.header
          _x = _v3.seq
          buff.write(_get_struct_I().pack(_x))
          _v4 = _v3.stamp
          _x = _v4
          buff.write(_get_struct_2I().pack(_x.secs, _x.nsecs))
          _x = _v3.frame_id
          length = len(_x)
          if python3 or type(_x) == unicode:
            _x = _x.encode('utf-8')
            length = len(_x)
          buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
          _x = val2.name
          length = len(_x)
          if python3 or type(_x) == unicode:
            _x = _x.encode('utf-8')
            length = len(_x)
          buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
          _v5 = val2.pose
          _v6 = _v5.position
          _x = _v6
          buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
          _v7 = _v5.orientation
          _x = _v7
          buff.write(_get_struct_4d().pack(_x.x, _x.y, _x.z, _x.w))
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
      if self.trajectories is None:
        self.trajectories = None
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.trajectories = []
      for i in range(0, length):
        val1 = yocs_msgs.msg.Trajectory()
        _v8 = val1.header
        start = end
        end += 4
        (_v8.seq,) = _get_struct_I().unpack(str[start:end])
        _v9 = _v8.stamp
        _x = _v9
        start = end
        end += 8
        (_x.secs, _x.nsecs,) = _get_struct_2I().unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          _v8.frame_id = str[start:end].decode('utf-8', 'rosmsg')
        else:
          _v8.frame_id = str[start:end]
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.name = str[start:end].decode('utf-8', 'rosmsg')
        else:
          val1.name = str[start:end]
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        val1.waypoints = []
        for i in range(0, length):
          val2 = yocs_msgs.msg.Waypoint()
          _v10 = val2.header
          start = end
          end += 4
          (_v10.seq,) = _get_struct_I().unpack(str[start:end])
          _v11 = _v10.stamp
          _x = _v11
          start = end
          end += 8
          (_x.secs, _x.nsecs,) = _get_struct_2I().unpack(str[start:end])
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          start = end
          end += length
          if python3:
            _v10.frame_id = str[start:end].decode('utf-8', 'rosmsg')
          else:
            _v10.frame_id = str[start:end]
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          start = end
          end += length
          if python3:
            val2.name = str[start:end].decode('utf-8', 'rosmsg')
          else:
            val2.name = str[start:end]
          _v12 = val2.pose
          _v13 = _v12.position
          _x = _v13
          start = end
          end += 24
          (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
          _v14 = _v12.orientation
          _x = _v14
          start = end
          end += 32
          (_x.x, _x.y, _x.z, _x.w,) = _get_struct_4d().unpack(str[start:end])
          val1.waypoints.append(val2)
        self.trajectories.append(val1)
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
      length = len(self.trajectories)
      buff.write(_struct_I.pack(length))
      for val1 in self.trajectories:
        _v15 = val1.header
        _x = _v15.seq
        buff.write(_get_struct_I().pack(_x))
        _v16 = _v15.stamp
        _x = _v16
        buff.write(_get_struct_2I().pack(_x.secs, _x.nsecs))
        _x = _v15.frame_id
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
        _x = val1.name
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
        length = len(val1.waypoints)
        buff.write(_struct_I.pack(length))
        for val2 in val1.waypoints:
          _v17 = val2.header
          _x = _v17.seq
          buff.write(_get_struct_I().pack(_x))
          _v18 = _v17.stamp
          _x = _v18
          buff.write(_get_struct_2I().pack(_x.secs, _x.nsecs))
          _x = _v17.frame_id
          length = len(_x)
          if python3 or type(_x) == unicode:
            _x = _x.encode('utf-8')
            length = len(_x)
          buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
          _x = val2.name
          length = len(_x)
          if python3 or type(_x) == unicode:
            _x = _x.encode('utf-8')
            length = len(_x)
          buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
          _v19 = val2.pose
          _v20 = _v19.position
          _x = _v20
          buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
          _v21 = _v19.orientation
          _x = _v21
          buff.write(_get_struct_4d().pack(_x.x, _x.y, _x.z, _x.w))
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
      if self.trajectories is None:
        self.trajectories = None
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.trajectories = []
      for i in range(0, length):
        val1 = yocs_msgs.msg.Trajectory()
        _v22 = val1.header
        start = end
        end += 4
        (_v22.seq,) = _get_struct_I().unpack(str[start:end])
        _v23 = _v22.stamp
        _x = _v23
        start = end
        end += 8
        (_x.secs, _x.nsecs,) = _get_struct_2I().unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          _v22.frame_id = str[start:end].decode('utf-8', 'rosmsg')
        else:
          _v22.frame_id = str[start:end]
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.name = str[start:end].decode('utf-8', 'rosmsg')
        else:
          val1.name = str[start:end]
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        val1.waypoints = []
        for i in range(0, length):
          val2 = yocs_msgs.msg.Waypoint()
          _v24 = val2.header
          start = end
          end += 4
          (_v24.seq,) = _get_struct_I().unpack(str[start:end])
          _v25 = _v24.stamp
          _x = _v25
          start = end
          end += 8
          (_x.secs, _x.nsecs,) = _get_struct_2I().unpack(str[start:end])
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          start = end
          end += length
          if python3:
            _v24.frame_id = str[start:end].decode('utf-8', 'rosmsg')
          else:
            _v24.frame_id = str[start:end]
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          start = end
          end += length
          if python3:
            val2.name = str[start:end].decode('utf-8', 'rosmsg')
          else:
            val2.name = str[start:end]
          _v26 = val2.pose
          _v27 = _v26.position
          _x = _v27
          start = end
          end += 24
          (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
          _v28 = _v26.orientation
          _x = _v28
          start = end
          end += 32
          (_x.x, _x.y, _x.z, _x.w,) = _get_struct_4d().unpack(str[start:end])
          val1.waypoints.append(val2)
        self.trajectories.append(val1)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_2I = None
def _get_struct_2I():
    global _struct_2I
    if _struct_2I is None:
        _struct_2I = struct.Struct("<2I")
    return _struct_2I
_struct_3d = None
def _get_struct_3d():
    global _struct_3d
    if _struct_3d is None:
        _struct_3d = struct.Struct("<3d")
    return _struct_3d
_struct_4d = None
def _get_struct_4d():
    global _struct_4d
    if _struct_4d is None:
        _struct_4d = struct.Struct("<4d")
    return _struct_4d
