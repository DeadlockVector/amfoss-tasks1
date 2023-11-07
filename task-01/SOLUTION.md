# Terminal Hunt

## Set-up

I cloned the repo with ```git clone https://github.com/KshitijThareja/TerminalWizard.git```

Creating the "codes" directory : ```cd TerminalWizard``` and ```mkdir codes```

Making the text files: ```touch Part_1``` (repeat for each of the other 3 parts)

## Part 1:

To move to the directory: ```cd 06```

To get the spell: ```cat Spell_05```

To navigate to the spellbook: ```cd ..``` and ```cd spellbook```

To execute the python file with the spell name: ```python3 Impedimenta.py```

To add the code to the codes/Part_1.txt file: ```cd ..``` > ```cd codes``` > ```echo "<code>" >> Part_1```

## Part 2:

To move to the directory: ```cd 02```

To get the spell: ```cat Spell_03```

To navigate to the spellbook: ```cd ..``` and ```cd spellbook```

To execute the python file with the spell name: ```python3 <python file with spell name>```

To add the code to the codes/Part_2.txt file: ```cd ..``` > ```cd codes``` > ```echo "<code>" >> Part_2```

## Part 3:

To move to the branch: ```git checkout defenseAgaisntTheDarkArts```

To navigate to the spellbook: ```cd ..``` and ```cd spellbook```

To execute the python file with the spell name: ```python3 Riddikulus.py```

To add the code to the codes/Part_3.txt file: ```cd ..``` > ```cd codes``` > ```echo "<code>" >> Part_3```

To copy the Riddikulus.py to the spellbook of the main branch: ```git checkout main``` > ```git checkout defenseAgainstTheDarkArts ../spellbook/Riddikulus.py```

## Part 4:

To get the commit logs: ```git log```

To switch to theGraveyard: ```git checkout theGraveyard```

To switch back to main : ```git checkout main```

To add the code to the codes/Part_4.txt file: ```cd ..``` > ```cd codes``` > ```echo "<code>" >> Part_4```

## Final Code:

Switch to the codes directory: ```cd codes```

Create finalcode.txt: ```touch finalcode```

Concatenate each of the spells: ```cat Part_1 Part_2 Part_3 Part_4 >> finalcode ```

Removing the files: ```rm Part_1``` (Remove each file similarly)

## After decoding: 

After cloning the decoded repo link: ```cd TheFinalSpell```

Then: cat TheOneThatEndsItAll

## To move codes file to main repository:
```cp -r /home/isocyanate/Documents/amfoss-reference/TerminalWizard/codes /home/isocyanate/Documents/amfoss-tasks1/task-01/```


