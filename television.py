class Television: 
  MIN_VOLUME = 0
  MAX_VOLUME = 2
  MIN_CHANNEL = 0
  MAX_CHANNEL = 3
  
  def __init__(self): 
    self.__status = False
    self.__muted = False
    self.__volume += MIN_VOLUME
    self.__channel += MIN_CHANNEL

  def power(self): 

    return self.__status
  def mute(self): 

    return self.__muted
  def channel_up(self): 
    if self.__channel == MAX_CHANNEL: 
      self.__channel += MIN_CHANNEL
    else: 
      self.__channel += 1
    return self.__channel
  def channel_down(self): 

  def volume_up(self): 
    if self.__volume == MAX_VOLUME: 
      self.__volume += MIN_VOLUME
    else: 
      self.__volume += 1
    return self.__volume
  def volume_down(self): 

  def __str__(self): 

    


