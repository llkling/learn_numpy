# NumPy

## What is NumPy?

At its simplest, NumPy (Numerical Python) is a library that allows Python to handle massive amounts of numerical data with extreme speed. While standard Python is great for general logic, it struggles with heavy math; NumPy fixes this by introducing the N-dimensional array (ndarray).

* Basically, it is a library that help the code to using the memories more efficiently and faster runtime.

Example: Filtering scores
* The standard Python way
    ```py
    scores = [72, 95, 50, 84, 91]
    high_scores = []

    for s in scores:
        if s > 80:
            high_scores.append(s)
    ```
* The NumPy way
```py
    import numpy as np

    scores = np.array([72, 95, 50, 84, 91])
#This creates a 'mask' (True/False) and filters instantly
    high_scores = scores[scores > 80]
```

## Linear Algebra

**Linear Algebra** is essentially the mathematics of **arrays**. While basic arithmetic deals with single numbers ($2 + 2 = 4$), Linear Algebra deals with entire sets of numbers (vectors and matrices) at the same time.

* What is it? 
- Vector: A single row or column of data (e.g., the $[x, y, z]$ coordinates of a point)
- Matrix: A table of data (e.g., an Excel spreadsheet or a digital image).A Matrix is what happens when you stack vectors on top of each other. It’s a 2D grid with __Rows__ (horizontal) and __Columns__ (vertical).
- Transformation: Using math to move, rotate, scale, or change those grids.

Example:
A: Digital Images (The Matrix)
- Outside World: 
    When you look at a digital photo, you see a picture.
- Coding World: 
    The computer sees a Matrix where every cell is a number representing a pixel's brightness.
- *Linear Algebra in Action*: 
    When you apply a "Brighten" filter, the code doesn't loop through every pixel. It performs Matrix Addition, adding a value (e.g., $+10$) to the entire grid at once.

B: Recommendation Engines (The Dot Product)
- Outside World: 
    Netflix suggests a movie because "Users who liked Inception also liked The Matrix."
- Coding World: Your interests are stored as a Vector (a list of 1s and 0s for movies you liked).
- *Linear Algebra in Action*: 
    To find a "match," the code calculates the Dot Product between your vector and another user's vector. The higher the resulting number, the closer the match.

C: Navigation & GPS
- Outside World: 
    You rotate a map on your phone to see which way you are facing.
- Coding World: 
    Your location is a vector.
- *Linear Algebra in Action*: 
    To rotate the map, the phone multiplies your location vector by a Rotation Matrix. This instantly calculates the new coordinates for every street and icon on your screen.

### 1. Inner or Dot Product of Two n-vectors

__Dot Product__ (also called the Inner Product): This is the "glue" that allows us to combine two vectors into a single number. It tells us how much two vectors "align" with each other.
To find a Dot Product: 
    __Multiply__ the corresponding components (1st to 1st, 2nd to 2nd) and the __Add__ them up
Mathematically, if $A = [a_1, a_2]$ and $B = [b_1, b_2]$, the dot product is:
            $$A \cdot B = (a_1 \times b_1) + (a_2 \times b_2)$$

In NumPy, we use: 
- `np.inner()`
- `np.dot()`
- `@`

`.shape` is an attribute that tells you the dimensions of your array
| Array Type | Example Shape | Meaning |
| ---------- |---------------|---------|
|  1D Vector |`(5,)`| A single row (or column) with 5 elements|
|  2D Matrix | `(3, 4)`|3 Rows and 4 Columns|
| 3D Tensor|`(2, 3, 4)`|2 "pages",each containing a 3×4 matrix|

The `.shape` always return in a tuple of integers.

### 2. Euclidean Norm of an n-vector

If a vector is a "point in space," the **Euclidean Norm** is simply the straight-line distance from the origin $(0, 0)$ to that point. In plain English: **it is the length of the vector.**

To find the norm of a vector:
   - **Square** every number in the vector.
   - **Add** them all together.
   - Take the **Square Root** of the total.

Mathematically, for vector $x$:
    $$||x|| = \sqrt{x_1^2 + x_2^2 + \dots + x_n^2}$$

In NumPy, we use:
- `np.linalg.norm()`

    * The Root Mean Square (rms)
The RMS is essentially a way to calculate the "average magnitude" of a set of numbers, especially when some are positive and some are negative.
    
    $$RMS = \sqrt{\frac{x_1^2 + x_2^2 + \dots + x_n^2}{n}}$$

In the Coding world, using *rms* tells you how much "error" your code is. It emphasizes the big and heaviest error for you to see, make your code analyzing more accurate.

In NumPy, we use:
```py
- rms = np.sqrt(np.mean(v**2))
#v is the array
```
### 3. Linear Combination of a Set Vectors

It is when you multiply a vector with a scalar, and add them together to create a brand new vector

If we have a set of vectors $\{v_1, v_2, \dots, v_n\}$ and a set of scalars $\{c_1, c_2, \dots, c_n\}$, the linear combination looks like this:

    $$w = c_1v_1 + c_2v_2 + \dots + c_nv_n$$

In NumPy, we use:
- `*` and `+` `#operator`

### 4. Linear Dependence vs Independence

- A __dependent__ vector means they are made up from scaling or adding the others. It doesn't provide any new information. It can be track back from one origin vector. It is on the same dimension (one line).

- An __independent__ vector means they are unique/origin vector/data that provide a whole new information or a whole new "dimension". There is no way to create an independent vector from the others.

- Mathematically, a set of vectors is dependent if you can find a __linear combination__ of them (besides all zeros) that equals zero.

### 5. Linear Independence: Determinant and Inverse

These two are tools to tell if your vectors(data) are dependent or independent.
     **a.The Determinant**
The Independence Rule:
 - If $\det(A) \neq 0$: The vectors are Linearly Independent. They spread out and create a real area or volume. (they spread out in different dimension)
 - If $\det(A) = 0$: The vectors are Linearly Dependent. The shape has "collapsed." In 2D, this means the vectors lie on the same line (Ox or Oy or Oz), so the area is zero. 

    **b. The Inverse**
The Inverse is the "Undo" button. If you multiply a matrix by its inverse, you get the Identity Matrix (the matrix equivalent of the number 1) #basically a matrix that returns the same result

The Independence Rule:
 - A matrix only has an inverse if its vectors are Linearly Independent.
 - There is no inverse (determinant=0) means it's Dependent Vector

In NumPy, we use:
- `np.linalg.det()`
- `np.linalg.inv()`

*Note*: The computer stores and handles numbers a llite different. Sometimes you will run up to a **Rounding Error** or **Floating-Point Artifact**, which mean they are a little off the numbr $0$ in this case.

### 6. Reduced Row Echelon Form (RREF)

It a way to find out how many **Independence** are hiding in a Matrix. 
(It required SymPy to run the `rref()` function)

### 7. Inverse in Matrix

Similar to vectors, the Inverse $A^{-1}$ is the matrix that "undoes" whatever $A$ did. If you multiply them together, you get back to the Identity Matrix $I$.
    $$A \cdot A^{-1} = I$$

The Identity Matrix will have the form of a square matrix that has 1s on the main diagonal (from top-left to bottom-right) and 0s everywhere else.
    $$I = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix}$$

### 8. Eigenvalue and Eigenvector

Usually a vector will change direction whenever they are @ by a matrix. However, there are a few special directions where the vector **stays on its original line.**
- Eigenvector ($\mathbf{v}$): A vector that does not change direction when a transformation is applied. It only gets stretched or squished.
- Eigenvalue ($\lambda$): The scalar that tells you *how much* that eigenvector was stretched or squished. 
    $$A\mathbf{v} = \lambda\mathbf{v}$$

In NumPy, we use: 
- `np.linalg.eig()`

### 9. Standard Basis Vectors

Think of them as the "pure" unit measurment. A foundation for everything else. Those are always __Independent__.

In a 2D space, the standard basis vectors are usually called $\mathbf{i}$ and $\mathbf{j}$:
    $\mathbf{i} = \begin{bmatrix} 1 \\ 0 \end{bmatrix}$ (One unit step exactly along the $x$-axis)
    $\mathbf{j} = \begin{bmatrix} 0 \\ 1 \end{bmatrix}$ (One unit step exactly along the $y$-axis)

Every other vector in your space is just a "recipe" or a linear combination of these two. For example, the vector $\begin{bmatrix} 3 \\ 2 \end{bmatrix}$ is just $3\mathbf{i} + 2\mathbf{j}$.

In NumPy, they are usually to test how a matrix transformation behave. 
- `i=np.array[1,0]`

### 10. Matrix Transformation

In coding, a matrix acts like a *function*. Every matrix A takes the entire grid of space and pushes, pulls, or twists it into a new *shape*.

*Example:*
- Translation/Scaling: Making a character larger or smaller.
- Rotation: Turning a camera to look around a corner.
- Shearing: Distorting an image to create a sense of speed or motion.

In NumPy, we use:
- `@` #dot product

### 11. Normalized and Unit Vector

- A **Unit Vector** is a vector that has a magnitude (length) == 1.
- **Normalization** is the mathematical process of taking any vectors to scale into **Unit Vectors**.

Real-World Example: AI Similarity (Cosines)
- "User A" likes 100 action movies and 50 comedies.

- "User B" likes 2 action movies and 1 comedy.

Mathematically, these users are identical in their tastes—they both like action twice as much as comedy. However, the length of User A's vector is much larger because they watch more movies.

By Normalizing both users into Unit Vectors, we can compare their "directions" directly. This is called Cosine Similarity, and it’s how Netflix or Spotify knows you have the same taste as someone else, even if you’ve consumed less content.

Mathematically: 
To get the unit vector $\mathbf{\hat{v}}$ (pronounced "v-hat"), you divide the original vector by its own magnitude.
    $$\mathbf{\hat{v}} = \frac{\mathbf{v}}{\|\mathbf{v}\|}$$

In NumPy, we use:
-`v / np.linalg.norm(v)` #v is the vector




