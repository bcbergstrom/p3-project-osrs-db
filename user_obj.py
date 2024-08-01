from requirements import SkillRequirements
class User:
    def __init__(self, name, reqs):
        self.name = name
        self.reqs = reqs
    
    @property
    def name(self):
        return self._name 
        
    @name.setter
    def name(self,value):
        if type(value) is str:
            self._name = value
        else:
            raise ValueError("Wrong Type")

    @property
    def reqs(self):
        return self._reqs 
        
    @reqs.setter
    def reqs(self,value):
        if type(value) is SkillRequirements:
            self._reqs = value
        else:
            raise ValueError("Wrong Type")