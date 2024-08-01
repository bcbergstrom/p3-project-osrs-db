from requirements import SkillRequirements
class MMM_Obj:
    def __init__(self, method, profit,time, reqs=None, ):
        #String of Method Name
        self._methods = method
        #Profit of Method (int)
        self._profit = profit
        #Requirements Objeect
        self._reqs = reqs
        #Boolean if Method Takes Time
        self._time = time
    @property
    def reqs(self):
        return self._reqs
    
    @reqs.setter
    def reqs(self, reqs_obj):
        if reqs_obj is SkillRequirements or None:
            self._reqs = reqs_obj
        else:
            raise ValueError("Not a Skill Req")