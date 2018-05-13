from subprocess import call, check_call, check_output
import os


#go to dir & git pull
os.chdir("/var/www/SapperCodingPlatform/express")
call(['git', 'pull'])


#pm2 should be running with pm2's app 0 being server.js
#but we can't assume it is, esp. if pushing bug fix.
try:
  PM2_NOT_STARTED = call(['pm2', 'stop', '0'])
  #gets set to 0 if no errors
  #1 on error when app 0 isn't running
except Exception:
  PM2_NOT_STARTED = 1

os.chdir('DeveloperMarketplace')
try:
  call(['ng', 'build', '--prod'])
except Exception:
  yn = input("production build failed. try dev build (y/n) ? ")
  if yn.lower() == 'y':
    call(['ng', 'build'])

os.chdir('..')
if PM2_NOT_STARTED:
  call(['pm2', 'start', 'server.js'])
else:
  call(['pm2', 'start', '0'])
