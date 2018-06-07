import pyforms
from   pyforms          import BaseWidget
from   pyforms.controls import ControlText
from   pyforms.controls import ControlButton
import sorteio

class Sorteio(BaseWidget):

    def __init__(self):
        super(Sorteio,self).__init__('Sorteio')

        #Definition of the forms field
        self._member1 = ControlText('Membro 1')
        self._member2 = ControlText('Membro 2')
        self._member3 = ControlText('Membro 3')
        self._member4 = ControlText('Membro 4')
        self._member5 = ControlText('Membro 5')
        self._member6 = ControlText('Membro 6')

        self._button = ControlButton('Sorteie agora')

        #Define the button action
        self._button.value = self.__buttonAction

    def __buttonAction(self):
        """Button action event"""
        self._members = [self._member1.value,self._member2.value,self._member3.value,self._member4.value,self._member5.value,self._member6.value]
        print(self._members)
        sorteio(self._members)

#Execute the application
if __name__ == "__main__":   pyforms.start_app( Sorteio )