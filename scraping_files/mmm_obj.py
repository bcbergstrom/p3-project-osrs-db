from requirements import SkillRequirements
class MMM_Obj:
    def __init__(self, method, profit, reqs=None):
        self._methods = method
        self._profit = profit
        self._reqs = reqs
    
    @property
    def reqs(self):
        return self._reqs
    
    @reqs.setter
    def reqs(self, reqs_obj):
        if reqs_obj is SkillRequirements:
            self._reqs = reqs_obj
        else:
            raise ValueError("Not a Skill Req")