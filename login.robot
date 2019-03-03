*** Settings ***


*** Variables ***
https://www.facebook.com/
chrome

*** Keywords ***


*** Test Cases ***
login test
  Open browser to the login page
  input username demo
  CLOSE BROWSER

