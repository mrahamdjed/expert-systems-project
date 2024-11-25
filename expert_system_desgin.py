from abc import ABC, abstractmethod

class Fact:
    def __init__(self, name:str):
        super().__init__()
        self.name = name.lower()
    
    def __eq__(self, other):
        if isinstance(other, Fact):
            return self.name == other.name
        return False
    def __hash__(self):
        return hash((self.name))


class Rule(ABC):
    def __init__(self, children:list):
        self.children = children
        super().__init__()

    @abstractmethod
    def check(self, inputFacts:list) -> bool :
        pass
    
    def getChildren(self) :
        temp = []
        for i in self.children :
            if isinstance(i, Fact) :
                temp.append(i)
            elif isinstance(i, Rule) :
                temp.append(i.getChildren())
        return temp

class OrRule(Rule):
    def check(self, inputFacts:list) -> bool:
        for i in self.children :
            if isinstance(i, Fact) :
                # print(f" [[ OrRule :  {i.name}]] ")
                if i in inputFacts : return True
            elif isinstance(i, Rule) :
                # print(f" [[ OrRule :  {i.children}]] ")
                if i.check(inputFacts) : return True
        return False

class AndRule(Rule):
    def check(self, inputFacts:list) -> bool:
        for i in self.children :
            if isinstance(i, Fact) :
                # print(f" [[ AndRule :  {i.name}]] ")
                if not(i in inputFacts) : return False
            elif isinstance(i, Rule) :
                # print(f" [[ AndRule :  {i.children}]] ")
                if not(i.check(inputFacts)) : return False
        return True

class NotRule(Rule):
    def check(self, inputFacts:list) -> bool:
        for i in self.children :
            if isinstance(i, Fact) :
                if i in inputFacts : return False
            elif isinstance(i, Rule) :
                if i.check(inputFacts) : return False
        return True
    

class Animal :
    def __init__(self, name:str, rule:Rule):
        self.name = name.lower()
        self.rule = rule
        self.facts = self.rule.getChildren()    

    def __eq__(self, other):
        if isinstance(other, Fact):
            return self.name == other.name
        return False
    def __hash__(self):
        return hash((self.name))
