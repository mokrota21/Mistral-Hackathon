monty <- function() {
doors <- 1:3

# randomly pick where the car is
cardoor <- sample(doors,1)

# prompt player
print("Monty Hall says ‘Pick a door, any door!’")

# receive the player’s choice of door (should be 1,2, or 3)
chosen <- scan(what = integer(), nlines = 1, quiet = TRUE)

# pick Monty’s door (can’t be the player’s door or the car door)
if (chosen != cardoor) montydoor <- doors[-c(chosen, cardoor)]
else montydoor <- sample(doors[-chosen],1)

# find out whether the player wants to switch doors
print(paste("Monty opens door ", montydoor, "!", sep=""))
print("Would you like to switch (y/n)?")
reply <- scan(what = character(), nlines = 1, quiet = TRUE)

# interpret what player wrote as "yes" if it starts with "y"
if (substr(reply,1,1) == "y"){
chosen <- doors[-c(chosen,montydoor)]
}

# announce the result of the game!
if (chosen == cardoor) print("You won!")
else print("You lost!")
}
```

The print command prints its argument to the screen. We combine this with the paste command since if we used print("Monty opens door montydoor") then R would literally print “Monty opens door montydoor”. The scan command interactively requests input from the user; we use what = integer() when we want the user to enter an integer and what = character() when we want the user to enter text. Using substr(reply,1,1) extracts the first character of reply, in case the user replies with “yes” or “yep” or “yeah!” rather than with “y”.

### 2.11 Exercises

Exercises marked with 8 have detailed solutions at http://stat110.net.

####