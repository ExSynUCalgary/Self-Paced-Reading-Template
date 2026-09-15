# Self-Paced-Reading-Template

PsyEXP file created in PsychoPy version 2024.1.5

Current version runs online through Pavlovia on Google Chrome.

The SPR PsyEXP file is designed to present single word SPR experiments using the output of the SPR_Gen.py script as the stimuli file. This Readme file will contain explanations and instructions for the SPR PsyEXP file customization. For information about customizing the SPR_Gen.py script, please refer to the code comments.

## Intro Routine:

The Into_Text and Intro_key components are placeholders.

The Initialization code block does two important things. First, it initializes the 'r_num' variable at the beginning of the experiment. This is done through the code block to ensure compatibility with both local PsychoPy experiments and online experiments run on Pavlovia. In the 'Begin Routine' tab, the code will combine the character "r" with the number 'r_num'. This is directly tied to the Stimuli file column names. The output of this initialization code will be "r0", the first column of the SPR regions.

## Item_Loop:

This outer loop is where the Stimuli.csv is called. The conditions and parameters detected here can be used in the inner loop. By default, it is set to go through Stimuli.csv one time in sequential order.

## SPR_Loop:

This loop will handle the moving window portion of the experiment. No Conditions parameter is necessary for this loop as it will make use of the conditions and parameters from Item_Loop.

The Num. repeats box is set to Region_Num -- This calls the column of the same name from Stimuli.csv which is equal to the number of regions (words) in the corresponding sentence + 1 to account for region 0. This allows the experiment to handle sentences of different lengths by changing the number of times it will repeat.

## SPR Routine:

The Window_Text component will evaluate the current Region variable and display the text from the corresponding column of Stimuli.csv. By default, the font for this component is set to Courier New which is a monospaced font, with a size of 0.05. These can be changed in the formatting tab of the component. For the letter height, you can create a column in Stimuli.csv that will change the letter height for each item to account for sentences of different lengths. Since there are many variables to this (screen size, aspect ratio, etc.)  calculate this optimally in the SPR_Gen.py script is not currently supported.

The Continue component should be self explanatory.

The 'Increment' code block will increase the value of the 'r_num' variable by 1 at the end of the routine. This will then change the value of the 'Region' variable. This is will change the region being displayed by Window_Text on the next iteration of the routine. r0 --> r1 --> ... --> r(n).

Once this routine has repeated a number of times equal to the Region_Num value from Stimuli.csv (when the sentence is complete), the experiment will leave the SPR_Loop and move to the CompQ routine.

## CompQ Routine:

The Question component calls the CompQ parameter from Stimuli.csv and displays the comprehension question.

The Response component is by default set to accept either a 'y' or 'n' key press with a "correct" key '$CompAns' that corresponds to the column of the same name in Stimuli.csv.

The 'Reset' code block functions much like the 'Initialization' code block in the Intro routine. This code block resets the value of 'r_num' to 0 and thereby restarts the Region value to r0 to prepare for the next item in Item_Loop.

Upon exiting the CompQ routine, the Item_Loop will move the experiment to the next routine and start the SPR_Loop again. If there are no items left for Item_Loop (i.e. all items have been seen), the Item_Loop will terminate and the experiment will move to the Exit Routine. The text and key response components in the Exit routine are both placeholders.


