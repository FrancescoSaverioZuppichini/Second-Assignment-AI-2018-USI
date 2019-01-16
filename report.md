# Artificial Intelligence 2018/2019
## Second Homework: Causal Inference

My model represents weightlifting. The variables are, in order of appearence from left to right:

- `age`. The age of the athleat
- `weight`
- `diet`. Represent what the athleat eats. It's outcome is `1`, athleat eats around 200~400 kcal more that its baseline, or `0`, less that its baseline.
- `sleep`. How much the athleat sleeps. We assume that sleep time begin around 23:00 ~ 00:00. The outcome is `1` if the athleat sleeps more that `7.5` hourse, `0` otherwise.
- `rest`. The hours between two workouts. `1` if more than 36 hours, `0` otherwise.
- `sex`. `1` is male, `0` is female.
- `body fat`. `1` if more than 20%, `0` if less.
- `hormone production`. `1` is hormone production is under average, `0` if more. Hormones such as `gh` and `testosterone` are essetianl to better gains.
- `gains`. Measured in grams of muscle per month. `1` if more than 400g, `0` otherwise.
- `1RM_increase`. In % how much we increase the one range of motion every month on the base exercises: `deadlift`, `squat` and `bench press`. `1` if 5% more than last month, `0` otherwise.

It follows an explanation of the arcs in the graph. `body fat` depends by the weight, the diet, booth depend of the `age`, and the gains. The more you gain the more you weight.

`gains` is the most important node. It depends by `weight`, `diet`, `sleep`, `rest` and `hormone production`. The late, directly depend on `sex`, `sleep` and `diet`. 

`1RM increase` depends on the `gains`.


#### State which is the objective of the network: for instance, highlight a couple of situations in which decision making could be difficult and in which the graph could provide valuable indications.

Probably a mix of situations for `gains`. For instance, if the athleat sleeps more than 7.5 hours, eat enought but does not rest more than 36 hours. An other could be where the diet prevents a correct hormones production but the athleat trains, sleep and rest well.

#### Explaining how you decide the arcs orientation, in case they are not self- explaining.

They are all streigthforward.

#### Which arrows can be reversed without being detectable by a statistical test? Explain why.

The following set of edges can be reversed without being detectable by a statistical test.
$(e(age, weight), e(age, diet), e(gains, 1RM increase))$ 

#### Identify at least 4 couple of nodes (the node of each couple should be not directly linked to each other) and analyze their d-separation properties possibly conditioning on others.

The nodes graphs are denominated using letters by following the alphabet from left to right from top to bottom. It should be easy to the reader to remap them.

1. (`age`, `body_fat`)
There are five paths: $\{A,B,G\}, \{A,C,G\}, \{A,C,H,G\}  \{A,B,H,G\},  \{A,C,I,H,G\}$

They are all chains, thus we can block them by conditioning on $\{B,C\}$

2. (`age`, `gains`)
There are five paths: $\{A,B,H\}, \{A, B, G, H\}, \{A,C, H\}  \{A,C,G,H\},  \{A,C,I,H\}$

In the second path, $G$ is a collider for $B, H$. We can condition on $B, C$. $B$ will prevent the paths $\{A,B,H\},  \{A, B, G, H\}$. $C$ will prevent the paths $\{A,C, H\} \{A,C,G,H\},  \{A,C,I,H\}$.

3. (`age`, `hormones production`)
There are five paths: $\{A,C,I\}, \{A, C, H, I\},  \{A,B ,G, H, I\},  \{A, B, H, I\}, \{ A,B,G,C,H,I\}$. We just need to condition on $C$ to block the chain $\{ A, C, I\}$ since $G$ is a collider for $B$ and $H$ while $H$ is a collider for $B$ and $I$ so they are already blocked.

4. (`diet`, `sleep`)
There are five paths: $\{C, H, D \}, \{ C,G,H,D\}, \{C, H, I, D\}$.
All those paths are already blocked by $H$ that is a collider


#### Discuss how d-connected variables are in fact dependent in the real problem, while d-separated variables are instead independent in the real problem.

