from halo import Halo
from time import sleep

spinner = Halo(text='Loading', spinner='dots')
spinner.start() 
sleep(10)
spinner.stop()