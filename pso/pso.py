from __future__ import division
import time
from pso.particle import Particle


class PSO:
    def __init__(self, func_fitness, dimensions, num_particles, max_iterations, inertia_weight, cognitive_constant,
                 social_constant):
        self.convergence_time = -1
        self.best_position = []
        self.best_error = -1
        self.error_history = []
        self.dimensions = dimensions
        self.num_particles = num_particles
        self.max_iterations = max_iterations
        self.particle_positions = []
        self.best_position_history = []

        err_best_g = -1  # best error for group
        pos_best_g = []  # best position for group
        err_best_g_list = []

        start_time = time.time()

        for i in range(self.max_iterations):
            self.particle_positions.append([])

        # establish the swarm
        swarm = []
        for i in range(0, num_particles):
            swarm.append(Particle(self.dimensions, inertia_weight, cognitive_constant, social_constant))

        # begin optimization loop
        i = 0
        while i < self.max_iterations:
            # cycle through particles in swarm and evaluate fitness
            for j in range(0, self.num_particles):
                swarm[j].evaluate(func_fitness)

                # determine if current particle is the best (globally)
                if swarm[j].err < err_best_g or err_best_g == -1:
                    pos_best_g = list(swarm[j].position)
                    err_best_g = float(swarm[j].err)

            # Saving the best error values
            err_best_g_list.append(err_best_g)
            self.error_history.append(err_best_g)

            # cycle through swarm and update velocities and position
            for j in range(0, self.num_particles):
                x, y, z = swarm[j].position
                self.particle_positions[i].append([x, y, z])
                # swarm[j].update_velocity_intertia(pos_best_g)
                swarm[j].update_velocity_clerc(pos_best_g)
                swarm[j].update_position()
            i += 1
            a, b, c = pos_best_g
            self.best_position_history.append([a, b, c])

        self.convergence_time = time.time() - start_time
        self.best_error = err_best_g

        # update final results squared_error
        self.best_position = pos_best_g
