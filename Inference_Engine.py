from expert_system_desgin import *

class Knowledge_Base:
    def __init__(self):
        self.facts=[]
        self.rules={}
        self.additional={}

    def add_fact(self,fact:str):
        if fact not in self.facts:
            self.facts.append(Fact(fact))

    def get_facts(self):
        fact_names=[]
        for fact in self.facts:
            fact_names.append(fact.name)
        return fact_names

    def clear_facts(self):
        self.facts.clear()

    def add_rule(self,name:str,rule:Rule):
        self.rules[name]=rule

    def add_additional(self,name:str,info:str):
        self.additional[name]=info

    def Forward_Chaining(self):
        results=[]
        go=1
        while go:
            satisfied=0
            for rule_name,rule in self.rules.items():
                if rule.check(self.facts) and rule_name not in self.get_facts():
                    self.add_fact(rule_name)
                    results.append(rule_name)
                    satisfied=1

            if satisfied==0:
                go=0
            
        return results

    def Backward_Chaining(self,goal):
        if goal in self.facts:
            return True
        elif isinstance(goal,Fact) and goal.name in self.rules:
            if self.Backward_Chaining(self.rules[goal.name]):
                self.add_fact(goal.name)
                return True

        if isinstance(goal,AndRule):
            return all(self.Backward_Chaining(fact) for fact in goal.children)
        if isinstance(goal,OrRule):
            return any(self.Backward_Chaining(fact) for fact in goal.children)
        if isinstance(goal,NotRule):
            return not any(self.Backward_Chaining(fact) for fact in goal.children)
                
        return False
