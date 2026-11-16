import numpy as np

# Nodes A, B, C form one group; D, E, F form another; Connected by one edge: C-D.
A = np.array([
    [0, 1, 1, 0, 0, 0],
    [1, 0, 1, 0, 0, 0],
    [1, 1, 0, 1, 0, 0],
    [0, 0, 1, 0, 1, 1],
    [0, 0, 0, 1, 0, 1],
    [0, 0, 0, 1, 1, 0]
], dtype=float)

# Degree matrix
D = np.diag(A.sum(axis=1))

# Graph Laplacian
L = D - A

eigenvalues, eigenvectors = np.linalg.eigh(L)

fiedler = eigenvectors[:, 1]

# The eigenvector's sign is arbitrary; make the first entry positive
if fiedler[0] < 0:
    fiedler = -fiedler

nodes = np.array(["A", "B", "C", "D", "E", "F"])
group1 = nodes[fiedler > 0]
group2 = nodes[fiedler < 0]

print("Eigenvalues:", np.round(eigenvalues, 3))
print("Second-smallest eigenvalue:", round(eigenvalues[1], 3))
print("Fiedler vector:", np.round(fiedler, 3))
print("Group 1:", group1)
print("Group 2:", group2)


print("\n--------Explaination--------");
print("\nWhat the result means:")
print("The network is split into two groups based on its connections.")
print("Positive Fiedler values belong to Group 1.")
print("Negative Fiedler values belong to Group 2.")

print("\nFiedler value for each person:")
for name, value in zip(nodes, fiedler):
    group = "Group 1" if value > 0 else "Group 2"
    print(f"{name}: {value:+.3f} -> {group}")

print("\nInterpretation:")
print("A, B, C form one closely connected group.")
print("D, E, F form another closely connected group.")
print("The groups are joined by the friendship between C and D.\n")







