import random
from random import uniform
import matplotlib.pyplot as plt

class Particle:
  def __init__(self, position) -> None:
    self.positions = [position]
  
  def update_positions(self, inc) -> None:
    self.positions.append(self.positions[-1]+inc)

def new_Part(pos:float|int) -> Particle:
  return Particle(pos)

def random_walk(num_steps:int, prob_right:float, num_particles:int):
  
  particles = [new_Part(0) for i in range(num_particles)]

  for i in range(num_steps):
    for particle in particles:
      if uniform(0,1) <= prob_right:
        particle.update_positions(uniform(0, 5))
      else: particle.update_positions(uniform(-5, 0))

  particle_paths = [p.positions for p in particles]

  create_plot(num_steps, particle_paths)

  return particle_paths

def create_plot(num_steps, particle_paths):

  time = [x for x in range(len(particle_paths[0]))]

  for particle_path in particle_paths:
    plt.plot(particle_path, time)

  plt.title('Random Walk - N particles')
  plt.xlabel('Position')
  plt.ylabel('Time')
  plt.show()

num_steps = 100
prob_right = 0.8
num_particles = 200

random_walk(num_steps, prob_right, num_particles)