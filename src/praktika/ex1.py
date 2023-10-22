class Tomato:

    states = ["нету", "цветение", "зеленый", "красный"]
    state_index = 0

    def __init__(self, index):
        """
        make dynamic properties:
        _index: int
        _state: str
        """
        self._index = index
        self._state = self.states[self.state_index]

    def grow(self):
        """
        change state of tomato
        """
        self.state_index += 1
        self._state = self.states[self.state_index]
    
    def is_ripe(self):
        """
        return True if tomato state is last state
        """
        return self._state == self.states[-1]

class TomatoBush:

    def __init__(self, number_of_tomatoes):
        """
        make tomato bush by specifying amount of tomatoes on bush
        """
        self.tomatoes = [Tomato(i) for i in range(number_of_tomatoes)]

    def grow_all(self):
        """
        change state of all tomatoes on bush
        """
        for i in self.tomatoes:
            i.grow()

    
    def all_are_ripe(self):
        """
        return true if bush is ready to harvest
        """
        return self.tomatoes[0].is_ripe()


    def give_away_all(self):
        """
        return tomatoes and delete them from class
        """
        tomatoes = self.tomatoes
        del self.tomatoes
        return tomatoes

class Gardener:

    plant_harvested = 0

    def __init__(self, name, plant: TomatoBush):
        """
        make gardener with name and given tomato bush
        """
        self.name = name
        self._plant = plant

    def work(self):
        """
        make bush growing
        """
        print("working....")
        self._plant.grow_all()

    
    def harvest(self):
        """
        if plant ready to harvest, make harvest and return tomatoes
        """

        if self._plant.all_are_ripe():
            print("harvesting")
            self.plant_harvested += 1
            return self._plant.give_away_all()
        print("plant not ready yet")
    
    def knowledge_base(self):
        """
        print info about gardener
        """
        print(f"\ngardener name: {self.name}\nharvested: {self.plant_harvested}")
    
tomato_bush = TomatoBush(10)

gardener = Gardener("bob", tomato_bush)

gardener.knowledge_base()

gardener.work()

gardener.harvest()

gardener.work()

gardener.work()

tomatoes = gardener.harvest()

print(tomatoes[1]._index)

gardener.knowledge_base()