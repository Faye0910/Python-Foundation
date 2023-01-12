from random import randint

class password:
    def abc(self,guess,lowest,highest,answer):
        guess=int(guess)
        lowest=int(lowest)
        highest=int(highest)
        answer=int(answer)
        if guess <= lowest or guess >= highest:
            return(str(str(lowest) + '-' + str(highest)))
        if guess == answer:
            return str('答對了！')
        if guess < answer:
            lowest = guess
            return str(str(lowest) + '-' + str(highest))
        else:
            highest = guess
            return str(str(lowest) + '-' + str(highest))
