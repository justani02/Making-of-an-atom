 ### MAKING OF AN ATOM 
*************************************

In utopia, God is making an atom. Each atom consists of N particles, where an electron is represented by a '0' charge and a proton by a '1'.In utopia, opposites do not exist, and no electron-proton can stay in 1 atom.

In this realm, an atom can be composed of only electrons or protons. If both an electron and proton exist in the atom, the two will disappear. This keeps on happening until the atom becomes stable.

Return the final number of particles in the given atom.

Input Format

First line contains an integer n, the number of particles
Second line contains a binary string

Output Format

Print an Integer, the number of particles in the atom

Sample Input 0

8
11101111
Sample Output 0

6
One electron disappears with 1 proton, leaving the final size of the atom to be 6.
*************************************

# Here's a step-by-step explanation of the code:

1. The function `count_particles` takes two arguments: `n` (the number of particles) and `binary_string` (the binary string representing the charges in the atom).

2. We initialize an empty stack, which will be used to keep track of the charges.

3. We iterate through each charge in the binary string using a loop.

4. Inside the loop, we check if the stack is not empty (`stack`) and if the current charge is different from the top of the stack (`stack[-1] != charge`). This condition determines if we have an electron-proton pair.

5. If we have an electron-proton pair, we remove the top element from the stack using `stack.pop()`.

6. If the condition in step 4 is not met (i.e., the current charge matches the top of the stack or the stack is empty), we add the charge to the stack using `stack.append(charge)`.

7. After iterating through all the charges in the binary string, we return the length of the stack using `len(stack)`. This represents the final number of particles in the atom.

8. Finally, we can call the `count_particles` function with the given input values and print the result.

The code essentially eliminates electron-proton pairs from the binary string by using a stack. The remaining elements in the stack after processing all the charges represent the final particles in the atom.
