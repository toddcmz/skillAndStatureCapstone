class Gambit_Template():

    def __init__(self, options=1, free = False, title="", flavor = "", prereq = None, effects={}):
        self.options = options
        self.free = free
        self.title = title
        self.flavor = flavor
        self.prereq = prereq
        self.effects = effects

    def play_this_gambit(self):
        # do prereq check
        if self.prereq:
            passed_prereq = self.meet_prereq()
            if passed_prereq == False:
                return() # TLC - I'm not sure the correct way to interrupt flow here if the prereq isn't met - where do we go if prereq isn't met? Somewhere in the driver once that's set up?
        # check if there's more than one effect, if so, choose one, else it's the default effect
        if len(self.effects == 2):
            which_effect = input("choose 1 or 2") # TLC - Change this input to pull in and print both effects.
        else:
            which_effect = "1"
        
        # confirm playing gambit
        user_choice = input("Confirm playing/choice?(y/n)").lower()
        if user_choice == "y":
            self.activate_effect(which_effect)

        print(f'Playing gambit: {self.title}')


class Forged_Letter_Gambit(Gambit_Template):

    def __init__(self, options=2, free = False, title="Forged Letter from Spouse", flavor="Save the farm!", prereq = None, 
    effects={"Effect 1" : "Swap a worker with an opponent's worker up to two times", 
             "Effect 2" : "Move a worker to any location"}):
        super().__init__(options, free, title, flavor, prereq, effects)

    def meet_prereq(self):
        pass

    def activate_effect(self, which_effect):
        if which_effect == "1":
            self.dedicated_effect_swap_workers()
        else:
            self.dedicated_effect_move_worker()

    def dedicated_effect_swap_workers(self):
        pass

    def dedicated_effect_move_worker(self):
        pass

class Preferred_Contract_Gambit(Gambit_Template):

    def __init__(self, options=1, free = False, title="Preferred Contract", flavor="Early access", prereq = None, 
    effects={"Effect" : "The top 2 commissions of the draw pile are available for you to work this turn"}):
        super().__init__(options, free, title, flavor, prereq, effects)

    def meet_prereq(self):
        pass

    def activate_effect(self, which_effect):
        self.dedicated_effect_extra_commissions()

    def dedicated_effect_extra_commissions(self):
        pass

class Thin_Soled_Shoes_Gambit(Gambit_Template):

    def __init__(self, options=2, free = False, title="Forged Letter from Spouse", flavor="Save the farm!", prereq = "Spend 5 travel points", 
    effects={"Effect 1" : "Swap a worker with an opponent's worker up to two times", 
             "Effect 2" : "Move a worker to any location"}):
        super().__init__(options, free, title, flavor, prereq, effects)

    def meet_prereq(self):
        pass

    def activate_effect(self, which_effect):
        if which_effect == "1":
            self.dedicated_effect_stature()
        else:
            self.dedicated_effect_repeat_action()

    def dedicated_effect_stature(self):
        pass

    def dedicated_effect_repeat_action(self):
        pass

class Dowsing_Rod_Gambit(Gambit_Template):

    def __init__(self, options=1, free = True, title="Dowsing Rod", flavor="How'd these get here?", prereq = "Roll a die", 
    effects={"Effect" : "3-6: Gain 2 raw resources | 1-2: It's just a stick"}):
        super().__init__(options, free, title, flavor, prereq, effects)

    def meet_prereq(self):
        pass

    def activate_effect(self, which_effect):
        self.dedicated_effect_roll()

    def dedicated_effect_roll(self):
        pass

class Spoiled_Fish_Gambit(Gambit_Template):

    def __init__(self, options=1, free = True, title="Spoiled Fish", flavor="Give a man a fish", prereq = None, 
    effects={"Effect" : "Give an opponent up to 2 resources and take an equal number of raw resources from them"}):
        super().__init__(options, free, title, flavor, prereq, effects)

    def meet_prereq(self):
        pass

    def activate_effect(self, which_effect):
        self.dedicated_effect_forced_trade()

    def dedicated_effect_forced_trade(self):
        pass

class Proprietary_Maps_Gambit(Gambit_Template):

    def __init__(self, options=2, free = False, title="Proprietary Maps", flavor="Found a shortcut", prereq = None, 
    effects={"Effect 1" : "+7 travel points",
             "Effect 2" : "Swap 2 site disks, excluding opponents' villages. Pieces move with the site."}):
        super().__init__(options, free, title, flavor, prereq, effects)

    def meet_prereq(self):
        pass

    def activate_effect(self, which_effect):
        if which_effect == "1":
            self.dedicated_effect_travel_points()
        else:
            self.dedicated_effect_swap_sites()

    def dedicated_effect_travel_points(self):
        pass

    def dedicated_effect_swap_sites(Self):
        pass

class Paid_Vacation_Gambit(Gambit_Template):

    def __init__(self, options=2, free = False, title="Paid Vacation", flavor="Well deserved rest", prereq = None, 
    effects={"Effect 1" : "Travel after refinement",
             "Effect 2" : "Move one of your artisans to any non-guild site"}):
        super().__init__(options, free, title, flavor, prereq, effects)

    def meet_prereq(self):
        pass

    def activate_effect(self, which_effect):
        if which_effect == "1":
            self.dedicated_effect_refine_travel()
        else:
            self.dedicated_effect_move_artisan()

    def dedicated_effect_refine_travel(self):
        pass

    def dedicated_effect_move_artisan(Self):
        pass

class Burlap_Sacks_Gambit(Gambit_Template):

    def __init__(self, options=2, free = False, title="Burlap Sacks", flavor="This is salvageable", prereq = None, 
    effects={"Effect 1" : "When spending resources, return up to 2 raw of that type to your refinery",
             "Effect 2" : "When an opponent spends resources, take 1 raw of any of the types spent"}):
        super().__init__(options, free, title, flavor, prereq, effects)

    def meet_prereq(self):
        pass

    def activate_effect(self, which_effect):
        if which_effect == "1":
            self.dedicated_effect_recover_mine()
        else:
            self.dedicated_effect_recover_yours()

    def dedicated_effect_recover_mine(self):
        pass

    def dedicated_effect_recover_yours(Self):
        pass

class Coffee_Gambit(Gambit_Template):

    def __init__(self, options=1, free = False, title="Coffee", flavor="Do everything", prereq = "Return 1 stature", 
    effects={"Effect" : "Use a 4th action"}):
        super().__init__(options, free, title, flavor, prereq, effects)

    def meet_prereq(self):
        pass

    def activate_effect(self, which_effect):
        self.dedicated_effect_roll()

    def dedicated_effect_roll(self):
        pass


