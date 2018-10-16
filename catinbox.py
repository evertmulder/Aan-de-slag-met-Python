from random import randrange, choice


class Cat:
    def __init__(self):
        self.box_index = None
        self.can_jump_from_first_to_last = True

    def jump_in_box(self, boxes):
        if self.box_index:
            boxes[self.box_index].remove_cat_from_box()

        self.box_index = randrange(len(boxes))
        boxes[self.box_index].put_cat_in_box()

    def move(self, boxes):
        boxes[self.box_index].remove_cat_from_box()
        new_index = self.box_index + choice([-1, 1])
        if self.can_jump_from_first_to_last:
            if new_index < 0:
                new_index = len(boxes) - 1
            elif new_index > len(boxes) - 1:
                new_index = 0
        else:
            if new_index < 0:
                new_index = 1
            elif new_index > len(boxes) - 1:
                new_index = len(boxes) - 1
        boxes[new_index].put_cat_in_box()
        self.box_index = new_index


class Box:
    def __init__(self, box_no):
        self._box_no = box_no
        self._has_cat = False

    def has_cat(self):
        return self._has_cat

    def put_cat_in_box(self):
        assert not self._has_cat
        self._has_cat = True

    def remove_cat_from_box(self):
        assert self._has_cat
        self._has_cat = False


class Simulation:
    def __init__(self, number_of_boxes, cat_can_jump_from_first_to_last):
        self._boxes = [Box(box_no) for box_no in range(number_of_boxes)]
        self._tries = 0
        self._cat_found = False
        self._cat = Cat()
        self._cat.can_jump_from_first_to_last = cat_can_jump_from_first_to_last
        self._cat.jump_in_box(self._boxes)

    def check_random_box(self):
        box_to_open = randrange(len(self._boxes))
        self.check_box(box_to_open)

    def check_box(self, box_number_to_open):
        self._tries = self._tries + 1
        if self._boxes[box_number_to_open].has_cat():
            self._cat_found = True
        else:
            self._cat.move(self._boxes)

    def run_until_cat_found(self):
        while not self._cat_found:
            self.check_random_box()

    def get_tries(self):
        return self._tries

    def __str__(self):
        return "# %i tries. Cat found: %s" % (self._tries, self._cat_found)


simulation_runs = 2000
no_boxes = 100
all_simulation_results = []

cat_can_jump_from_first_to_last = True

for i in range(simulation_runs):
    s = Simulation(no_boxes, cat_can_jump_from_first_to_last)
    s.run_until_cat_found()
    tries = s.get_tries()
    all_simulation_results.append(tries)
str()
average_tries = sum(all_simulation_results) / simulation_runs
print("Gemiddeld %i pogingen om de kat te vinden in %i dozen. Runs: %i. Min pogingen: %i. Max pogingen: %i" %
      (average_tries, no_boxes, simulation_runs, min(all_simulation_results), max(all_simulation_results)))
