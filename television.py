class Television: 
  MIN_VOLUME = 0
  MAX_VOLUME = 2
  MIN_CHANNEL = 0
  MAX_CHANNEL = 3
  
  def __init__(self): 
    self.__status = False
    self.__muted = False
    self.__volume = MIN_VOLUME
    self.__channel = MIN_CHANNEL

  def power(self): 
    self.__status = True
    return self.__status
  
  def mute(self): 
    self.__muted = True
    return self.__muted
  
  def channel_up(self): 
    if self.__channel == MAX_CHANNEL: 
      self.__channel = MIN_CHANNEL
    else: 
      self.__channel += 1
    return self.__channel
  
  def channel_down(self): 
    if self.__channel == MIN_CHANNEL: 
      self.__channel = MAX_CHANNEL
    else: 
      self.__channel -= 1
    return self.__channel
    
  def volume_up(self): 
    if self.__volume == MAX_VOLUME: 
      self.__volume = MAX_VOLUME
    else: 
      self.__volume += 1
    return self.__volume
  
  def volume_down(self): 
    if self.__volume == MIN_VOLUME: 
      self.__volume = MIN_VOLUME
    else: 
      self.__volume -= 1
    return self.__volume
    
  def __str__(self): 
    return f'Power = [{status}], Channel = [{channel}], Volume = [{volume}]'
    


