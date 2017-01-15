class LightSwitch():
    def __init__(self, state):
        if state == 'on':
            self._state = True
        elif state == 'off':
            self._state = False

    def switch_on(self):
        self._state = True

    def switch_off(self):
        self._state = False

    def flip(self):
        self._state = not self._state

    def get_state(self):
        state = self._state
        return state

    def __str__(self):
        if self._state:
            state = 'on'
        else:
            state = 'off'
            return "I am " + state


class SwitchBoard():
    def __init__(self, switches):
        self._switches = []
        for counter in range(switches):
            new_switch = LightSwitch("off")
            self._switches.append(new_switch)

    def __str__(self):
        ok = self.which_switch()
        for switch in range(switches):
            if(self._switches[switch] is true):
                On_switches += ' ' + str(switch)
        return 'The following switches are on: ' + " ".join(str(x) for x in ok)

    def which_switch(self):
        self._switches_on = []
        for on in range(len(self._switches)):
            if self._switches[on].get_state() is True:
                self._switches_on.append(on)
        return(self._switches_on)

    def flip(self, n):
        self._switches[n].flip()

    def flip_every(self, n):
        counter = 0
        while counter < len(self._switches):
            self._switches[counter].flip()
            counter += n

    def reset(self):
        for reset in range(len(self._switches)):
            self._switches[reset].switch_off()

    def solution(self):
        for solution in range(1, len(self._switches)):
            self.flip_every(solution)
