import random
class Entity:
  def __init__(self, attack, defense, hitpoints):
    self.attack=attack
    self.defense=defense
    self.hitpoints=hitpoints
  def attacks(self, oponent):
    oponent.hitpoints-=(self.attack-oponent.defense)
  def heal(self):
    self.hitpoints+=self.defense
  def isDead(self):
    if self.hitpoints>0:
      return False
    else:
      return True
  def block(self, opponent):
    self.hitpoints-=(opponent.attack-self.defense)
hero = Entity(10,5,40)
enemy = Entity(10,5,40)
def battle1(entity1, entity2):
  i=1
  while (True):
    print(i)
    print("Hero Hitpoints: ", entity1.hitpoints)
    print("Enemy Hitpoints: ", entity2.hitpoints)
    entity1.attacks(entity2)
    if entity2.isDead():
      return True
    entity2.attacks(entity1)
    if entity1.isDead():
      return False
    i+=1
def battle2(entity1, entity2):
  i=1
  while (True):
    print(i)
    print("Hero Hitpoints: ", entity1.hitpoints)
    print("Enemy Hitpoints: ", entity2.hitpoints)
    if random.uniform(0,1)<0.5:
      entity1.attacks(entity2)
      if entity2.isDead():
        return True
    else:
      entity1.heal()
    if random.uniform(0,1)>0.5:
      entity2.attacks(entity1)
      if entity1.isDead():
        return True
    else:
      entity2.heal()
    i+=1
def fight(entity1, entity2):
  if entity1.hitpoints<=(entity2.attack-entity1.defense):
    if entity2.hitpoints<=(entity1.attack-entity2.defense):
      entity1.attacks(entity2)
    else:
      entity1.heal()
  else:
    entity1.attacks(entity2)
print(fight(hero, enemy))
