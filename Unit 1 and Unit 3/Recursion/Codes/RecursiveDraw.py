import turtle

def draw_branch(t, branch_length, depth):
    if depth == 0: # Base Case
        return
    else:
        # Draw the main branch
        t.forward(branch_length)
        # Turn left and draw a smaller branch (recursive call)
        t.left(30)
        draw_branch(t, branch_length * 0.7, depth-1)
        # Turn right and draw another smaller branch (another recursive call!)
        t.right(60)
        draw_branch(t, branch_length * 0.7, depth-1)
        # Go back to the start of this branch
        t.left(30)
        t.backward(branch_length)

# Setup
window = turtle.Screen()
artist = turtle.Turtle()
artist.left(90) # Point the turtle upward
artist.speed('fastest')

# Draw the tree!
draw_branch(artist, 100, 7) # Depth of 7 recursive calls
window.exitonclick()
