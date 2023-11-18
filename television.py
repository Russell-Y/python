class Television: 
  '''
  Default values and variables, all values type -> int. 
  '''
  MIN_VOLUME = 0
  MAX_VOLUME = 2
  MIN_CHANNEL = 0
  MAX_CHANNEL = 3
  
  def __init__(self): 
    '''
    Set all variables to private. 
    '''
    self.__status = False
    self.__muted = False
    self.__volume = MIN_VOLUME
    self.__channel = MIN_CHANNEL

  def power(self): 
    '''
    Changes status variable to True when activating power on tv. 
    '''
    self.__status = True
    return self.__status
  
  def mute(self): 
    '''
    Changes volume to mute (True) with muted variable when activated. 
    '''
    self.__muted = True
    return self.__muted
  
  def channel_up(self): 
    #All channel variables type -> int. 
    '''
    Cycles through all channels like an actual tv when constantly activated. 
    '''
    if self.__channel == MAX_CHANNEL: 
      self.__channel = MIN_CHANNEL
    else: 
      self.__channel += 1
    return self.__channel
  
  def channel_down(self): 
    #All channel variables type -> int. 
    '''
    Switches to maximum channel when (descending) beyond the minimum channel, parentheses replace double quotation to express. 
    '''
    if self.__channel == MIN_CHANNEL: 
      self.__channel = MAX_CHANNEL
    else: 
      self.__channel -= 1
    return self.__channel
    
  def volume_up(self): 
    #All volume variables type -> int. 
    '''
    Stays at maximum volume like an actual tv when constantly activated. 
    '''
    if self.__volume == MAX_VOLUME: 
      self.__volume = MAX_VOLUME
    else: 
      self.__volume += 1
    return self.__volume
  
  def volume_down(self): 
    #All volume variables type -> int. 
    '''
    Stays at minimum volume like an actual tv when constantly activated. 
    '''
    if self.__volume == MIN_VOLUME: 
      self.__volume = MIN_VOLUME
    else: 
      self.__volume -= 1
    return self.__volume
    
  def __str__(self): 
    '''
    Returns all variables and values to display when activated. 
    '''
    return f'Power = [{status}], Channel = [{channel}], Volume = [{volume}]'
    


