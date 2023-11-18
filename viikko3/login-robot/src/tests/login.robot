*** Settings ***
Resource  resource.robot
Test Setup  Create User And Input Login Command

*** Test Cases ***
Login With Correct Credentials
    Input Credentials  kalle  kalle123
    Output Should Contain  Logged in    

Login With Incorrect Password
    Input Credentials kalle wrongpassword
    Output Should Contain Incorrect password

Login With Nonexistent Username
    Input Credentials nonexistentuser password
    Output Should Contain User not found

*** Keywords ***
Create User And Input Login Command
    Create User  kalle  kalle123
    Input Login Command
