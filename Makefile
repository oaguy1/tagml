# specify all source files here
SRC = parse.c main.c 

# specify target here (name of executable)
TARG = TagML

# specify compiler, compile flags, and needed libs
CC = gcc
OPTS =`xml2-config --cflags`
LIBS = -lm `xml2-config --libs`

# this translates .c files in src list to .o’s
OBJ = $(SRC:.c=.o)

# all is not really needed, but is used to generate the target
all: $(TARG)

# this generates the target executable
$(TARG): $(OBJ)
	echo "Building Executable"
	$(CC) -o $(TARG) $(OBJ)

# this is a generic rule for .o files
%.o: %.c
	echo "Building Objects"
	$(CC) $(OPTS) $(LIBS) -c $< -o $@

# and finally, a clean line
clean:
	echo "Cleaning Build"
	rm -f $(OBJ) $(TARG)
