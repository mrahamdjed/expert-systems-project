from expert_system_desgin import *

class Knowledge_Base:
    def __init__(self):
        self.facts=[]
        self.rules={}
        self.additional={}

    def add_fact(self,fact:str):
        if fact not in self.facts:
            self.facts.append(Fact(fact))

    def clear_facts(self):
        self.facts.clear()

    def add_rule(self,name:str,rule:Rule):
        self.rules[name]=rule

    def add_additional(self,name:str,info:str):
        self.additional[name]=info

    def Forward_Chaining(self):
        for rule_name,rule in self.rules.items():
            if rule.check(self.facts):
                print(rule_name,":",self.additional[rule_name])
                self.add_fact(rule_name)

    def Backward_Chaining(self,goal):
        if goal in self.facts:
            return True
        elif isinstance(goal,Fact) and goal.name in self.rules:
            if self.Backward_Chaining(kb.rules[goal.name]):
                self.add_fact(goal.name)
                return True

        if isinstance(goal,AndRule):
            return all(self.Backward_Chaining(fact) for fact in goal.children)
        if isinstance(goal,OrRule):
            return any(self.Backward_Chaining(fact) for fact in goal.children)
        if isinstance(goal,NotRule):
            return not any(self.Backward_Chaining(fact) for fact in goal.children)
                
        return False

kb=Knowledge_Base()

kb.add_rule("cat",AndRule(children=[Fact("four_legs"),OrRule(children=[Fact("meows"),Fact("rectangle_claws")])]))
kb.add_additional("cat","Domesticated, known for hunting rodents")

kb.add_rule("persian_cat",AndRule(children=[Fact("cat"),Fact("long_fur"),Fact("small_size")]))
kb.add_additional("persian_cat","Domesticated, known for its elegent appearance")

kb.add_rule("bird",AndRule(children=[Fact("feathers"),Fact("can_fly")]))
kb.add_additional("bird","Lives in trees, lays eggs")

kb.add_rule("fish",AndRule(children=[Fact("gills"),Fact("swims")]))
kb.add_additional("fish","Lives in water, breathes underwater")

kb.add_rule("shark",AndRule(children=[Fact("fish"),Fact("sharp_teeth"),Fact("large_size")]))
kb.add_additional("shark","Carnivorous, apex predator in oceans")

kb.add_rule("white_shark",AndRule(children=[Fact("shark"),Fact("length_>_4")]))
kb.add_additional("white_shark","Found in open oceans, known feo its aggressive behavior")

kb.add_rule("elephant",AndRule(children=[Fact("large_size"),OrRule(children=[Fact("trunk"),Fact("tusks")])]))
kb.add_additional("elephant","Herbivorous, lives in savannas or forests")

kb.add_rule("lion",AndRule(children=[Fact("four_legs"),Fact("large_size"),Fact("mane"),Fact("roars")]))
kb.add_additional("lion","Carnivorous, apex predator, lives in savannas")

kb.add_rule("tiger",AndRule(children=[Fact("four_legs"),Fact("large_size"),Fact("triped_fur"),Fact("roars")]))
kb.add_additional("tiger","Carnivorous, lives in forests")

kb.add_rule("bengal_tiger",AndRule(children=[Fact("tiger"),Fact("orange_coat_with_black_stripes")]))
kb.add_additional("bengal_tiger","Carnivorous, live in Asian forests")

kb.add_rule("frog",AndRule(children=[Fact("amphibian"),Fact("jumps"),Fact("can_live_on_land")]))
kb.add_additional("frog","Amphibious, lives near water")

kb.add_rule("eagle",AndRule(children=[Fact("bird"),Fact("sharp_talons"),Fact("singspan_>_2")]))
kb.add_additional("eagle","Carnivorous, execellent vision")

kb.add_rule("kangaroo",AndRule(children=[Fact("jumps_high"),Fact("pouch_for_carrying_young")]))
kb.add_additional("kangaroo","Herbivorous, found in Australia")

kb.add_rule("horse",AndRule(children=[Fact("four_legs"),Fact("strong_build"),Fact("can_run_fast")]))
kb.add_additional("horse","Herbivorous, used for transport or sport")

kb.add_rule("bat",AndRule(children=[Fact("mammal"),Fact("wings"),Fact("nocturnal"),Fact("wingspan_<_0.5")]))
kb.add_additional("bat","Uses echolocation, active at night")

kb.add_rule("whale",AndRule(children=[Fact("mammal"),Fact("large_size"),Fact("breathes_air")]))
kb.add_additional("whale","Marine mammal, lives in oceans")

kb.add_rule("crocodile",AndRule(children=[Fact("scales"),Fact("sharp_teeth"),Fact("can_live_on_land"),Fact("swims")]))
kb.add_additional("crocodile","Carnivorous, found in rivers and wetlands")

kb.add_rule("wolf",AndRule(children=[Fact("four_legs"),Fact("howls"),Fact("lives_in_packs")]))
kb.add_additional("wolf","Carnivorous, found in forests and mountains")

kb.add_rule("dolphin",AndRule(children=[Fact("mammal"),Fact("intelligent"),Fact("number_of_clicks_>_10")]))
kb.add_additional("dolphin","Marine mammal, highly social")


kb.add_fact("four_legs")
kb.add_fact("meows")
kb.add_fact("rectangle_claws")
kb.add_fact("long_fur")
kb.add_fact("small_size")

kb.add_fact("gills")
kb.add_fact("swims")
kb.add_fact("sharp_teeth")
kb.add_fact("large_size")
kb.add_fact("length_>_4")

# kb.add_fact("mammal")
# kb.add_fact("intelligent")
# kb.add_fact("number_of_clicks_>_10")

# print("Forward Chaining infered rules based on provided facts : ")
# kb.Forward_Chaining()

print("Backward Chaining infered rules based on provided facts : ")
for name,rule in kb.rules.items():
    if kb.Backward_Chaining(rule):
        print(name,":",kb.additional[name])

# print("\nFacts :")
# for fact in kb.facts:
#     print(fact.name)