import tkinter as tk
import tkinter.messagebox as messagebox
from Inference_Engine import Knowledge_Base
from expert_system_desgin import *

class AnimalIdentification:
    def __init__(self, master, knowledge_base,Facts):
        self.master = master
        self.knowledge_base = knowledge_base
        
        self.master.title("ANIMAL DETECTION")
        self.master.minsize(width=1000, height=500)
        self.master.maxsize(width=1000, height=500)

        self.fr1 = tk.Frame(self.master, width=1000, height=1000, bg="#2d3250")
        self.fr1.place(x=1, y=1)

        self.lb = tk.Label(self.fr1, text="Animals Recognition System", fg="#fff", bg="#2d3250", font=("Arial", 20))
        self.lb.place(x=50, y=10)

        self.submitBtn1 = tk.Button(self.fr1, text="  Generate Animal (Forward)  ", font=("Arial", 12), fg="#2d3250", bg="#fcb17a", cursor="hand2",command=self.generate_animalsForward)
        self.submitBtn1.place(x=20, y=450)
        
        self.submitBtn2 = tk.Button(self.fr1, text="Generate Animal (Backward)", font=("Arial", 12), fg="#2d3250", bg="#fcb17a", cursor="hand2",command=self.generate_animalsBackward)
        self.submitBtn2.place(x=300, y=450)

        self.resetBtn = tk.Button(self.fr1, text="Reset", font=("Arial", 12), fg="#2d3250", bg="#fcb17a", cursor="hand2", command=self.printing)
        self.resetBtn.place(x=600, y=450)

        self.facts = Facts
        self.rules = self.knowledge_base.rules
        self.facts_vars = {fact.name: tk.BooleanVar() for fact in self.facts}

        self.create_checkboxes()

        self.result_label = tk.Label(self.fr1,text="",fg="#fff",bg="#2d3250",font=("Arial", 14),wraplength=450,justify="left")
        self.result_label.place(x=20, y=300)

    def printing(self):
        for rule in self.facts :
            print(rule)
        
    def create_checkboxes(self):
        row = 50
        for index, fact in enumerate(self.facts):
            if fact.name in ("cat","fish","shark") :
                continue
            else :
                column = index % 3
                row = index // 3
                var = tk.BooleanVar()
                checkbox = tk.Checkbutton(self.fr1, text=fact.name, variable=var, fg="#fff", bg="#2d3250", activebackground="#2d3250", activeforeground="#fff", selectcolor="#2d3250", font=("Arial", 12))
                checkbox.place(x=20 + (column * 300), y=60 + (row * 30))
                self.facts_vars[fact.name] = var

    def generate_animalsForward(self):
        
        self.knowledge_base.clear_facts()

        for fact_name, var in self.facts_vars.items():
            if var.get():
                self.knowledge_base.add_fact(fact_name)

        self.knowledge_base.Forward_Chaining()

        results = [
            f"{rule_name}: {self.knowledge_base.additional[rule_name]}"
            for rule_name in self.knowledge_base.rules.keys()
            if rule_name in [fact.name for fact in self.knowledge_base.facts]
        ]

        if results:messagebox.showinfo("Inferred Animals", "\n".join(results))
        else:
            messagebox.showerror("No Animal Found", "No animal corresponds to the selected facts.")

    def generate_animalsBackward(self):
        self.knowledge_base.clear_facts()
        for fact_name, var in self.facts_vars.items():
            if var.get():
                self.knowledge_base.add_fact(fact_name)
    
        results = []
    
        for rule_name, rule in self.rules.items():
            if self.knowledge_base.Backward_Chaining(rule):
                results.append(f"{rule_name}: {self.knowledge_base.additional[rule_name]}")
    
        if results:
            messagebox.showinfo("Inferred Animals", "\n".join(results))
        else:
            messagebox.showerror("No Animal Found", "No animal corresponds to the selected facts.")



    def reset(self):
        for var in self.facts_vars.values():
            var.set(False)


kb = Knowledge_Base()

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

kb.add_rule("tiger",AndRule(children=[Fact("four_legs"),Fact("large_size"),Fact("striped_fur"),Fact("roars")]))
kb.add_additional("tiger","Carnivorous, lives in forests")

kb.add_rule("bengal_tiger",AndRule(children=[Fact("tiger"),Fact("orange_coat_with_black_stripes")]))
kb.add_additional("bengal_tiger","Carnivorous, live in Asian forests")

kb.add_rule("frog",AndRule(children=[Fact("amphibian"),Fact("jumps"),Fact("can_live_on_land")]))
kb.add_additional("frog","Amphibious, lives near water")

kb.add_rule("eagle",AndRule(children=[Fact("bird"),Fact("sharp_talons"),Fact("wingspan_>_2")]))
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

Facts=[Fact("four_legs"),Fact("meows"),Fact("rectangle_claws"),Fact("long_fur"),Fact("small_size"),
       Fact("feathers"),Fact("can_fly"),Fact("gills"),Fact("swims"),Fact("sharp_teeth"),Fact("large_size"),
       Fact("length_>_4"),Fact("trunk"),Fact("tusks"),Fact("mane"),Fact("roars"),Fact("striped_fur"),
       Fact("orange_coat_with_black_stripes"),Fact("amphibian"),Fact("jumps"),Fact("can_live_on_land"),
       Fact("sharp_talons"),Fact("wingspan_>_2"),Fact("jumps_high"),Fact("pouch_for_carrying_young"),
       Fact("strong_build"),Fact("can_run_fast"),Fact("wings"),Fact("nocturnal"),Fact("wingspan_<_0.5"),
       Fact("breathes_air"),Fact("scales"),Fact("howls"),Fact("lives_in_packs"),
       Fact("intelligent"),Fact("number_of_clicks_>_10")]

root = tk.Tk()
AnimalIdentification(root, kb, Facts)
root.mainloop()