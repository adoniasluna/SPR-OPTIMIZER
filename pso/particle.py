import random


class Particle:
    def __init__(self, dimensions):
        self.dimensions = dimensions
        self.position = []  # particle position
        self.velocity = []  # particle velocity
        self.pos_best = []  # best position individual
        self.err_best = -1  # best error individual
        self.err = -1  # error individual

        global num_dimensions
        # num_dimensions = len(x0)
        num_dimensions = len(self.dimensions)

        for i in range(0, num_dimensions):
            self.velocity.append(random.uniform(-1, 1))
            self.position.append(random.uniform(min(self.dimensions[i]),
                                                max(self.dimensions[i])))
            # self.position.append(x0[i])

    # evaluate current fitness
    def evaluate(self, func_fitness):
        self.err = func_fitness(self.position)

        # check to see if the current position is an individual best
        if self.err < self.err_best or self.err_best == -1:
            self.pos_best = self.position
            self.err_best = self.err

    # update new particle velocity - inertia192.168.99.100
    def update_velocity_intertia(self, pos_best_g):
        w = 0.5  # constant inertia weight (how much to weigh the previous velocity)
        c1 = 2.04  # cognative constant
        c2 = 2.04  # social constant

        for i in range(0, num_dimensions):
            r1 = random.random()
            r2 = random.random()

            vel_cognitive = c1 * r1 * (self.pos_best[i] - self.position[i])
            vel_social = c2 * r2 * (pos_best_g[i] - self.position[i])
            self.velocity[i] = w * self.velocity[i] + vel_cognitive + vel_social

    # update new particle velocity - clerc
    def update_velocity_clerc(self, pos_best_g):
        c_fac = 0.7298

        for i in range(0, num_dimensions):
            r1 = random.random()
            r2 = random.random()

            vel = c_fac * (
                    (self.velocity[i] + r1) * (self.pos_best[i] - self.position[i]) + (
                        r2 * (pos_best_g[i] - self.position[i])))
            self.velocity[i] = vel

    # update the particle position based off new velocity updates
    def update_position(self):
        for i in range(0, num_dimensions):
            self.position[i] = self.position[i] + self.velocity[i]

            # adjust maximum position if necessary
            if self.position[i] > max(self.dimensions[i]):
                self.position[i] = max(self.dimensions[i])

            # adjust minimum position if neseccary
            if self.position[i] < min(self.dimensions[i]):
                self.position[i] = min(self.dimensions[i])

    def get_position(self):
        return self.position
