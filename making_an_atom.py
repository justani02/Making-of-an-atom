# to find the final number of particles in the given atom, we need to eliminate the pairs of electrons and protons until the atom becomes stable.

def return_final_number_of_particles(n, particle_string):
    stack = []

    for particle in particle_string:
        if stack and stack[-1] != particle:
            stack.pop()
        else:
            stack.append(particle)

    return len(stack)

# If we have an electron-proton pair, we remove the top element from the stack using stack.pop().
# After iterating through all the charges in the binary string, we return the length of the stack using len(stack). This represents the final number of particles in the atom.

# read input
n = int(input())
particle_string = input()

# find the final number of particles
final_atom_particles = return_final_number_of_particles(n, particle_string)

# Print the result
print(final_atom_particles)

# This code maintains a stack. Inside the loop, we check if the stack is not empty (stack) and if the current charge is different from the top of the stack (stack[-1] != charge). This condition determines if we have an electron-proton pair.
