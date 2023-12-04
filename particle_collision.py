import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def balls_collided(ball1_x, ball2_x):
  return abs(ball1_x-ball2_x) <= 0.3

def box_collision(ball_x, box_size):
  return not (0.2 <= ball_x <= box_size-0.2)

def simulate_collision(initial_pos1, initial_pos2,\
                      initial_velocity1, initial_velocity2,\
                      mass1, mass2, num_frames, box_size):
  ball1_x = [initial_pos1]
  ball2_x = [initial_pos2]
  v1 = initial_velocity1
  v2 = initial_velocity2
  m1 = mass1
  m2 = mass2
  total_mass = mass1 + mass2
  num_collisions = 0
  

  for i in range(num_frames):
    if balls_collided(ball1_x[-1], ball2_x[-1]):
      v1, v2 = ((m1-m2)*v1/total_mass)+(2*m2*v2/total_mass), ((m2-m1)*v2/total_mass)+(2*m1*v1/total_mass)
      num_collisions += 1
    if box_collision(ball1_x[-1], box_size):
      v1 *= -1
      num_collisions += 1
    if box_collision(ball2_x[-1], box_size):
      v2 *= -1
      if ball2_x[-1] > box_size:
        break
    
    ball1_x.append(ball1_x[-1]+v1)
    ball2_x.append(ball2_x[-1]+v2)

    print(num_collisions)


  return create_animation(ball1_x, ball2_x, box_size)


def create_animation(positions1, positions2, box_size):
  num_frames = len(positions1)

  fig, ax = plt.subplots()
  ax.set_xlim(0, box_size)
  ax.set_ylim(-0.1, 0.1)

  ball1 , = ax.plot(positions1[0], 0, 'bo', markersize=10)
  ball2 , = ax.plot(positions2[0], 0, 'ro', markersize=10)

  def update(frame):
    ball1.set_xdata(positions1[frame])
    ball2.set_xdata(positions2[frame])
    return ball1, ball2
  
  ani = FuncAnimation(fig, update, frames=num_frames, blit=True)
  plt.show()

  plt.close(fig)

initial_pos1 = 1
initial_pos2 = 10
initial_velocity1 = 0.1
initial_velocity2 = -0.1
mass1 = 0.1
mass2 = 10.0
num_frames = 200
box_size = 20

simulate_collision(initial_pos1, initial_pos2, initial_velocity1, initial_velocity2, mass1, mass2, num_frames, box_size)