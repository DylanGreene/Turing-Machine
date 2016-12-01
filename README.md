# Turing-Machine

Written by: Dylan Greene  
Updated on: 30 November 2016

To run the simulator, ensure that tm.py is executable. To ensure this, simply
run the command 'chmod +x tm.py'.

The simulator must be run with a Turing Machine definition file which follows
the following format:
  * Line 1: The name of the TM program. This should be echoed to stdout before
  the rules are echoed.
  * Line 2: The set of symbols to be used for the input alphabet ∑: only
  single ASCII letters are allowed, comma separated, as in a,b,c,… "\_" is not
  allowed as an alphabet character.
  * Line 3: The additional set of symbols beyond Σ that can also be used for
  the tape alphabet Γ: only single ASCII letters are allowed, comma separated,
  as in a,b,c,… You do not have to duplicate Σ nor include "\_". If there are
  no additional characters, leave this line blank.
  * Line 4: The names of the states, separated by commas, as in q0,q1,… There
  is no constraint on the length of a state name.
  * Line 5: The name of the state that should be considered the start state.
  * Line 6: The name of the state that should be considered the accepting
  state.
  * Line 7: The name of the state that should be considered the rejecting
  state.
  * Line 8 and beyond: one transition rule per line, in the format:
   \<Initial\_State\>,\<Tape\_Symbol\>|\<New\_State\>,\<New\_Tape\_Symbol\>,\<D
   irection\>
     * The direction shall be either a "L" for left, of "R" for right.

Processing of rules stops with the end of file.

Additionally, an test file containing the the character strings to run against
the machine must be supplied. The format for the test file is simply one line
for each string to be input to the machine.

To run the simulator with these two files, execute the command './tm.py
TM_DEF_FILE TEST_STRING_FILE'. A help message will be displayed if usage is
incorrect.

Once run, the simulator will print the transitions for every string, as
well as if each string is accepted or rejected by the machine.

Specifically, the output will follow the format:
  * On the first line, the initial tape values, prefixed by “Tape: “
  * For each transition, the following on a separate line:
  \<Step\#\>@\<Current\_Tape\_Head\_Index\>\#\<Rule\_Number\>:\<Initial\_State\_Name\>,\<Current\_Tape\_Symbol\>, | \<New\_State\_Name\>,\<New\_tape\_symbol\>,\<New\_tape\_index\>
  * After all transitions have been performed, print either “Accepted” (if the
  last state was an accepting state),“Rejected” (if the last state was a
  rejecting state), or “Error”. This should be followed by a “:” and the
  contents of the tape as a string up to (but not including) the first blank.

Additionally, I have designed my own TM and included it in the Custom
subdirectory. This TM is designed to compute the logical bitwise OR of two
strings separated by a #. The TM will store the bitwise OR in the front of the
\# symbol, and x out the second string following the #.
