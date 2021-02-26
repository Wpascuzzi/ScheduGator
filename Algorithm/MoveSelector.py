import copy
from Shift import Shift
from Schedule import Schedule
import Constraints
from Employee import Employee

# Author: Will Pascuzzi
# This will contain methods responsible for generating moves. 
# These moves include attempting to place a shift in a possible location, and changing the schedule to better fit an new entity

# methods should return a list of schedule states found
# this set of states can be run through a scorer, which can return the most optimal state to choose

# This attempts to place a given entity in a given schedule state without moving other entities.
# returns a list of possible states to be run through the scorer
def tryToPlaceBasic(currentState : Schedule, constraints):
    possibleStates = []
    for entity in currentState.roster.values(): #TODO: remove employees from the roster when their maximum hours are spent
        for day in currentState.schedule:
            for sLen in constraints.shiftSizes:
                for start in currentState.unfilled[day]: #start times will only involved those that are unfilled
                    newShift = Shift.createShift(entity.ID, start, sLen, day)
                    # create a copy of the currentstate and add the newly generated shift.
                    # note: this probably will end up using a lot of memory. 
                    # Hopefully can find a way to only copy certain parts of the schedule
                    newState = copy.deepcopy(currentState)
                    newState.insertShift(newShift, day)                 
                    possibleStates.append(newState) # add another potential state to the list
    return possibleStates


             

