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
Speed(100)
### During the race ###
# Keep going until we have fished all of the laps

while True:
	
	WaitForWaypoint(2)
	AimForLane(-1.0)
	Speed(100)
	WaitForWaypoint(3)
	AimForLane(-1.0)
	Speed(100)
	WaitForWaypoint(4)
	AimForLane(-2.0)
	Speed(100)
	WaitForWaypoint(5)
	AimForLane(-2.0)
	Speed(100)
	WaitForWaypoint(6)
	AimForLane(-1.0)
	Speed(100)
	WaitForWaypoint(7)
	AimForLane(-1.0)
	Speed(100)
	WaitForWaypoint(8)
	AimForLane(-2.0)
	Speed(100)
	WaitForWaypoint(9)
	AimForLane(-2.0)
	Speed(100)
	nt(1)
	AimForLane(-1.0)
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

