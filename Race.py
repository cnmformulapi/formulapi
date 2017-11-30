### Settings for this race ###
laps = 99

### Start of the race ###
# Wait until we can see the track
while not TrackFound():
	WaitForSeconds(1.0)
# We can see the track now, start by following the lane we are on
trackLane = round(CurrentTrackPosition())
AimForLane(trackLane)
# Save a start-line image
photo = GetLatestImage()
SaveImage(photo, 'Start-line')
# Start logging what happens
StartUserLog()
#StartDetailedLog()
# Wait for the go signal from the start/stop lights.
WaitForGo()
# Go at max speed
Speed(80)
### During the race ###
# Keep going until we have fished all of the laps

AimForLane(trackLane)
WaitForWaypoint(2)
AimForLane(trackLane)
WaitForWaypoint(3)
AimForLane(trackLane)
while True:
	
	"""WaitForWaypoint(4)
	AimForLane(0.0)
	WaitForWaypoint(5)
	AimForLane(1.0)
	WaitForWaypoint(6)
	AimForLane(-0.5)
	WaitForDistance(1.25)
        WaitForWaypoint(7)
	AimForLane(-1.0)
	WaitForWaypoint(8)
	AimForLane(-1.0)
	WaitForWaypoint(9)
	AimForLane(-1.0)
	WaitForWaypoint(1)
	AimForLane(-1.0)
	WaitForWaypoint(2)
	AimForLane(-1.0)"""
	
        WaitForWaypoint(4)
        AimForLane(1.0)
	Speed(80)
        WaitForWaypoint(5)
        AimForLane(1.0)
        WaitForWaypoint(6)
        AimForLane(-2)
        WaitForDistance(1.25)
        WaitForWaypoint(7)
	Speed(30 )       
	AimForLane(-2.0)
        WaitForWaypoint(8)
        #AimForLane(-2.0)
        WaitForWaypoint(9)
	Speed(80)        
	#AimForLane(-2.0)
	WaitForDistance(1)
        WaitForWaypoint(1)      
	AimForLane(-2.0)
	Speed(100)
        WaitForWaypoint(2)
        AimForLane(-2.0)
	WaitForWaypoint(3)
	AimForLane(0)
	
        
### End of the race ###
# Save a finish-line image
photo = GetLatestImage() # continue running just for a bit to ensure we've definately crossed the finish line!
SaveImage(photo, 'Finished')
WaitForWaypoint(3)
# Slow the MonsterBorg down gradually from 100% to 0%
for slowing in range(99, -1, -1):
	Speed(slowing)
	WaitForSeconds(0.01)
# Stop the logging
EndUserLog()
EndDetailedLog()
# End the race (will stop the robot and end the program)
FinishRace()

