#!/usr/bin/env python3
# -*- coding: iso-8859-15 -*-

import numpy as np


def normalize(v):
    L = np.linalg.norm(v)
    if L != 0:
        return v/L
    else:
        return np.zeros(2)

def scale(v, n):
    return n * normalize(v)

def look_at(v1, v2):
    return v2-v1


class Spring:
    def __init__(self, obj1, obj2, L0=1, k=1):
        self.obj1 = obj1
        self.obj2 = obj2
        self.L0 = L0
        self.k = k
        self.F1 = np.zeros(2)
        self.F2 = np.zeros(2)

    def forces(self):
        L = abs(self.obj1.pos - self.obj2.pos)
        dx = L - self.L0
        F = -self.k * dx
        F1 = scale(look_at(self.obj1.pos, self.obj2.pos), F)
        F2 = -self.F1
        return F1, F2


class Object:
    def __init__(self, pos=np.zeros(2), vel=np.zeros(2), mass=1, mu=1):
        self.pos = pos
        self.vel = vel
        self.mass = mass
        self.m_ = 1./mass
        self.reset_forces()
        self.F = np.zeros(2)
        self.mu = mu

    def reset_forces(self):
        self.forces = np.zeros(2)

    def add_force(self, F):
        self.forces = np.vstack((self.forces, F))

    def sum_forces(self):
        return np.sum(self.forces, axis=0)

    def move(self, dt=0.01):
        Fd = -scale(self.vel, self.vel**2) * self.mu
        self.add_force(Fd)
        F = self.sum_forces()
        a = F*self.m_
        # Not the best integrator...
        self.vel = self.vel + a*dt
        self.pos = self.pos + self.vel*dt
        # Reset forces
        self.reset_forces()
