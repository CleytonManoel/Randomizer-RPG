# Randomizer Rpg

## Summary

- Project
- Git clone
- Requirements
- How to use
- Custom libs
- More doubts

## Project

RandomizerRPG is a tool created to assist in the development of rpg games and to accelerate the development of programs that use table rpg mechanics.

## Git clone

```sh
git clone https://github.com/CleytonManoel/Randomizer-RPG.git
```

## Requirements

It is necessary for the execution of the program to have the random and json modules and some python version compatible with both.

## How to use

Import the functions to the file where they will be used, and then put the function you want to use, for example:

```py

import randomizerrpg


print(randomizerrpg.weapons.random_weapon())

```

Depending on your custom lib, the function return should be something like:

```
sword
```

Some functions may need additional data, for example:

```py
randomizerrpg.generatornpc.generator_npc(agetype, job, gender, breed)
```

Where your variables must be filled in according to the variables inside the JSON files present in the lib folder.

## Custom libs

To use custom libs, just place the custom JSON files inside the "lib" folder, following the existing standards.

## More doubts

For more questions about the project, consult the official documentation:

> documentação oficial https://randomizerrpgdocs.netlify.app
