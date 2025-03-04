# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from sbg_driver/SbgMag.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import geometry_msgs.msg
import sbg_driver.msg
import std_msgs.msg

class SbgMag(genpy.Message):
  _md5sum = "de7614c4cbb6cbd430c4a9b79bad88ca"
  _type = "sbg_driver/SbgMag"
  _has_header = True  # flag to mark the presence of a Header object
  _full_text = """# SBG Ellipse Messages
Header header

# Time since sensor is powered up (us)
uint32 time_stamp

# Magnetometer output (X, Y, Z)
geometry_msgs/Vector3 mag

# Accelerometer output (X, Y, Z) in m/s2
geometry_msgs/Vector3 accel

# Status
SbgMagStatus status

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
string frame_id

================================================================================
MSG: geometry_msgs/Vector3
# This represents a vector in free space. 
# It is only meant to represent a direction. Therefore, it does not
# make sense to apply a translation to it (e.g., when applying a 
# generic rigid transformation to a Vector3, tf2 will only apply the
# rotation). If you want your data to be translatable too, use the
# geometry_msgs/Point message instead.

float64 x
float64 y
float64 z
================================================================================
MSG: sbg_driver/SbgMagStatus
# SBG Ellipse Messages
# Submessage

# True if the magnetometer X has passed the self test.
bool mag_x

# True if the magnetometer Y has passed the self test.
bool mag_y

# True if the magnetometer Z has passed the self test.
bool mag_z

# True if the accelerometer X has passed the self test.
bool accel_x

# True if the accelerometer Y has passed the self test.
bool accel_y

# True if the accelerometer Z has passed the self test.
bool accel_z

# True if magnetometer is not saturated
bool mags_in_range

# True if accelerometer is not saturated
bool accels_in_range

# True if magnetometer seems to be calibrated
bool calibration
"""
  __slots__ = ['header','time_stamp','mag','accel','status']
  _slot_types = ['std_msgs/Header','uint32','geometry_msgs/Vector3','geometry_msgs/Vector3','sbg_driver/SbgMagStatus']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       header,time_stamp,mag,accel,status

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(SbgMag, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.time_stamp is None:
        self.time_stamp = 0
      if self.mag is None:
        self.mag = geometry_msgs.msg.Vector3()
      if self.accel is None:
        self.accel = geometry_msgs.msg.Vector3()
      if self.status is None:
        self.status = sbg_driver.msg.SbgMagStatus()
    else:
      self.header = std_msgs.msg.Header()
      self.time_stamp = 0
      self.mag = geometry_msgs.msg.Vector3()
      self.accel = geometry_msgs.msg.Vector3()
      self.status = sbg_driver.msg.SbgMagStatus()

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
      _x = self
      buff.write(_get_struct_3I().pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_I6d9B().pack(_x.time_stamp, _x.mag.x, _x.mag.y, _x.mag.z, _x.accel.x, _x.accel.y, _x.accel.z, _x.status.mag_x, _x.status.mag_y, _x.status.mag_z, _x.status.accel_x, _x.status.accel_y, _x.status.accel_z, _x.status.mags_in_range, _x.status.accels_in_range, _x.status.calibration))
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
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.mag is None:
        self.mag = geometry_msgs.msg.Vector3()
      if self.accel is None:
        self.accel = geometry_msgs.msg.Vector3()
      if self.status is None:
        self.status = sbg_driver.msg.SbgMagStatus()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 61
      (_x.time_stamp, _x.mag.x, _x.mag.y, _x.mag.z, _x.accel.x, _x.accel.y, _x.accel.z, _x.status.mag_x, _x.status.mag_y, _x.status.mag_z, _x.status.accel_x, _x.status.accel_y, _x.status.accel_z, _x.status.mags_in_range, _x.status.accels_in_range, _x.status.calibration,) = _get_struct_I6d9B().unpack(str[start:end])
      self.status.mag_x = bool(self.status.mag_x)
      self.status.mag_y = bool(self.status.mag_y)
      self.status.mag_z = bool(self.status.mag_z)
      self.status.accel_x = bool(self.status.accel_x)
      self.status.accel_y = bool(self.status.accel_y)
      self.status.accel_z = bool(self.status.accel_z)
      self.status.mags_in_range = bool(self.status.mags_in_range)
      self.status.accels_in_range = bool(self.status.accels_in_range)
      self.status.calibration = bool(self.status.calibration)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_3I().pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_I6d9B().pack(_x.time_stamp, _x.mag.x, _x.mag.y, _x.mag.z, _x.accel.x, _x.accel.y, _x.accel.z, _x.status.mag_x, _x.status.mag_y, _x.status.mag_z, _x.status.accel_x, _x.status.accel_y, _x.status.accel_z, _x.status.mags_in_range, _x.status.accels_in_range, _x.status.calibration))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.mag is None:
        self.mag = geometry_msgs.msg.Vector3()
      if self.accel is None:
        self.accel = geometry_msgs.msg.Vector3()
      if self.status is None:
        self.status = sbg_driver.msg.SbgMagStatus()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 61
      (_x.time_stamp, _x.mag.x, _x.mag.y, _x.mag.z, _x.accel.x, _x.accel.y, _x.accel.z, _x.status.mag_x, _x.status.mag_y, _x.status.mag_z, _x.status.accel_x, _x.status.accel_y, _x.status.accel_z, _x.status.mags_in_range, _x.status.accels_in_range, _x.status.calibration,) = _get_struct_I6d9B().unpack(str[start:end])
      self.status.mag_x = bool(self.status.mag_x)
      self.status.mag_y = bool(self.status.mag_y)
      self.status.mag_z = bool(self.status.mag_z)
      self.status.accel_x = bool(self.status.accel_x)
      self.status.accel_y = bool(self.status.accel_y)
      self.status.accel_z = bool(self.status.accel_z)
      self.status.mags_in_range = bool(self.status.mags_in_range)
      self.status.accels_in_range = bool(self.status.accels_in_range)
      self.status.calibration = bool(self.status.calibration)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_3I = None
def _get_struct_3I():
    global _struct_3I
    if _struct_3I is None:
        _struct_3I = struct.Struct("<3I")
    return _struct_3I
_struct_I6d9B = None
def _get_struct_I6d9B():
    global _struct_I6d9B
    if _struct_I6d9B is None:
        _struct_I6d9B = struct.Struct("<I6d9B")
    return _struct_I6d9B
